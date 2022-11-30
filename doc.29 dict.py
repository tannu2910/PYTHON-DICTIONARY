# num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# sorted_dict = {x: sorted(y) for x, y in num.items()}
# print(sorted_dict)



student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
student_dict = {x.translate({32: None}): y for x, y in student_list.items()}
print("New dictionary: ",student_dict)
