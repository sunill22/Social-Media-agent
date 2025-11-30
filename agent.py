# agent.py  (NEW OPENAI v1.x VERSION)

from openai import OpenAI
import os
from dateutil import parser
from datetime import timedelta
import json
import random
import re

class SocialMediaAgent:
    def __init__(self, model="gpt-4o-mini", temperature=0.7):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model
        self.temperature = temperature

    def call(self, prompt, max_tokens=512):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()

    def parse_json_array(self, text):
        try:
            match = re.search(r"(\[.*\])", text, re.S)
            if match:
                return json.loads(match.group(1))
        except:
            pass
        return []

    def generate_ideas_prompt(self, brand, voice, audience, goal, platforms, num):
        return f"""
Generate {num} social media content ideas for the brand "{brand}".
Brand voice: {voice}
Audience: {audience}
Goal: {goal}
Platforms: {', '.join(platforms)}

Return a JSON array. Each element MUST contain:
- title
- type
- brief
- suggested_hashtags
- image_prompt
"""

    def generate_caption_prompt(self, title, brief, voice, platform):
        return f"""
Create captions for: "{title}"
Brief: "{brief}"
Brand Voice: "{voice}"
Platform: {platform}

Return JSON with:
- caption_short
- caption_long
- suggested_hashtags
"""

    def generate_campaign(self, brand_name, brand_voice, audience, goal,
                          platforms, start_date, end_date, posts_per_week=3, num_ideas=5):

        # 1️⃣ Generate ideas
        prompt = self.generate_ideas_prompt(brand_name, brand_voice, audience, goal, platforms, num_ideas)
        raw_ideas = self.call(prompt, max_tokens=700)
        ideas = self.parse_json_array(raw_ideas)

        if not ideas:
            ideas = [
                {
                    "title": f"Idea {i+1}",
                    "type": "educational",
                    "brief": "Simple fallback idea",
                    "suggested_hashtags": "#brand",
                    "image_prompt": "Minimal design"
                }
                for i in range(num_ideas)
            ]

        # 2️⃣ Create posting schedule
        start = parser.parse(start_date).date()
        end = parser.parse(end_date).date()
        total_days = (end - start).days + 1
        weeks = total_days / 7
        total_posts = max(1, int(posts_per_week * weeks))
        step = max(1, int(7 / posts_per_week))

        dates = []
        d = start
        while d <= end and len(dates) < total_posts:
            dates.append(str(d))
            d += timedelta(days=step)

        while len(dates) < total_posts:
            dates.append(str(start + timedelta(days=random.randint(0, total_days-1))))

        # 3️⃣ Generate captions
        schedule = []
        for idx, d in enumerate(dates):
            idea = ideas[idx % len(ideas)]
            platform = platforms[idx % len(platforms)]
            cap_prompt = self.generate_caption_prompt(
                idea["title"], idea["brief"], brand_voice, platform
            )

            try:
                cap_raw = self.call(cap_prompt, max_tokens=400)
                cap_json = json.loads(re.search(r"(\{.*\})", cap_raw, re.S).group(1))
            except:
                cap_json = {
                    "caption_short": idea["brief"],
                    "caption_long": idea["brief"] + " Learn more!",
                    "suggested_hashtags": idea["suggested_hashtags"]
                }

            schedule.append({
                "date": d,
                "platform": platform,
                "post_title": idea["title"],
                "post_type": idea["type"],
                "caption_short": cap_json["caption_short"],
                "caption_long": cap_json["caption_long"],
                "hashtags": cap_json["suggested_hashtags"],
                "image_prompt": idea["image_prompt"]
            })

        return {"ideas": ideas, "schedule": schedule}
