🚀 Overview

The AI Social Media Agent is a Streamlit-based application that automatically generates:
✔ Social media post ideas
✔ Captions (short + long)
✔ Hashtags
✔ Image prompts
✔ Posting schedules
✔ Exportable CSV campaign plans

It uses the new OpenAI API (v1.x) and supports multiple models like gpt-4o-mini, gpt-4o, and gpt-4o-mini-instruct.

📂 Project Structure

├── app.py              # Streamlit UI application
├── agent.py            # Core logic for generating ideas, captions & schedule
├── utils.py            # Helper for saving CSV files
├── requirements.txt    # Required dependencies
└── outputs/            # Auto-created folder to store generated CSVs

🧠 Features

✅ 1. Automated Content Idea Generation

Generates N social media ideas using brand info, voice, audience, goals, and selected platforms.

✅ 2. Caption Generator

For each idea, the agent creates:

Short captions

Long captions

Suggested hashtags

Image prompt

✅ 3. Campaign Scheduling

Automatically calculates:

Total posts needed

Weekly posting slots

Balanced cross-platform schedule

✅ 4. CSV Export

Every generated campaign can be saved as a CSV file via:

outputs/plan.csv

✅ 5. Modern OpenAI API (v1.x)

Uses the new OpenAI() client and latest chat completions format.

⚙️ Installation & Setup

1️⃣ Clone the repository
git clone https://github.com/your-repo/social-media-agent.git
cd social-media-agent

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Set OpenAI API key

You can set it as an environment variable:

export OPENAI_API_KEY="your_api_key_here"


Or enter it directly in the Streamlit sidebar.

▶️ Running the App

Launch the Streamlit application:

streamlit run app.py


The browser will open automatically at:

http://localhost:8501

🧩 Code Summary

agent.py

Contains the SocialMediaAgent class that:

Calls OpenAI models

Generates content ideas

Produces captions

Parses AI-generated JSON

Builds the final posting schedule

app.py

Implements the Streamlit interface:

Inputs (brand, voice, audience, goal)

Platform selection

Date range

Generate & Export buttons

Displays schedule & ideas in tables

utils.py

Contains helper for:

Saving generated dataframes as CSV into outputs/.

📦 Requirements

From requirements.txt:

streamlit>=1.20
openai>=0.27.0
python-dateutil
pandas

📝 Example Workflow

Enter brand details

Choose platforms (Instagram, X, LinkedIn)

Pick campaign date range

Generate ideas & schedule

Export plan to CSV

🛠 Future Enhancements (Optional)

Image generation with DALL·E

Multi-language content output

Downloadable PDF reports

User login/profile-based campaigns