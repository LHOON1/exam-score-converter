import csv
import math
import sys

PASSING_GRADE = 10  # out of 20

def compute_constant(cutoff):
    s_c = cutoff / 5
    return (s_c - 20) / math.log(PASSING_GRADE / s_c)

def convert(score, constant):
    s = score / 5  # scale to /20
    return round(s * math.exp((s - 20) / constant), 2)

cutoff = float(sys.argv[1]) if len(sys.argv) > 1 else 65
constant = compute_constant(cutoff)
print(f"Cutoff: {cutoff}/100  →  constant C = {constant:.4f}")

with open("score.csv") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    score = int(row["score"])
    grade = convert(score, constant)
    row["grade"] = grade
    row["pass"] = "P" if grade >= PASSING_GRADE else "F"

with open("grades.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["n", "name", "score", "grade", "pass"])
    writer.writeheader()
    writer.writerows(rows)

print(f"{'n':>4}  {'name':<10}  {'score':>5}  {'grade':>5}  pass")
print("-" * 36)
for row in rows:
    print(f"{row['n']:>4}  {row['name']:<10}  {row['score']:>5}  {row['grade']:>5}  {row['pass']}")
print("\nSaved to grades.csv")
