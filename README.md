# 🧩 GPU Software Validation Mini Project

## 📘 Overview

This mini-project simulates what a **Graphics Validation Intern at Intel** does — analyzing results before and after a GPU software update to identify **performance regressions** or changes in system metrics.  

The project compares test results (`Before` vs `After`) based on three key validation metrics:
- **FrameRate (FPS)** — measures graphics performance  
- **Memory Usage (MB)** — tracks how much GPU memory is consumed  
- **Temperature (°C)** — monitors GPU heat behavior  

---

## 🧠 Objective

The goal of this project is to:
1. Compare GPU performance metrics before and after a software update.
2. Identify **regressions** (e.g., FPS drop > 10%).
3. Summarize findings in a clean and interpretable way using Python and pandas.

---

## 🧰 Tools & Technologies

- **Python 3.x**
- **pandas** — for data handling  
- **Excel (.xlsx)** — for input data storage  
- **Jupyter Notebook or VS Code** — for running the analysis  

---




## 📊 Dataset

The dataset includes 50 GPU test results measured **before** and **after** an update.

Each record contains:
- `Test_Name`
- `FrameRate_FPS`
- `Memory_MB`
- `Temperature_C`

Example (Before):

| Test_Name | FrameRate_FPS | Memory_MB | Temperature_C |
|------------|----------------|-------------|----------------|
| test_01    | 120.5          | 1450        | 67.2           |
| test_02    | 115.7          | 1420        | 66.1           |

Example (After):

| Test_Name | FrameRate_FPS | Memory_MB | Temperature_C |
|------------|----------------|-------------|----------------|
| test_01    | 105.2          | 1470        | 68.0           |
| test_02    | 118.3          | 1440        | 66.3           |

---

## 🧮 Python Analysis Code

```python
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
```
---
## 📈 Sample Output

| Test_Name | FPS_Before | FPS_After | FPS_Change_% | Regression_Flag |
|------------|-------------|------------|----------------|----------------|
| test_01    | 120.5       | 105.2      | -12.7%         | Regression      |
| test_02    | 115.7       | 118.3      | +2.2%          | Stable          |
| test_03    | 98.3        | 89.1       | -9.4%          | Stable          |

---
## 📉 Data Interpretation

**FrameRate_FPS_Change_%:**  
Measures the performance difference after the update.  
Negative values indicate performance degradation.

**Regression_Flag:**  
- `"Regression"` → FPS dropped by more than **10%**  
- `"Stable"` → FPS stayed similar or improved  

**Interpretation Example:**  
- `test_01` shows a **12.7% drop** in FPS — potential **performance regression**.  
- `test_02` shows a **2.2% improvement**, so it’s marked **Stable**.  
- `test_03` is slightly lower but within tolerance, so it’s also **Stable**.  
---

## 🧩 Key Insights

- Out of **50 tests**, typically **4–6 tests** show minor regressions after a GPU update.  
- Regressions are likely due to **driver optimizations**, **memory handling changes**, or **thermal throttling**.  
- Tests with consistent performance indicate **stable GPU behavior**.  

---


