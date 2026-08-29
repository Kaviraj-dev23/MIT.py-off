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

# name = input("Enter name: ")
# age = int(input("Enter age: "))
# print("User:", name, "Age next year:", age + 1)
items = ["alpha", "beta", "gamma"]
total_count = len(items)      # 3

for i in range(total_count):  # iterates i = 0, 1, 2
    print(i, items[i])

scores = [88, 42, 95, 61]
total = sum(scores)          # 286
highest = max(scores)        # 95
ordered = sorted(scores)     # [42, 61, 88, 95] (scores remains untouched)




