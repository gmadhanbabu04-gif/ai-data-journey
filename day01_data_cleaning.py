"""
Day 1 (Part 2): Handling Dirty Data & Safe Type Conversion
Author: Madhan Babu
Topic: Data Cleaning, Exception Handling (try-except), Sets & Imputation
"""

# 1. A Typical "Dirty" Real-World Dataset
raw_student_records = [
    {"id": 201, "name": "Madhan", "score": "95", "branch": "AI&DS"},
    {"id": 202, "name": "Kaviyan", "score": None, "branch": "AI&DS"},       # Missing score
    {"id": 203, "name": "Priyanka", "score": "88", "branch": "ECE"},
    {"id": 204, "name": "Abishek", "score": "absent", "branch": "CSE"},     # Invalid text score
    {"id": 205, "name": "Niranjani", "score": 92, "branch": "AI&DS"},
    {"id": 206, "name": "Ramesh", "score": "60", "branch": None},          # Missing branch
    {"id": 207, "name": "Madhan", "score": "95", "branch": "AI&DS"},        # Duplicate record
]

print("--- 1. Raw Dirty Records Count ---")
print(f"Total raw records: {len(raw_student_records)}")


# 2. Extract Unique Branches using Python SET
# Set automatically removes duplicates (Key Data Engineering Concept)
unique_branches = {
    record["branch"] for record in raw_student_records if record["branch"] is not None
}
print("\n--- 2. Unique Valid Branches Found ---")
print(unique_branches)


# 3. Data Cleaning Pipeline Function
def clean_record(record: dict) -> dict:
    """
    Cleans a single student record:
    - Converts string scores to float safely using try-except.
    - Fills missing/invalid scores with a default value (0.0).
    - Fills missing branch with 'Unknown'.
    """
    cleaned = record.copy()
    
    # Safe Score Conversion
    raw_score = cleaned.get("score")
    try:
        cleaned["score"] = float(raw_score)
    except (ValueError, TypeError):
        # Handles None, 'absent', 'N/A' without crashing the script
        cleaned["score"] = 0.0

    # Handling Missing Branch
    if not cleaned.get("branch"):
        cleaned["branch"] = "Unknown"
        
    return cleaned


# 4. Process All Records
cleaned_data = [clean_record(r) for r in raw_student_records]

print("\n--- 3. Cleaned Records ---")
for r in cleaned_data:
    print(r)


# 5. Filter Active Students (Score > 0)
active_students = [r for r in cleaned_data if r["score"] > 0]
clean_avg = sum(r["score"] for r in active_students) / len(active_students)

print(f"\n--- 4. Cleaned Valid Average Score ---")
print(f"Average of valid test takers: {clean_avg:.2f}")