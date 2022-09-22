# # print('meow')
# # print('meow')
# # print('meow')

# # catSound = 0

# # while catSound < 5:
# #     catSound += 1
# #     # print('meow')

# # for _ in range(4):
# #     print('woof')

# # print('moo\n' * 3, end='')

# # while True:
# #     n = int(input("What do you want n to be? "))
# #     if n > 0:
# #         break

# # for _ in range(n):
# #     print('Neiigghhhh')


# # def main():
# #     number = get_number()
# #     woof(number)

# # def get_number():
# #     while True:
# #         n = int(input('What is n? '))
# #         if n > 0:
# #             return n
    

# # def woof(n):
# #     for _ in range(n):
# #         print('woof!!')



# # students = ['Harry', 'Ron', 'Hermione', 'Draco']
# # houses = ['Gryffindor', 'Gryffindor', 'Gryffindor', 'Slytherin']

# # hogwarts = {
# #     'Harry': 'Gryffindor', 
# #     'Ron': 'Gryffindor',
# #     'Hermione': 'Gryffindor',
# #     'Draco': 'Slytherin'
# #     }

# # for student in hogwarts:
# #     print(student, hogwarts[student], sep=" ~ House: ")

# students = [
#     {
#         'name': 'Harry',
#         'house': 'Gryffindor',
#         'petronus': 'Stag'
#     },
#     {
#         'name': 'Ron',
#         'house': 'Gryffindor',
#         'petronus': 'Jack Russel Terrier'
#     },
#     {
#         'name': 'Hermione',
#         'house': 'Gryffindor',
#         'petronus': 'Otter'
#     },
#     {
#         'name': 'Draco',
#         'house': 'Slytherin',
#         'petronus': None
#     }

# ]

# for student in students:
#     print(student['name'], student['house'], student['petronus'], sep=', ')


# c = input('CamelCase? ')

# for i in c:                             #iterate through str from input
#     if i.isupper():                     #if the element is uppercase
#         new_c = '_' + i.lower()         #change to lower case and append to _ and store in var
#         i = new_c                       #set i to new var
#     print(i, end="")                    #print new var


# def main():
#     math = str(input('Enter an expresseion for solving: '))
#     print(math)
#     x, y, z = math.split()

#     x = float(x)
#     z = float(z)

#     match 
    
#     # match y:
#     #     case '+':
#     #         print(add(x, z))
#     #     case '-':
#     #         print(subract(x, z))
#     #     case '*':
#     #         print(multiply(x, z))
#     #     case '/':
#     #         print(divide(x, z))

# def add(x, z):
#     return x + z

# def subtract(x, z):
#     return x - z

# def multiply(x, z):
#     return round(x * z, 3)

# def divide(x, z):
#     return round(x / z, 3)

# main()



# main()
#     txt = input('')


# smallest = None
# print("Before:", smallest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#         break
#     print("Loop:", itervar, smallest)
# print("Smallest:", smallest)


# counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
# print(counts.get('kris', 0))


def snake_case():
    text = input('Enter a camelCase phrase: ')

    for i in text:
        if i.isupper():
            new_text = '_' + i.lower()
            i = new_text
        print(i, end='')

snake_case()