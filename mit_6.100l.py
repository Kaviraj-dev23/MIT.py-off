print(round(7.9))
print(3+2)
print(float((4+2)*6-1))
print(5/3)
print(type(float(123)))
print(int(5.2))
print(round(5.9))
print(int(7.2))
print(round(7.9))
print(float(123))
print(9+8)
print(type(7+4))

#######
# float((4+2)*6-1)
# print((13-4) / (12*12))
# print(5//3)
# print(5%3)
# print(2**6.0)

#####
# a=3
# b=4 
# print(a+b)
# xy = 3+5
# xy = 3 + 5
# print(xy)

###############
# import numpy as np
# import scipy.stats as stats
# a=2
# b=3
# c=4
# total=(a+b)*c
# print(total)

###################
# x = 1 + 2 * 3 - 4 / 2
# print(x)
# a = "me"
# b = "myself"
# c = "memyself" 
# d = a + " " + b
# print(d)
# silly = a * 3
# print(silly)
# b = ":"
# c = ")"
# s1 = b + 2*c
# print(s1)
# f = "a"
# g = " b"
# h = "3"
# s2 = (f+g)*int(h)
# print(s2)
# print(f+g)
# print((int)(h))
# s= 'abc'
# len(s)
# s= 'abc'
# print(s[0])
# print(s[2])
# print(s[-1])
# print(s[len(s)-1])
# print(8**6)

###################
# s= "abcdefgh"
# print(s[2:6])
# print(s[3:5:1])
# print(s[0:len(s):1])
# print(s[::-1])
# print(s[4:1:-2])
# print(s[3:7:2])
# print(s[1:2:3])

#####################
# s= "ABC d3f ghi"
# print(s[3:len(s)-1])
# print(s[2:0])

######################
# a= "we"
# b= 4
# c= "us"
# print(a,b,c)
# print(a + str(b) + c)

##########################
# text =input("type anything: ")
# num1= input("type a number: ")
# print(5*num1)
# num2= int(input("type a number: "))
# print(8*num2)
# k= input("type anything: ")
# print(3*k)
# question= input('choose a verb: ')
# print('i can', question, 'better than you!')
# print((question+' ')*5)

#################################################
# Try Newton Raphson for cube root
# x= int(input('what x to find cube root of?'))
# g= int(input('what guess to start with?'))
# print('current estimate cubed = ', g**3)
# next_g = g - ((g**3 - x)/(3*g**2))
# print('next guess to try = ', next_g)

#####################################################
# print(2>3)
# print(not(4>5))
# print((2<3) and (3>4))
# print((2<3) or (3>4))

# ###################################################
# pset_time = 15
# sleep_time = 8
# print(sleep_time < pset_time)
# derive = True
# drink = False
# both = drink and derive
# print(both)

##################################################
# secret = 2 
# guess =int(input("please guess a number: "))
# equal = (secret == guess)
# print(equal)
# secret= 4
# guess= int(input("make a guess: "))
# secret == guess
# print(secret == guess)

###################################################
# branching example:bool,if,elif,else

# x = int(input("Enter a number for x: "))
# y = int(input("Enter a different number for y: "))
# if x == y:
#     print("x and y are equal")
#     if y != 0:
#         print("Therefore, x/y is", x/y)
# elif x < y:
#     print("x is amaller")
# else:
#     print("y is smaller")
# print('thanks!')

#############################################
#example
# secret= 10
# guess= int(input("guess a num: "))
# if guess > secret:
#     print("too high")
# elif guess == secret:
#     print('equal')
# else:
#     print("too low")

# #############################################
# # While loops example
# ###
# n = 0
# where = input("go left or rght?")
# while where == "right":
#     n = n + 1
#     if n>2:
#         print(":(")
#     where = input("go left or right? ")
# print("you got out!")


# 2nd example#####################################
# n = int(input("enter a non-negative: "))
# while n>0:
#     print('x')
#     n = n-1 #the same as n =-1

# while True:
#     print("noooo")
#     user_input = input("type ' stop' to end: ")
#     if user_input == "stop":
#      break
  
  # Range example#####################################
# for i in range (1,4,1):
#     print(i)
# for j in range (1,3,2):
#     print(j)
# for k in range (4,0,-1):
#     print('$'*k)

# #################################
# mysum = 0
# for i in range(10):
#     mysum += i 
# print(mysum)

# #######example 2 ####
# mysum = 0
# start = 3
# end = 5
# for i in range(start, end+1):
#     print('i=',i)
#     mysum += i
# print(mysum) 
# ###################################
# ###(factorial example )
# x = 4
# i = 1
# factorial = 1
# while i <= x:
#     factorial *= 1
#     i += 1
# print(f' {x} factotial is {factorial}')

###########################
# ===================================================================
# >>> Lecture 4: Loops over Strings, Guess-and-Check, and Binary
# ===================================================================
## break STATEMENT:
# >> in order to exit a loop before the natural end comes,we cann use break statement.
# >> skips remaining expressions in code block and imm exits whatever loop it is in 
# >> exits only innermost loop!
#ex: it doesn't work it's just a example
# while <condition_1>:
#     while <condition_2>:
#         <expression_a>
#         break
#         <expression_b>
#     <expresssion_c>

## example 2:
mysum=0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
        mysum += 1
print(mysum)
#ex 2 try yourself 
even_num = 10
for i in range(5):
    #i is 0,1,2,3,4,5
    if i%2==0:
        even_num += 1
print(even_num)
 ###############
 # ==================================
 # STRINGS AND LOOPS( the sequence of values in a for loop isn't limited to numbers) 
 # ==============================
#example all 3  works 
# 1) 
# s = "demo loops - fruit loops"
# for index in range (len(s)):
#     if s[index] == 'i' or s[index] == 'u':
#        print("there is an i or u")

# for char in s:
#     if char == 'i' or char == 'u':
#         print("there is an i or u")

# for char in s:
#     if char in 'iu':
#         print("there is an i or u") 
#         break

#===========================================
#>>>> IMPLEMENTATION
#===========================================
x= 54
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001
while abs(guess**2 - x) >= epsilon: 
    guess += increment
    num_guesses += 1
print(f'num_guesses = {num_guesses}')
print(f'{guess} is close to square root of {x}')

x = 54
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001
while abs(guess**2 - x) >= epsilon and guess**2 <= x: 
    guess += increment
    num_guesses += 1
print(f'num_guesses = {num_guesses}')
print(f'{guess} is close to square root of {x}')

############## <<<<BISECTION SEARCH>>> ##########
x = 1234
epsilon = 0.01
num_guesses= 0
low = 0 
high = x
guess = (high + low )/2.0
while abs(guess**2 - x  ) >= epsilon:
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print('num_guesses =' ,num_guesses)
print(guess, 'is close to square root of', x)

#x=36
x = 512
epsilon=0.01
low=0
high = x
guess = (low + high) / 2.0

while abs(guess**2-x) >= epsilon:
    num_guesses  += 1
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (low + high )/2.0
print(f'num_guesses =', num_guesses)
print(guess, 'is close to square root of', x)

x = 45
low = 0
epsilon = 0.01
high = x
guess = (low + high )/2.0
while abs(guess**2-x) >=epsilon:
    num_guesses +=1
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (low+high)/2.0
print(f'num_guesses =', num_guesses)
print(guess, 'is close to square root of', x)

#Logarathimic log(N)
x = 0.5
epsilon = 0.01
if x >=1:
    low = 1.0
    high= x
else:
    low = x
    high = 1.0
guess = (low + high)/2.0
while abs(guess**2-x) >=epsilon:
    if guess**2 < x :
        low = guess
    else:
        high = guess
    guess = (high+low)/2.0
print(f'{str(guess)} is close to square root of {str(x)}')

########Example bisection search
cube = 27
epsilon = 0.01
low = 0
high = cube
num_guesses = 0
estimate = (low + high) / 2.0
while abs(estimate**3 - cube) >= epsilon:
    num_guesses += 1
    if estimate**3 < cube:
        low = estimate
    else:
        high = estimate
    estimate = (low+high)/2.0
print(f'num guesses: {num_guesses}')
print(f'{estimate} is close to the cube root of {cube}')

# New Algorithm Newton-Raphon #########
# epsilon = 0.01
# k = 54321
# guess = k/2.0
# # num_guesses= 0
# while abs (guess*guess - k) >= epsilon:
#     num_guesses += 1 
# print(f'num_guesses = {str(num_guesses)}')
# print(f'sq root of {k} is about {guess}')

## lec 7 Functions  ####
# def is_even(i):
#     """ Assumes: i, a positive int returns True if i is even, otherwise 
#     False """
#     if i%2 == 0:
#         return True
#     else:
#         return False
# print(is_even(3))
# print(is_even(14))

# def div_by(n,d):
#     """ n and d are ints > 0
#     returns True if d divides n evenly and False otherwise"""
#     if n%d==0:
#         return True
#     else:
#         return False
# print(div_by(n=10,d=3))
# print(div_by(n=195,d=13))

# def is_even(i):
#     if i % 2 == 0:
#         return True
#     else:
#         return False
# for i in range(1,10):
#     if is_even(i):
#         print(i, 'even')
#     else:
#         print(i,'odd')

####Lecture 8 Functions as Objects########
# def is_even_with_remainder(i):
#     """input i, a positive int returns none"""
#     print('without return')
#     remainder = i%2
#     has_rem = (remainder==0)
#     print(has_rem)
# print(is_even_with_remainder(6))

# def add(x,y):
#     return x+y
# def mult(x,y):
#     print(x*y)
# add(1,2)
# print(add(2,3))
# mult(3,4)
# print(mult(4,5))

# def is_triangular(n):
#     """n is an int>0 returns True if n i triangular, i.e, equals a summation of
#     natural numbers (1+2+3+.....+j), False otherwise """
#     total=0
#     for i in range(n+1):
#         total += i
#         if total == n:
#             return(True)
#     return(False)
# print(is_triangular(6))

def bisection_root(x):
    epsilon=0.01
    low= 0
    high=x
    ans=(low+high)/2.0
    while abs(ans**2-x) >=epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans =(high + low )/2.0
    return ans
print(bisection_root(67)) 

def  count_nums_with_sqrt_close_to(n, epsilon):
    """n is an int > 2
    epsilon is positive number <1 returns how many integers have a square root 
    within epsilon of n"""
    count = 0
    for i in range(n**3): 
        sqrt = bisection_root(i)
        if abs(n-sqrt)< epsilon:
            count += 1 
    return count
print(count_nums_with_sqrt_close_to(9,0.1))
print(count_nums_with_sqrt_close_to(10,1))

#########Variable Scope####
def f(y):
    x=1
    x += 1
    print(x)
x=5
f(x)
print(x)
####ex2####
def f(x):
    x=x+1
    print('in f(x): x=', x)
    return x
x=9
z=f(x)
###lec 8 finger exercise #####
def same_chars(s1,s2):
    """returns booleann True is a character in s1 is also in s2, and vice versa. if a 
    character only exists in one of s1 or s2, returns false"""
    for char in s1:
        if char not in s2:
            return False
    for char in s2:
        if char not in s1:
            return False
    return True
print(same_chars("abc", "cba"))
print(same_chars('abcd',"abdc"))

def f(y):
    x=1
    x += 1
    print(x)
x=5
f(x)
print(x)

def g(y):
    print (x)
    print(x+1)
x=5
g(x)
print(x)

# def h(y):
#     x += 1
# x = 5
# h(x)
# print (x)

# def is_even(n):
#     return n%2==0
# f=3
# result = is_even(f)
# print(result)

def calc (op,x,y):
    return op(x,y)
def add(a,b):
    return a+b
def div(a,b):
    if b != 0:
        return a/b
print('denom was 0.')
res = calc(add,2,3)


### Lec 9 Lambda Functions, Tuples, and Lists #########
def do_twice(n,fn):
    return fn(fn(n))
print(do_twice(3,lambda x: x**2 ))

######### Tuples #########
b = (4,) 
print(type(b))
print(b)
seq = (2,'a',4,(1,2)) #o-2, 1-'a', 2- 4,3-(1,2)
print(len(seq))
print(seq[3])
print(seq[-1])
print(seq[3][0])
# print(seq[4])p # tuple index out of range 
print(seq[1])
print(seq[-2:])
print(seq[1:4:2])
print(seq[:-1])
print(seq[1:3])

for e in seq:
    print(e)

def quotient_and_remainder(x,y):
    q = x//y
    r = x % y
    return(q,r)
both = quotient_and_remainder(10,3)
print("both:", both)
(quot, rem)= quotient_and_remainder(5,2)
print('quotient is:', quot)
print('remainder is:', rem)
##try yourself ###
def char_counts(s):
    """ s is a string of lowercase chars return a tuple where the first 
    element is the number of vowels in s and the second element is the 
     number of consonants in s """
    vowels = 'aeiou' 
    (c, v)=(0, 0)
    for char in s:
        if char in vowels:
            v += 1
    else:
        c +=1
    return (v, c)

print(char_counts('apple'))
print(char_counts('bits'))

def mean(args):
   tot = 0
   for a in args:
       tot += a 
   return tot/len(args)
print(mean((1,2,3,4,5,6)))


    