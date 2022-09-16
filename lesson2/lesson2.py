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


def main():
    x = int(input('What is x? '))
    if is_even(x):
        print('Even')
    else:
        print('Odd')

def is_even(x):
    # if x % 2 == 0:
    #     return True
    # else:
    #     return False
    
    # return True if x % 2 == 0 else False        #refactor 4 lines into 1
    return x % 2 == 0                             #refactor if else into assumption

main()