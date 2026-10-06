"""
Day 1: Python Foundations for Data & AI Engineering
Author: Madhan Babu
Topic: Data Structures, List Comprehension, and Aggregation
"""

# 1. Real-World Dataset Simulation (List of Dictionaries)
students_data = [
    {"id": 101, "name": "Madhan", "score": 92, "branch": "AI&DS"},
    {"id": 102, "name": "Kaviyan", "score": 78, "branch": "AI&DS"},
    {"id": 103, "name": "Priyanka", "score": 85, "branch": "ECE"},
    {"id": 104, "name": "Abishek", "score": 64, "branch": "CSE"},
    {"id": 105, "name": "Niranjani", "score": 95, "branch": "AI&DS"},
    {"id": 106, "name": "Ramesh", "score": 66, "branch": "CSE"},
]

print("--- 1. Raw Data ---")
for student in students_data:
    print(student)

# 2. List Comprehension:Filter students scoring below 75
# This is how we filter rows in Data Science without writing 5-line for-loops
need_improvement = [s["name"] for s in students_data if s["score"] < 75]
print("\n--- 2. Low Scorers (Score < 75) ---")
print(need_improvement)

# 3. Custom Function with Type Hints to Calculate Average Score
def calculate_average(data: list[dict]) -> float:
    """Calculates the average score of all students."""
    total_score = sum(student["score"] for student in data)
    return total_score / len(data)

avg_score = calculate_average(students_data)
print(f"\n--- 3. Class Average Score ---")
print(f"Average: {avg_score:.2f}")

# 4. Data Aggregation: Count students per branch (Foundation for SQL GROUP BY)
branch_counts = {}
for student in students_data:
    branch = student["branch"]
    branch_counts[branch] = branch_counts.get(branch, 0) + 1

print("\n--- 4. Student Count Per Branch ---")
print(branch_counts)