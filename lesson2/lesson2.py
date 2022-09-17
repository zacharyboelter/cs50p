# ~~~~~~~~~~~~~~~~~~~~~~~~~~~  Conditionals ~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# x = int(input('Is it a fizzbuzz? Enter a number '))

# if x % 3 == 0 and x % 5 == 0:
#     print('Fizzbuzz')
# elif x % 3 == 0:
#     print('Fizz')
# elif x % 5 == 0:
#     print('Buzz')
# else:
#     print('Nope')


# def main():
#     x = int(input('What is x? '))
#     if is_even(x):
#         print('Even')
#     else:
#         print('Odd')

# def is_even(x):
#     # if x % 2 == 0:
#     #     return True
#     # else:
#     #     return False
    
#     # return True if x % 2 == 0 else False        #refactor 4 lines into 1
#     return x % 2 == 0                             #refactor if else into assumption

# main()



 # ~~~~~~~~~~~~~~~~ Match ~~~~~~~~~~~~~~~~~~
 
# name = input('Whats your name ')

# match name:
#     case 'bob' | 'bill' | 'billy':
#         print('fuck you')
#     case 'jack':
#         print('not fuck you too')
#     case _:
#         print('I love you')


# answer = str(input('What is the Great Answer of Life, the Universe and Everything? '))
# a = answer.replace('-', ' ').lower().strip()

# match a:
#     case '42' | 'forty two':
#         print('Yes')
#     case _:
#         print('No')


# def main():
#     expression = str(input("Enter an Expression of MATHS!!!! "))
#     x, y, z = expression.split()

#     x = float(x)
#     z = float(z)

#     match y:
#         case '+':
#             print(add(x,z))
#         case '-':
#             print(sub(x,z))
#         case '*':
#             print(mult(x,z))
#         case '/':
#             print(div(x,z))
#         case _:
#             print('Ya done fucked it mate.')

# def add(x,z):
#     return x + z
# def sub(x,z):
#     return x - z
# def mult(x,z):
#     return round(x * z, 2)
# def div(x,z):
#     return round(x / z, 3)

# main()


def main():
    time = str(input('What time it is? '))
    hours, minutes = time.split(':')                    #split the string into two strings

    timeToEat = float(convert(hours, minutes))          #set the conversion function to a variable

    



def convert(hours, minutes):
    hours = float(hours)                                #convert to float
    minutes = round(float(minutes) / 60, 2)             #convert minutes to float, divide that by 60 for the hour, round the float to 2nd place
    return float(hours) + float(minutes)                #return the minutes added to hours


if __name__ == "__main__":
    main()
