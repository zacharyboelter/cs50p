# ~~~~~~~~~~~~~~~~~~~~~~~~~~~  Conditionals ~~~~~~~~~~~~~~~~~~~~~~~~~~~~


x = int(input('Is it a fizzbuzz? Enter a number '))

if x % 3 == 0 and x % 5 == 0:
    print('Fizzbuzz')
elif x % 3 == 0:
    print('Fizz')
elif x % 5 == 0:
    print('Buzz')
else:
    print('Nope')