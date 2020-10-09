#------------Simple Funtion Example 1-------------------
# def function(n):
#     print(n)

# function(50)

#----------------Simple Function Example 2-----------------------
# def main():
#     kitten()

# def kitten():
#     print('Meow')

# if __name__ == "__main__":
#     main()

#-------------------Funtion Arguments--------------
def main():
    x = [5]
    y = x
    y[0] = 3
    print(id(x))
    print(id(y))
    print(x)
    print(y)
    # kitten(x)
    # print(f'in main: x is {x}')

def kitten(a):
    print(id(a))
    a=3
    print(id(a))
    print('Meow')
    print(a)

if __name__ == "__main__":
    main()

#----------------Prime/Not Prime-----------------

# def isprime(n):
#     if n <= 1:
#         return False
#     for x in range(2, n):
#         if n % x == 0:
#             return False
#     else:
#         return True

# n = 5
# if isprime(n):
#     print(f'{n} is prime')
# else:
#     print(f'{n} not prime')