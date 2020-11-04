# Task 1 - Finding year user was born
import datetime

age = 22
name = 'Matt Sokol'
current_date = datetime.datetime.now()
year_of_birth = current_date.year - 22


print(f"OMG {name}, you are {age} years old so you were born in {year_of_birth}")

# Extension, prompt user for age, name etc. Take into account if the persons birthday
# has already happened this year or not

user_age = int(input("Please input your age. "))
user_name = input("Please input your full name. ")
user_year_of_birth = current_date.year - user_age


birthday = input("Enter your date of birth in the format dd/mm/yyyy. ")
bday = datetime.datetime.strptime(birthday, '%d/%m/%Y')
# user_age_hours = current_date.hour - 15

print(f'Day: {bday.day}')
print(f'Month: {bday.month}')
print(f'Year: {bday.year}')

# This only takes the month into account
if current_date.month > bday.month:
    print("Hope your birthday this year was amazing!! ")
else:
    print("Only a couple of months left until your birthday! ")




# Task - Loops and Lists
# Make a loop using range that says hello 10 times
for i in range(10):
    print("hello")



# Make a loop with a range that asks for names and appends to list_names
# title() was used to capitalise if name given in lower case
list_names = []
while True:
    name = input("Input your name, otherwise type Stop ").title()
    if name == 'Stop':
        break
    list_names.append(name)
print(list_names)



# Make a loop that iterated over each name in the above list_names and format it
# into lowercase in a new variable called list_names_lower
list_names_lower = []
for i in list_names:
    list_names_lower.append(i.lower())
print(list_names_lower)

# Iterate over the list of names to find if the number of letters is even or odd
