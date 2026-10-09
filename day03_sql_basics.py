"""
Day 3: SQL Foundations from Scratch using SQLite
Author: Madhan Babu
Topic: CREATE TABLE, INSERT, SELECT, WHERE, ORDER BY, GROUP BY
"""

import sqlite3

# 1. Connect to SQLite database (creates 'college.db' file on disk automatically)
conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# 2. Step 1: Create a Students Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    score REAL,
    branch TEXT,
    city TEXT
)
""")
print("--- 1. Table 'students' created successfully ---")

# 3. Step 2: Insert Real Records into the Database
# Clear table first to avoid duplicate inserts on re-run
cursor.execute("DELETE FROM students")

student_records = [
    (101, "Madhan", 92.0, "AI&DS", "Erode"),
    (102, "Kaviyan", 78.0, "AI&DS", "Coimbatore"),
    (103, "Priyanka", 88.0, "ECE", "Salem"),
    (104, "Abishek", 64.0, "CSE", "Erode"),
    (105, "Niranjani", 95.0, "AI&DS", "Tirupur"),
    (106, "Ramesh", 74.0, "CSE", "Chennai"),
    (107, "Sanjay", 81.0, "AI&DS", "Erode"),
]

cursor.executemany("""
INSERT INTO students (id, name, score, branch, city)
VALUES (?, ?, ?, ?, ?)
""", student_records)

conn.commit()  # Save changes to the database
print(f"--- 2. Inserted {len(student_records)} records into Database ---")


# 4. Step 3: SQL Query 1 - SELECT & WHERE (Filter score >= 80)
print("\n--- Query 1: Top Scorers (score >= 80) ---")
cursor.execute("SELECT id, name, score, branch FROM students WHERE score >= 80")
for row in cursor.fetchall():
    print(row)


# 5. Step 4: SQL Query 2 - ORDER BY (Rank students from highest to lowest score)
print("\n--- Query 2: Leaderboard (ORDER BY score DESC) ---")
cursor.execute("SELECT name, score, branch FROM students ORDER BY score DESC")
for row in cursor.fetchall():
    print(row)


# 6. Step 5: SQL Query 3 - GROUP BY & Aggregation (Counts & Average per Branch)
print("\n--- Query 3: Branch-wise Analytics (GROUP BY branch) ---")
cursor.execute("""
SELECT branch, COUNT(*) AS student_count, ROUND(AVG(score), 2) AS avg_score
FROM students
GROUP BY branch
""")
for row in cursor.fetchall():
    print(f"Branch: {row[0]} | Total: {row[1]} | Average Score: {row[2]}")

# Close connection safely
conn.close()
print("\n--- Database connection closed safely ---")