# ==========================================================
# STUDENT DATA ANALYSIS WITH NUMPY(Statistics Mini Project)
# Author: Dikshit Sharma
# ===========================================================

# This project demonstrates:
#- Basic Statistics
#- Spread
#- Outlier Detection
#- Correlation
#- Scaling


import numpy as np 
from scipy import stats

print("===== STUDENT DATA ANALYSIS =====")

# Step 1: Data
marks = np.array([40,50,60,70,80,90,100])
hours = np.array([1,2,3,4,5,6,7])

# --------------------------------------------
# Step 2: Basic Statistics
# --------------------------------------------
print("\n--- Basic Statistics ---")
print("Mean: ", np.mean(marks))
print("Median: ", np.median(marks))
print("Mode: ", stats.mode(marks))

# --------------------------------------------
# Step 3: Spread
# --------------------------------------------
print("\n--- Spread ---")
print("Range: ", np.max(marks) - np.min(marks))
print("Variance: ", np.var(marks))
print("Standard deviation: ", np.std(marks))

# --------------------------------------------
# Step 4: Outlier Detection
# --------------------------------------------
print("\n--- Outlier Detection ---")

Q1 = np.percentile(marks, 25)
Q3 = np.percentile(marks, 75)
IQR = Q3 - Q1
lower = Q1 - (1.5 * IQR)
upper = Q3 + (1.5 * IQR)
outliers = marks[(marks < lower) | (marks > upper)]
print("Outliers: ", outliers)

# --------------------------------------------
# Step 5: Correlation
# --------------------------------------------
print("\n --- Correlation ---")

corr = np.corrcoef(hours, marks)
print("Correlation: ", corr[0][1])

# --------------------------------------------
# Step 6: Scaling
# --------------------------------------------
print("\n --- Scaling ---")

# Z-score
z_score = (marks - np.mean(marks)) / np.std(marks)
print("Z-score: ", z_score)

# Normalization
norm = (marks - np.min(marks)) / (np.max(marks) - (np.min(marks)))
print("Normalization: ", norm)

print("\n===== ANALYSIS COMPLETE =====")
