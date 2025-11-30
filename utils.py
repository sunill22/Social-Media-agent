import pandas as pd
import os

def save_csv(df, filename="plan.csv", folder="outputs"):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    df.to_csv(path, index=False)
    return path
