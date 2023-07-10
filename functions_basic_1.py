#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#output: 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#output: number_of_days_in_a_week_silicon_or_triangle_sides is not defiend

#3
def number_of_books_on_hold():
    return 5 #exits function after this
    return 10
print(number_of_books_on_hold())
#output: 5 

#4
def number_of_fingers():
    return 5 #exits function after this
    print(10)
print(number_of_fingers())
#output: 5 

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#output:
#5
#none

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#output:
#3
#5
#we do not have a return to store to print last 


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#output: 25 (combines strings not math)

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#output:
#100
#10

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#output:
#7
#14
#21 (7 + 14 since these values were stored in function)

#10
def addition(b,c):
    return b+c #exist the function after this
    return 10
print(addition(3,5))
#output: 8

#11
b = 500
print(b) #output: 500
def foobar(): #defining function
    b = 300
    print(b) #output: 300
print(b) #500 
foobar() #envoking the function
print(b) #500 
#output:
# 500
# 500
# 300
# 500


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#output:
# 500
# 500
# 300
# 500


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#output:
# 500
# 500
# 300
# 300


#14
def foo():  #step 1, def function
    print(1) #step 3, output 1
    bar() #step 4, invoking bar function
    print(2) #step 7, print output
def bar(): #step 5, function has been invoked 
    print(3) #step 6, print output
foo() #step 2 invoking function
#output: 
# 1
# 3
# 2


#15
def foo(): #step 1, we have a function
    print(1) #step 3, print as first output
    x = bar() #step 4,  function has been invoked and set as a new variable
    print(x) #step 8, print x which has now been stored as 5 so print 5
    return 10 #step 9, now foo()= 10, so y=10
def bar(): #step 5, function has been called so carry through these lines
    print(3) #step 6, print output
    return 5 #step 7, now bar() = 5 so x=5
y = foo() #step 2, it's invoked and set as a variable
print(y) #step 10, print y which has been assigned as 10 value
#output:
# 1
# 3
# 5
# 10

