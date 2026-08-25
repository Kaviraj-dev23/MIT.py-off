print('hello')
def factorial(n):
    """return n!using recursion"""
    if n==0:
        return n
    return n*factorial(n-1)
for i in range(8):
    print(f"{i}! =", factorial(i))


menu_items = [12, 25, 8, 15]
total_bill = 0
for price in menu_items:
    total_bill += price
print('total_bill:', total_bill)

def phone_case (func):
    def wrapper():
        print("case snapped on")
        func()
        print("phone is secure")
    return wrapper
@phone_case
def call_friend():
    print('dialing..')
call_friend()
    
def calculate_factorial(n):
    # Step 1: The Emergency Brake
    if n == 1:
        print('done')
        return 1
    else:
        return n *calculate_factorial(n - 1)

print(calculate_factorial(5))






