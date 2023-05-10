# Question 1#
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.#
#def hello_name(user_name):#

def hello_name(user_name):
    print("Hello_" + user_name + "!")
hello_name("John")


#Question 2#
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing#
#def first_odds():#

def first_odds():
    for num in range(1, 101, 2):
        print(num)
first_odds()


#Question 3#
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.#
def max_num_in_list(a_list):
    max_num = a_list[0]
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num
my_list = [3, 8, 2, 10, 5]
max_num = max_num_in_list(my_list)
print(max_num)  


#Question 4#
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).#
#def is_leap_year(a_year):#

def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(is_leap_year(2020))  
print(is_leap_year(2000))  
print(is_leap_year(1900)) 
print(is_leap_year(2022))

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
# def is_consecutive(a_list):

def is_consecutive(a_list):
    sorted_list = sorted(a_list)
    for i in range(1, len(sorted_list)):
        if sorted_list[i] != sorted_list[i-1] + 1:
            return False
    return True
print(is_consecutive([2, 3, 4, 5, 6, 7]))  
print(is_consecutive([1, 2, 4, 5])) 
print(is_consecutive([10, 11, 12, 13, 14, 15, 16])) 
print(is_consecutive([-3, -2, -1, 0, 1]))
