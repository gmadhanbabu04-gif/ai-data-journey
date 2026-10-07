"""
Day 2: CSV Data Ingestion, Cleaning & Export Pipeline
Author: Madhan Babu
Topic: File I/O, csv.DictReader, Feature Engineering, csv.DictWriter
"""

import csv
import os

RAW_FILE = "raw_students.csv"
CLEAN_FILE = "cleaned_students.csv"

# 1. Step 1: Create a Sample Raw CSV File (Simulating real-world dirty data)
sample_csv_data = """id,name,score,branch,city
101,Madhan,92,AI&DS,Erode
102,Kaviyan,,AI&DS,Coimbatore
103,Priyanka,88,ECE,Salem
104,Abishek,absent,CSE,Erode
105,Niranjani,95,,Tirupur
106,Ramesh,74,CSE,Chennai
107,Sanjay,invalid,AI&DS,Erode
"""

with open(RAW_FILE, "w", encoding="utf-8") as f:
    f.write(sample_csv_data.strip())
print(f"--- 1. Generated '{RAW_FILE}' successfully ---")


# 2. Step 2: Extract - Read CSV using csv.DictReader
# DictReader converts each row directly into a Python Dictionary!
records = []
with open(RAW_FILE, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        records.append(row)

print(f"\n--- 2. Extracted {len(records)} Records from CSV ---")
for r in records[:3]:  # Print first 3 rows
    print(r)


# 3. Step 3: Transform (Clean Dirty Values & Feature Engineering)
cleaned_records = []
for row in records:
    # A. Clean Score using try-except
    try:
        clean_score = float(row["score"])
    except (ValueError, TypeError):
        clean_score = 0.0

    # B. Clean Missing Branch
    clean_branch = row["branch"] if row["branch"].strip() else "Unknown"

    # C. Feature Engineering: Create a new 'status' column (Pass / Fail)
    status = "Pass" if clean_score >= 75 else "Fail"

    cleaned_records.append({
        "id": row["id"],
        "name": row["name"],
        "score": clean_score,
        "branch": clean_branch,
        "city": row["city"],
        "status": status  # New engineered column
    })

print(f"\n--- 3. Cleaned Sample (First 3) ---")
for r in cleaned_records[:3]:
    print(r)


# 4. Step 4: Analytics (City Count & Pass Rate)
city_counts = {}
passed_count = 0
for r in cleaned_records:
    city = r["city"]
    city_counts[city] = city_counts.get(city, 0) + 1
    if r["status"] == "Pass":
        passed_count += 1

print("\n--- 4. Analytics Summary ---")
print(f"Students per City: {city_counts}")
print(f"Total Passed: {passed_count} / {len(cleaned_records)}")


# 5. Step 5: Load - Write Cleaned Data to a New CSV File
fieldnames = ["id", "name", "score", "branch", "city", "status"]
with open(CLEAN_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  # Write column names
    writer.writerows(cleaned_records)  # Write all rows

print(f"\n--- 5. Successfully exported clean data to '{CLEAN_FILE}'! ---")