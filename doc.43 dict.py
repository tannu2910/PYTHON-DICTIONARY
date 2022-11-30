def grouping_dictionary(l):
    result = {}
    for key,value in l:
        result.setdefault(key,[]).append(value)
    return result
colors=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print("Grouping a sequence of key-value pairs into a dictionary of lists:")
print(grouping_dictionary(colors))

