import numpy as np
#creating an attendance matrix 
attendance=np.array([ [70, 75, 80],   # Student 1
                     [60, 65, 70],   # Student 2
                     [85, 90, 95]    # Student 3
])
print("Original Attendance Matrix:")
print(attendance)

#Deleting  1 month
attendance=np.delete(attendance, 0, axis=1)
print("After deleting 1st month :")
print(attendance)

#Broadcasting (Add 5% grace)
attendance = attendance+5
print("\nAfter Adding 5% grace attendance:")
print(attendance)


# Slicing:accessing student 2 details
student2=attendance[1, :]
print("\nAttendance of Student 2:")
print(student2)


#reshaping: Converting to Single Row Format
single_row = attendance.reshape(1, -1)
print("\nFinal Single Row Format:")
print(single_row)