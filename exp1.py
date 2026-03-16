# A fitness trainer records calories burned by 3 trainees over 3
# workout sessions. Each row represents Trainees and each
# column represents a session. The trainer wants to 1)Convert the
# 3x3 matrix into a single row for uploading 2)Calculate total
# calories per trainee 3)Compute avg calories burned per sess
# 4)Multiply intensity level using dot(.)

import numpy as np

calories=np.array([[220,250,300],[180, 220, 260],[210,240,280]])
print('Calories matrix:')
print(calories)

flat_data=calories.flatten
print("Flattened data:")
print(flat_data)

print("Transpose of matrix:")
print(calories.T)

total_calorie=calories.sum(axis=1)
print('Total calories burned per trainee:')
print(total_calorie)

average=calories.mean()
print("Average calories burned:")
print(average)

intensity=np.array([1.0,1.1,1.2])
weight=calories.dot(intensity)
print("Weightened performance:")
print(weight)