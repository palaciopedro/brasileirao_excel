import pandas as pd
from config import OUTPUT_FILE
import os

def export_to_excel(data):
    df = pd.DataFrame(data)
    if file_exists():
        with pd.ExcelWriter(
            OUTPUT_FILE,
            mode="a",
            engine="openpyxl",
            if_sheet_exists="replace"
        ) as writer:
            df.to_excel(writer, sheet_name="Sheet1", index=False)
    else:
        df.to_excel(OUTPUT_FILE, index=False)

def file_exists():
    if os.path.exists(OUTPUT_FILE):
        return True
    else:
        return False