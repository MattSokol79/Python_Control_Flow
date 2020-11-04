# Loops for loop and while loop
# for loop is used to iterate through the data 1 by 1 for example
# Syntax for variable name in name_of_data collection_variable

shopping_list = ['eggs', 'milk', 'supermalt']
print(shopping_list)

for item in shopping_list:
    if item == 'milk':
        print(item)

sparta_user_details = {
    'first_name' : 'Charlie',
    'last_name' : 'Shelby',
    'dob' : '22/10/1997',
    'address' : '74 Privet Drive',
    'course' : 'DevOps',
    'grades' : ['A*', 'A', 'A'],
    'hobbies' : ['running', 'reading', 'hunting']
}
# To print keys and values use a for loop
for i, j in sparta_user_details.items():
        if isinstance(j, list):
            print(f"Key: {i}")
            for k in j:
                print(f"List Value: {k}")
        else:
            print(f"Key: {i}, Value: {j}")

