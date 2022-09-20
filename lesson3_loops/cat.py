# print('meow')
# print('meow')
# print('meow')

# catSound = 0

# while catSound < 5:
#     catSound += 1
#     # print('meow')

# for _ in range(4):
#     print('woof')

# print('moo\n' * 3, end='')

# while True:
#     n = int(input("What do you want n to be? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print('Neiigghhhh')


# def main():
#     number = get_number()
#     woof(number)

# def get_number():
#     while True:
#         n = int(input('What is n? '))
#         if n > 0:
#             return n
    

# def woof(n):
#     for _ in range(n):
#         print('woof!!')



# students = ['Harry', 'Ron', 'Hermione', 'Draco']
# houses = ['Gryffindor', 'Gryffindor', 'Gryffindor', 'Slytherin']

# hogwarts = {
#     'Harry': 'Gryffindor', 
#     'Ron': 'Gryffindor',
#     'Hermione': 'Gryffindor',
#     'Draco': 'Slytherin'
#     }

# for student in hogwarts:
#     print(student, hogwarts[student], sep=" ~ House: ")

students = [
    {
        'name': 'Harry',
        'house': 'Gryffindor',
        'petronus': 'Stag'
    },
    {
        'name': 'Ron',
        'house': 'Gryffindor',
        'petronus': 'Jack Russel Terrier'
    },
    {
        'name': 'Hermione',
        'house': 'Gryffindor',
        'petronus': 'Otter'
    },
    {
        'name': 'Draco',
        'house': 'Slytherin',
        'petronus': None
    }

]

for student in students:
    print(student['name'], student['house'], student['petronus'], sep=', ')