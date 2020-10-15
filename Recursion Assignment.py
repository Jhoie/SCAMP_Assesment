# code for fibonnaci  sequence
def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)


try:
    num_terms = int(input("Enter any number: "))

    if num_terms <= 0:
        print("Please enter any digit greater than 0")
    else:
        print("Fibonacci sequence:")
        for i in range(num_terms):
            result = fib(i)
            print(result)

except ValueError:
    print("Enter any digit greater than 0")