student_dict = {
    'student': ['Angela', 'James', 'Lilly'],
    'score': [56, 76, 98]
}

# Looping through dictionaries
#for (key, value) in student_dict.items():
    #print(value)

# Another ways through pandas
import pandas
student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)

# Loop through a data frame
#for (key, value) in student_data_frame.item():
    #print(value)

#or
for (index, row) in student_data_frame.iterrows():
    if row.student == 'Angela':
        print(row.score)
