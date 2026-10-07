"""
Day 2 (Part 2): Descriptive Statistics from Scratch
Author: Madhan Babu
Topic: Mean, Median, Variance, Standard Deviation, File Reading
"""

import csv
import math

CLEAN_FILE = "cleaned_students.csv"

# 1. Step 1: Read Scores from cleaned_students.csv
scores = []
with open(CLEAN_FILE, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        score = float(row["score"])
        # We only consider students who attended the exam (score > 0)
        if score > 0:
            scores.append(score)

print("--- 1. Valid Scores Extracted from CSV ---")
print(f"Scores: {scores}")
print(f"Total Active Students (N): {len(scores)}")


# 2. Step 2: Calculate Mean (Average)
def calculate_mean(data: list[float]) -> float:
    return sum(data) / len(data)

mean_score = calculate_mean(scores)


# 3. Step 3: Calculate Median (Middle Value)
def calculate_median(data: list[float]) -> float:
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    
    # If odd, take middle; if even, average the two middle values
    if n % 2 != 0:
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0

median_score = calculate_median(scores)


# 4. Step 4: Calculate Min, Max & Range
min_score = min(scores)
max_score = max(scores)
score_range = max_score - min_score


# 5. Step 5: Calculate Variance and Standard Deviation (Spread of Data)
def calculate_variance(data: list[float], mean: float) -> float:
    # Variance = average of squared differences from the Mean
    squared_diffs = [(x - mean) ** 2 for x in data]
    return sum(squared_diffs) / len(data)

def calculate_std_dev(variance: float) -> float:
    # Standard Deviation is the square root of Variance
    return math.sqrt(variance)

variance = calculate_variance(scores, mean_score)
std_dev = calculate_std_dev(variance)


# 6. Step 6: Print Professional Data Science Summary Report
print("\n" + "=" * 45)
print("       DATA SCIENCE STATISTICAL REPORT       ")
print("=" * 45)
print(f"Student Count (N)  : {len(scores)}")
print(f"Mean (Average)     : {mean_score:.2f}")
print(f"Median (Middle)    : {median_score:.2f}")
print(f"Minimum Score      : {min_score:.2f}")
print(f"Maximum Score      : {max_score:.2f}")
print(f"Score Range (Spread): {score_range:.2f}")
print(f"Variance (σ²)      : {variance:.2f}")
print(f"Standard Dev (σ)   : {std_dev:.2f}")
print("=" * 45)

# 7. Data Science Interpretation
if std_dev < 10:
    print("Insight: The student performance is consistent (Low variance).")
else:
    print("Insight: The student performance has high variation between students.")