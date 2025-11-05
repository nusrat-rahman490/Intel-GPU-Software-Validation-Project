import pandas as pd

# Load Excel sheets
before = pd.read_excel("gpu_results.xlsx", sheet_name="Before")
after = pd.read_excel("gpu_results.xlsx", sheet_name="After")

# Merge on Test_Name
merged = before.merge(after, on="Test_Name", suffixes=("_Before", "_After"))

# Calculate % change
for col in ["FrameRate_FPS", "Memory_MB", "Temperature_C"]:
    merged[f"{col}_Change_%"] = ((merged[f"{col}_After"] - merged[f"{col}_Before"]) / merged[f"{col}_Before"]) * 100

# Flag significant regressions
merged["Regression_Flag"] = merged["FrameRate_FPS_Change_%"].apply(lambda x: "Regression" if x < -10 else "Stable")

# Show results
print(merged[["Test_Name", "FrameRate_FPS_Before", "FrameRate_FPS_After", "FrameRate_FPS_Change_%", "Regression_Flag"]])
