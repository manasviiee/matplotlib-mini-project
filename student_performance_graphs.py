"""
Mini Project: Student Performance Dashboard
Topic: Plot different types of graphs using the Matplotlib library
Libraries: NumPy, Matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# 1. Sample data (you can replace with your own marks)
# ------------------------------------------------------------------
subjects = ["Maths", "Python", "DBMS", "AI", "Physics"]
marks = [78, 92, 85, 88, 70]

months = ["Jun", "Jul", "Aug", "Sep", "Oct"]
attendance = [82, 88, 76, 91, 95]

study_hours = np.array([1, 2, 2.5, 3, 4, 4.5, 5, 6, 6.5, 7])
scores = np.array([45, 52, 55, 60, 68, 72, 78, 83, 88, 92])

time_spent = [40, 25, 15, 20]
activities = ["Studying", "Coding", "Sports", "Leisure"]

np.random.seed(1)
exam_scores = np.random.normal(70, 12, 100)  # 100 random student scores

# ------------------------------------------------------------------
# 2. Create dashboard with 6 different graph types
# ------------------------------------------------------------------
fig, axs = plt.subplots(2, 3, figsize=(16, 9))
fig.suptitle("Student Performance Dashboard", fontsize=18, fontweight="bold")

# (a) Bar chart
axs[0, 0].bar(subjects, marks, color="skyblue", edgecolor="black")
axs[0, 0].set_title("Bar Chart - Subject Marks")
axs[0, 0].set_ylabel("Marks")
axs[0, 0].set_ylim(0, 100)

# (b) Line plot
axs[0, 1].plot(months, attendance, marker="o", color="green", linewidth=2)
axs[0, 1].set_title("Line Plot - Monthly Attendance")
axs[0, 1].set_ylabel("Attendance (%)")
axs[0, 1].grid(True, linestyle="--", alpha=0.5)

# (c) Scatter plot with trend line
axs[0, 2].scatter(study_hours, scores, color="red")
m, c = np.polyfit(study_hours, scores, 1)
axs[0, 2].plot(study_hours, m * study_hours + c, color="black", linestyle="--")
axs[0, 2].set_title("Scatter Plot - Study Hours vs Score")
axs[0, 2].set_xlabel("Hours studied per day")
axs[0, 2].set_ylabel("Score")

# (d) Pie chart
axs[1, 0].pie(time_spent, labels=activities, autopct="%1.0f%%", startangle=90)
axs[1, 0].set_title("Pie Chart - Daily Time Spent")

# (e) Histogram
axs[1, 1].hist(exam_scores, bins=10, color="orange", edgecolor="black")
axs[1, 1].set_title("Histogram - Exam Score Distribution")
axs[1, 1].set_xlabel("Score")
axs[1, 1].set_ylabel("Number of students")

# (f) Horizontal bar chart
axs[1, 2].barh(subjects, marks, color="mediumpurple")
axs[1, 2].set_title("Horizontal Bar - Subject Marks")
axs[1, 2].set_xlabel("Marks")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("student_dashboard.png", dpi=150)
plt.show()

# ------------------------------------------------------------------
# 3. Small summary using NumPy
# ------------------------------------------------------------------
print("Average marks :", np.mean(marks))
print("Highest marks :", max(marks), "in", subjects[int(np.argmax(marks))])
print("Lowest marks  :", min(marks), "in", subjects[int(np.argmin(marks))])
