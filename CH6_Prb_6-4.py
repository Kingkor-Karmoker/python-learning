# code for problem 6.4:
programing_words = {
    'String': "a fundamental data type that represents a sequence of characters ",
    'Int': "Integers data type",
    'Float': "Data types for floating numbers",
    'Append': "Assigning new values at the end of a list",
    'List': "A data structure to store values"
}

for k, v in programing_words.items():
    print(f"word: {k}")
    print(f"Definition: {v}")

# adding 5 more items:
programing_words['tuple'] = "structure data type stores values which cant be mutilated "
programing_words['Set'] = "List of unique values"
programing_words['Dictionary'] = "list of key with values"
programing_words['insert'] = "inserting a value in a list"
programing_words['del'] = "a keyword to delete values in a list"

for k, v in programing_words.items():
    print(f"word: {k}")
    print(f"Definition: {v}")
