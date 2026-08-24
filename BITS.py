print('hello')
def factorial(n):
    """return n!using recursion"""
    if n==0:
        return n
    return n*factorial(n-1)
for i in range(9):
    print(f"{i}! =", factorial(i))