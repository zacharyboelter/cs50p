

# def main():
#     # print_wall(4)
#     # print_row(4)
#     print_square(3)
#     square(5)


# def print_wall(height):
#     print('#\n' * height, end="")

# def print_row(width):
#     print('#' * width)

# def square(size):
#     for i in range(size):
#         print_row(size)


# def print_square(size):

#     for i in range(size):           #for each row in square

#         for j in range(size):       #for each brick in row

#             print('#', end="")      #print each brick

#         print()                     #print empty to create new line

# main()




name = input('What is your name? ')

for i in name:
    if i.isupper():
        new_name =  '_' + i.lower()
        i = new_name
    print(i, end="")
    print()