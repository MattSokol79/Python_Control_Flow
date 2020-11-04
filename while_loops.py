# While Loops!
# break and continue can be used to control the flow of the loop
# Syntax: while variable_name condition value:
number = 0

while number < 10:
    print(f"It's working -> {number}" )
    if number == 4:
        break
    number += 1

# Take user input and use while loop

user_prompt = True

while user_prompt:
    age = input("Please enter your age")
    # Note: this user input is within our while loop therefore it'll prompt the user
    # until we get desired input
    if age.isdigit() and int(age) < 117:
        # isdigit() checks if the input is all digits
        user_prompt = False
    else:
        print("Please provide age in digits")
print(f"Your age is {age} ")
# Can also use isinstance(variable, data_type) e.g. isinstance(age, int) does the same thing
