# https://www.w3schools.com/python/python_intro.asp

# Single line comment
"""
This is a multi line comment
This is another line
"""
# Key sencetive
#name = 'Patrick'
#NAME = 'Maikel'

# x, y, z = "Patrick", "Maikel", 'Pedro'
# print(x, y, z)

# Indentation

# This is a function
# def add(x, y):
# return x + y

# result = add(500, 5000)
# print(result)

# name = 'Maikel'


# def printName():
# global name
#     name = 'Patrick'
#     print(name)


# printName()
# print(name)

# This is a string DataType
name = 'Patric'

# This is a int = integer DataType
age = 29
print(type(age))

# This is a float DataType
decimal = 14.56
# print(type(decimal))

# This is a dict DataType
person = {
    name: 'Patrick',
    age: 100
}
# print(type(person))

# This a Boolean DataType
# True
# False

# This is a list DataType
name_list = ['String', 26, person]

# This a tuple DataType
book_list = ('book1', 'book2', 26)

# Operators
sum = 5 + 5
# print(sum)
# -
# *
# /
# %

# Assignment Operators
# =
# +=
num = 10
# num = num + 10
# print(num)
num += 10
# print(num)

num1 = 15

# print(num > num1)

# Functions


def printName(name):
    return name


name = printName('Lily')
# print('My username is ', name)

# IF ELIF ELSE Conditions in Python
# if 2 > 5:
#     print('OK')
# elif 2 > 1:
#     print('YES')
# else:
#     print('NO')

# For loop in python
# user_list = ['Rogy', 'Pablo', 'Murien']
# for i in user_list:
# print(i)

# While loop
# num = 1
# while num < 10:
# print(num)
# num += 1

# username = input('Enter your username: ')
# print('My username is:', username)
# print('My username is: ' + username)


def userRegister():
    username = input('Username: ')
    age = input('Age: ')
    job = input('Job: ')
    print('My username is' + username +
          'and Job is ' + job + ' and im ' + age + ' old.')


# userRegister()
def app():
    # options_list = [1,2,3]
    user_option = input('Enter option. Options 1,2,3: ')
    if user_option == '1':
        username = input('What si your username: ')
        print('Good day ' + username)
        app()
    elif user_option == '2':
        print('User option is 2')
        app()
    elif user_option == '3':
        print('User option is 3')
        app()
    elif user_option == 'exit':
        exit()
    else:
        app()


app()
