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

# #### Lists & Mutability #####
# L = [1,2,3]
# L[2] = 5
# print(L)

L = [2,1,3]
L.append(5)
L= L.append(5)
print(L)
#  #TRY yourself## what's the value of L1,L2,L3
L1=['re']
L2=['mi']
L3=['do']
L4= L1 + L2 ## [re, mi]#
L3.append(L4)
L=L1.append(L3) 
print(L)

def make_ordered_list(n):
    """n is a positive int returns a list containing all line in 
    order from o to n (inclusive)"""
    mylist =[]
    for i in range(0,n+1):
        mylist.append(i)
    return mylist
print(make_ordered_list(2))

def remove_elem(L, e):
    """L is a list e is object returns a new list with elements in the same order as 
    L but without any elements equal to 3."""
    newlist =[]
    for i in L:
        # i is 1 then 2 then 2 then 2
        if i != e:
            newlist.append(i)
    return newlist
L= [1,2,2,2]
print(remove_elem(L, 2))
L=[1,2,2,2]
print(remove_elem(L, 1))
L= [1,2,2,2]
print(remove_elem(L, 0))

def count_words(sen):
    """sen is a string representing a sentence returns how many 
    words are in s(i.e, a word is a sequence of characters between spaces.)"""
    L1 = sen.split(' ')
    return len(L1)
s = "hello it's me"
print(count_words(s))
s = '123   45'
print(count_words(s))

# L = [1, 3, 4]
# L = L.sort()
# print(L)

def sort_words(sen):
    """sen is a string reprsenting a sentence returns a 
    list containing all the 
    words in sen but aorted in alphabetical order."""
    L = sen.split(' ')
    # L.sort()
    # return L
    return sorted(L)   ### other way to get that###
s = "hey this is Kavi"
print(sort_words(s))

range(4)
range(2,9,2)
L= [1,2,3,4]
for i in range (len(L)):
    L.append(i)
    print(L)
### another way ##
# L = [1,2,3,4]
# i  = 0
# for e in L:
        #### never stop it do loop until we stop##
#     L.append(i)
#     i += 1
#     print(L)
#Combining Lists##
L1= [2,1,3]
L2=[4,5,6]
L3= L1+ L2
print(L3)
L1.extend([0,6])
print(L1)
L2.extend([[1,2],[3,4]])
print(L2)
##Combining##
L = [1,2,3,4]
for e in L:
    L = L+ L
    print(L)
L = [1,4,5]
print(id(L))
L.append(8)
print(id(L))
L.clear()
print(L)
print(id(L))
###Lec 11- Aliasing and Cloning##
def remove_all(L, e):
    """L is a list 
    mutates L to remove all elements in L that are equal to e returns
    none. """
    Lnew = L[:]
    L.clear()
    for n in Lnew:
        if e != n:
            L.append(e)
Lin =[1,2,2,2]
remove_all(Lin, 2)
print(Lin)
def remove_all (L, e):
    """L is a list mutates L to remove all elements in L that are equals
     to e returns none. """
    for elem in L[:]:
        if elem == e:
            L.remove(e)
Lin = [1,2,2,2]
remove_all(Lin, 2)
print(Lin)
def remove_dups (L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        L1.remove(e)
L1 = [10,20,30,40]
L2 = [10,20,50,60]
remove_dups(L1, L2)
print(L1)
### Lec 12 Comprehensions, Functions as Objects, Testing and Debugging ###
def f(expr,old_list, test = lambda x: True):
    new_list = []
    for e in old_list:
        if test(e):
            new_list.append(expr(e))
    return new_list
[e**2 for e in range((6))]
print([e**2 for e in range(6)])
print([e**2 for e in range(8) if e%2 == 0])
print([[e,e**2] for e in range(4) if e%2 != 0])
## epsilon as parameter ##
# def bisection_root_new(x, epsilon): ## epsilon as default parameter##
def bisection_root_new(x, epsilon=0.01): ## epsilon as keyword parameter##
    num_guesses = 0
    low = 0
    high = x
    guess = (high + low)/2.0
    while abs(guess**2- x)>=epsilon:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (high+ low)/2.0
        num_guesses += 1
    print('num_guesses =', num_guesses)
    return guess
print(bisection_root_new(56, 0.01))
print(bisection_root_new(90, 1))
## debugging##
def is_pal(x):
    """returns True is list x is a palindrome and False otherwise """
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False
print(is_pal(list('abcba')))
print(is_pal(list('ab')))
##added print debug###
def is_pal(x):
    """returns True is list x is a palindrome and False otherwise """
    temp = x
    temp.reverse
    print(temp, x)
    if temp == x:
        return True
    else:
        return False
print(is_pal(list('ab')))
##another print###
def is_pal(x):
    """returns True is list x is a palindrome and False otherwise """
    temp = x[:] ### copy method##
    # temp = x
    print('before reverse', temp, x)
    # temp.reverse
    temp.reverse()  ###added () for getting 'b' 'a'
    print('after reverse', temp, x)
    if temp == x:
        return True ## after reverse should be 'b''a'
    else:
        return False
print(is_pal(list('abcba')))
### Lec 13 Exceptions and Assertions ###
def sum_digits(s):
    """"S is  non-empty string containing digits returns sum of all 
    characters that are digits"""
    total = 0
    for char in s:
        if char in '0123456789':
            val = int(char)
            total += val
    return total
print(sum_digits('123'))
print(sum_digits('123abc'))
## same code with Exceptions ##
def sum_digits(s):
    """"S is  non-empty string containing digits returns sum of all 
    characters that are digits"""
    total = 0
    for char in s:
        try:
            val = int(char)
            total += val
        except:
            print("couldn't print chracter", chr)
    return total
print(sum_digits('123abc'))

# def divide_nums1():
#     # a = int(input("tell me one number: "))
#     # b = int(input("tell me another number: " ))
#     print(a/b)
# divide_nums1()

# def divide_nums2():
#     try:
#         a = int(input("tell me one number: "))
#         b = int(input("tell me another number: "))
#         print(a/b)
#     except:
#         print('bug in user input')
# divide_nums2()
# def divide_nums3():
#     try:
#         a = int(input('tell me one number: '))
#         b = int(input('tell me another number: '))
#         print('a/b = ', a/b)
#         print('a+b = ', a+b)
#     except ValueError:
#         print("could not convert to a number. ")
#     except ZeroDivisionError:
#         print("can't divide by zero")
#         print("a/b = infinty")
#         print("a+b =", a+b)
#     except:
#         print("something went wrong.")
#     else:
#         print('success') ### we can add else inside an it will follow except# 
# divide_nums3()

## you try it ## lec 13 
def pairwise_div(Lnum, Ldenom):
     """Lnum and Ldenom are non-empty lists of equal lengths containing numbers
         Returns a new list whose elements are the pairwise 
          division of an element in Lnum by an element in Ldenom. 
            Raise a ValueError if Ldenom contains 0. """
     L = []
                #  L = [Lnum[i]/Ldenom[i] for in  range (len(Lnum))]  
        ## other way##
     if 0 in Ldenom:
         raise ValueError
     for i in range(len(Lnum)):
         ## i is 0,,1,2,3.....
        try:
             L.append(Lnum[i]/Ldenom[i])
        except:
            raise ValueError('nice message')
     return L
L1 = [4,5,6]
L2= [1,2,3]
print(pairwise_div(L1, L2))
## Assertion #### example 
def pairwise_div(Lnum, Ldenom):
    """ Lnum and Ldenom are non-empty lists of equal lengths
        containing numbers
    Returns a new list whose elements are the pairwise 
    division of an element in Lnum by an element in Ldenom. 
    Raise a ValueError if Ldenom contains 0. """
    assert len(Lnum) == len(Ldenom), 'lengths diff'## EQUAL ##
    assert len(Lnum) !=0 and len(Ldenom)!=0, 'empty list'## 
                            # NON EMPTY # len(a) ==len(b) len(a)  > 0
    L=[]
    for i in range (len(Lnum)):
        try:
            L.append(Lnum[i]/(Ldenom[i]))
        except: 
            raise ValueError('nice mesage')
    return L
L1 = [1,2,3]
L2=[4,5,6]
print(pairwise_div(L1, L2))
                     # Lec 14: Dictionaries##
def find_grades(grades, students):
    """grades is a dict mapping student names (str) to grades(str) students is 
    a list of student nmes returns a list containing the
      grades for students (in same order)"""
    Lnew= []
    for elem in students:
        grade = grades[elem]
        Lnew.append(grade)
    return Lnew
d = {'ana' : 'B', 'matt' : 'C', 'john': 'B', 'katy' : 'A'}
print(find_grades(d, ['matt', 'katy']))

def find_in_L(Ld, k):
    """ Ld is a list of dicts
    k is an int
    Returns True if k is a key in any dicts of Ld and False otherwise """
    for d in Ld:
        # d is k1, v1
        if k in d:
            return True
    return False
d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3 = {1:1, 3:9, 4:16, 5:25}
print(find_in_L([d1, d2, d3], 2))  # returns True
print(find_in_L([d1, d2, d3], 25))  # returns False

def count_matches(d):
    """d is a dict
    returns how many entries in d hve the key equal to its value """
    # count = 0
    # for v,k in d.items():
    #     if v==k:
    #         count = count +1
    # return count
                        ### other way ##
    count = 0
    for x in d.keys():
        if d[x]==x:
            count += 1   
    return count  
d = {1:2, 3:4, 5:6}
print(count_matches(d))   
d = {1:2, 'a':'a', 5:5}
print(count_matches(d))

my_d ={'Ana':{'mq':[10], 'ps':[10,10]}, 
       'Bob':{'ps':[7,8], 'mq':[8]},
       'Eric':{'mq':[3], 'ps':[0]}  }
def get_average(data, what):
    all_data = []
    for stud in data.keys():
        all_data = all_data + data[stud][what]

    return sum(all_data)/len(all_data)
# all_data = all_data + data[stud][what]
# all_data.append(data[stud][what])
# all_data = all_data + data[stud[what]]
# all_data.append(data[stud[what]])
print(get_average(my_d, 'mq'))  # Output: 7.0  -> (10 + 8 + 3) / 3
print(get_average(my_d, 'ps'))