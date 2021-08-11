#print("hello")
                                #to print index
language = "nikhil"
print (language[5])
                                  #to string silcing 

#lang = "Nikhil"
#syntax= (starting argument : ending argument-1)
#print("lang"[0:3]) 
                       #to step_argument

#print("lang"[0:3:2])  
                      #  enter your name by help of users and print in reverse order                                   

#name =input("enter your name ")
#print (f"your name is{name[-1::-1]}")

name = "nikhil kumar"
#print (len(name))           # to cout the length
#print (name.lower())           # to arrange in small leter
#print (name.upper())           # to arrange in big alphate 
#print (name.title())       # to arrange in title manaer  
#print (name.count("i"))     # to count any letter in a word.

                    # enter two input by the help of usear
#name, char = input("enter your name and char").split(",")
#print (f"length your name is {len(name)}")
#print (f"character count : {name.lower().count(char.lower())}") 

                             # to count length and of and single letter if any space given by any usear. 
#name, char = input("enter your name and char").split(",")
#print (f"length your name is {len(name)}")
#print (f"character count : {name.strip().lower().count(char.strip().lower())}")

                  # to replace any word or space in any line
#string = "my name is nikhil kumar and he is good boy"
#print (string.replace(" ","_") )
#print( string.replace("is","are"))
#is_pos1 = string.find("is")
#is_pos2 = string.find("is",is_pos1+1)
#print(is_pos2)

           # to add star in left or right.
#name = input("enter your name")
#print (name.center(len(name)+4,"*"))

          #Strings are Immutable in python, string can't be changed.

          # question if and else condition.
#age =int(input("enter your age "))
#if age >=14:
    #print("your age is above 14")          

                              # assigment question for if and else statement this is also known as nested statement.
#winning_no=27
#user_input=int(input("enter a no between 1 to 100"))
#if user_input==winning_no:
#    print("you win!!")
#else:
 #       if user_input < winning_no:
  #          print("it is to low!!")
   #     else:
    #            print("it is to High!!")

                                     # to use if and elif statement.
#age= int(input("enter your age: ")) 
#if age==0 or age <0:
 #   print("you can't watch this movies")
#elif 0<age<=3:
 #       print("the ticket is free")
#elif 4<age<=10:
 #           print("the ticket price is 150")
#elif 11<age<=60:
  #              print("the ticket price is 200")

                                                # to check this string is empty.  
#name=""
#if name:
 #   print("this is not empty")
#else:
 #       print("this is empty")

                            # using while loop.
#i=1
#while i <=10:
 #   print (f"hello world{i} ")
#    i=i+1

                                  # sum of first ten no.
#total=0
#i=1
#while i<=10:
  #  total += i
 #   i= i+1
#    print(total)

                             # summ of numer what ever you want enter by the help of usear.
#number=  (input("enter a no"))
#total=0
#i=0
#while i< len(number):
  #   total +=int(number[i])
 #    i= i+1
#     print(total)

                                              #enter a name it will count.
#name=input("enter a name")
#temp_var = " "
#i=0
#while i<len(name):
  #if name[i] not in temp_var:
   # temp_var += name[i]
  #print(f"{name[i]}:{name.count(name[i])}")
 # i+=1
 
                                       # sum of first  nine no using for loop.
#total=0
#for i in range(1,10):
 #  total+=i
#   print(total)

#num=(input("enter a no "))
# total=0
#for i in range(0,len(num)):
 # total +=int(num[i])
#  print(total)

                            # using of break and continue statement
#for i in range(1,10):
 #if i==5:
  #continue# break

 #print(i)


                       # code of small game using while loop.
#winning_no =43 
#guess=1 
#number=int(input("enter a n0 between 1 to 100: "))
#game_over=False
#while not game_over:
  #if number == winning_no:
    #print(f"you,win and guessed this numberin {guess} times")
   # game_over=True
  #else:
      #if number<winning_no:
      #  print("to low")
     #   guess+=1
    #    number=int(input("guess a number"))
   #   else :
  #      print("to high")
 #       guess+=1
#        number=input("guess a number")

#name =input("enter a name")
#for i in range (len(name)):
 # print( name[i])

                                   # sum of no using for loop.
#number=input("enter a number: ")
#total=0
#for i in number:
  #total+=int(i)
 # print(total)

                                     # to define function we use def .
#def add_num(a,b):
 #return a+b
#num_1=int(input("enter a first number: "))
#num_2=int(input("enter a second number: "))
#total=add_num (num_1,num_2)
#print(total)             

#def odd_even(num):
  #if num%2==0:
  #  return "even" 
 # else:
 #     return "odd"
#print(odd_even(10))


                    # to check whether it palindrome or not.
##def in_palindrom(word):
  #if word==word[::-1]:
   # return True
  #else :
   #   return False
#print(in_palindrom('naman'))
#print(in_palindrom('mohan'))  

                                        #to check whether it is fibonacci_seq are not.
#def fibonacci_seq(n):
  #a=0
  #b=1
  #if n==1:
   # print(a)
  #elif n==2:
    #print(a,b)
  ##else:
    #print(a,b,end=" ")
    #for i in range(n-2):
    #  c=a+b
   #   a=b
  #    b=c
 #     print(b,end=" " )  
#fibonacci_seq(10)      

                                  # to make list we use this kind of codeing by the help of append we can add the fruits how ever we want .
                                  #the first store name will be written in first and last will bbe written at last.
#fruits=[]
#fruits.append("mango")
#fruits.append("apple")
#fruits.append ("water-malena")
#print(fruits)


                                            # compare between is and equal.
#fruits1 =["apple","mango","licha","papaya","banana","kiwi"]
#fruits2 =["apple","mango","licha","papaya","banana","kiwi"]
#fruits3 =["apple","mango","licha","papaya"]
#print(fruits1 == fruits2)       # == it will check whether its is equal or not.
#print(fruits2 is fruits3)  # is will check whether fruits 1 and fruits 3 are in same memory or not.

                                  # list inside list.
#matrix=[[1,2,3],[7,4,3],[3,4,5]]
#print(matrix[2])
#for sublist in matrix:
 # for i in sublist:
 #   print(i)
#print(matrix[2][0]) 
#print(type(matrix))   


#number= list (range(1,11))
#number=[1,2,3,4,5,6,7,8,9,10]
#print(number)
#print(number.pop(2))
#print(number)
#def negative_list(l):
  #negative=[]
  #for i in l:
  #  negative.append(-i)
 # return negative
#
 #print(negative_list(number))


#def square_list(l):
  #square=[]
  #for i in l:
  #  square.append(i**3)
 #   return square

#numbers=[3,4,6]
#print(square_list(numbers))    

                            # reverse of number.#     
#def reverse_list(l):
 # return l[::-1]
#numbers=[1,2,3,4]
#print(reverse_list(numbers))

#def reverse_list(l):
  #r_list=[]
  #for i in range (len(l)):
   # popped_item=l.pop()
  #  r_list.append(popped_item)
 #   return r_list
#number=[1,2,3,4,5]
#print(reverse_list(number)) 

                                               # introduction of tuple.
 #tuple is data structre.
 #tuple can store any date type.
 #most important that tuple are Immutable, one tuple is created you can't update.
 #date inside tuple.
#example=("one","two","three")
 #no pop, no insert, no remove ,no append. when we craete a tuple we can't update .
 # tuple are faster than a list.
 # we can use count,index,len(fun),slicing
#print(example[:3])

#num=(1,2,3,4)
#print(type(num))
# tuple without`parameter.
#name= 'nikhil','neha','mohan','ram'
#print(type(name))
#tuple unpacking.
#name= ('nikhil','neha','mohan','ram')
#name1,name2,name3,name4=(name)
#print(name3)
#list inside tuple.
#color=('red','blue',['green','orange','yellow'])
#color[2].pop()
#color[2].append("pink")
#print(color)
#numbers = (4,5,6,7,8,9)
#print(min(numbers))
#print(max(numbers))
#print(sum(numbers))
#print(type(numbers))

                                                #fuction returing 
#def fun(int1,int2):
 # add=int1+int2
  #multiply=int1*int2
  #return add,multiply
#add,multiply=fun(4,5)
#print(add)
#print(multiply)

#num=tuple (range(1,7))
#print(num)
#number= list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
#print(number)
#no= str((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
#print(no)
#print(type(no))

                                  # dictionaries= unordered collection of date in key.
             # to create dictinaries :-
#user={'name' : 'nikhil', 'age':24}
#print(user) 
#print(type(user))
                   #second method to craete a dictinaries. 
#user1 =dict(name="Nikhil", age=20)
#print(user1)        
#print(user['name'])
                           # we can store :- number,list,dictionaries,string.
# how to add data to empty dictionary.
#user_info2={}
#user_info2["name"]="Nikhil"
#user_info2["age"] =19
#print(user_info2) 
                           

                           # using looping concepet.
#user_info1={
 # 'name':'Nikhil',
  #'age':24,
  #'movies':'kgf chapter',
  #'game':"cricket"
#}    
#for i,j in user_info1.items():
  #print(f"keys is {i} and value is {j}")   
#user_info1['fav songs']=["song1","song2"]
#print(user_info1)   
#popped_item=user_info1.pop('game')
#print(f"popped_item is {popped_item} ")
#more_info={"state": "Bihar","Hobbies":["playing games"]} # to update any dictionaries.we can create new dict and update theam and print it.
#user_info1.update(more_info)
#print(user_info1)

                                            # fromkeys
#d=dict.fromkeys(["name","age"],'unknown')  
#print(d)                                          
                                              #getkeys.
#d={"name":"Nikhil","age":'20'}
#print(d["age"])
#print(d.get('names'))           # it is better than above print condition.

#d.clear
#print(d)
#d1=d
#print(d1.popitem())
#print(d)

                # more about getkeys.
"""more about get,two same keys in dictionaries.
d={"name":"Nikhil","age":'20'}
print(d.get('names','not present in a list'))

def cube_finder(n):
  cubes = {}
  for i in range(1,n+1):
    cubes[i]= i**3
  return cubes
print(cube_finder(10))

 user={}
name=input("enter your namr: ")
age=input("enter your age: ")
film=input("enter your faviourit movies").split(",")
user['name']=name
user['age']=age
user['film']=film
print(user)
for key,value in user.items():
 print(f"{key}:{value}") """

              # set 
"""s={1,2,3,4,5,6,6,7,6,7}
print(s)
print(list(s))
d=[1,2,3,4,5,6,7,8,6,6,7]
print(set(d))
print(d) """
                   # to check for union and intersection
""" s1={1,2,4,5,3,2}
s2={1,4,2,5}
set_union=s1|s2
set_intersection=s1&s2
print(set_union)
print(set_intersection) """

       #     compreshension
""" square=[]
for i in range(1,11):
  square.append(i**2)
#print(square)
square[i**2 in range (1,11)] # compreshension
print(square)   """  

""" def reverse_list(l):
  return[name[::-1]for name in l]
print(reverse_list(["nikhil","kumar"])) """
                      
                      # for even no we use this type of compreshension.
""" even_num1=[i for i in range(1,11) if i%2==0]     
print(even_num1) """

""" def num_to_string(l):
  return[str(i) for i in l if(type(i)==int or type(i)==float or type(i)==list or type(i)==bool)]
print(num_to_string([True,False,[1,2,3],1,3,2.0])) """

""" num_list2=[i*2 if(i%2==0) else(-i) for i in range(1,11)]
print(num_list2) """ """
                       # to print list in a single list.
""" """ nested_list=[[i  for i in range(1,4) ]for j in range(3) ]
print(nested_list) """


                  # to sqaure number in range 1 to 10.
""" square={f"square of num":num**2 for num in range(1,11)}
for k,v in square.items():
  print(f"{k}:{v}")

string="Nikhil"
word_count={char:string.count(char)for char in string}
print(word_count) """


# *args, *operator
""" def total(a,b):
  return a+b
def all_total(*args):
  total=0
  for num in args:
    total +=num
  return total
print(all_total(1,2,3,4,5,6,7))       """

""" def multiply_num(*args):
  
  multiply=1
  #print(args)
  for i in args:
    multiply *= i
  return multiply
nums=[1,2,3,4]
print(multiply_num(*nums)) # unblock a list we use * operator.   """ 

""" def to_power(num,*args):
  if args:
    return [i**num for i in args]
  else:
    return "there is no args"
num=[1,2,3]
print(to_power(3,*num))     """


           # ** kwargs
""" def fun(**kwargs):
  for k,v in kwargs.items():
    print(f"{k}:{v}")
  
d={'name': 'nikhil','game':'cricket'}
fun(**d)
#fun(first_name="Nikhil",last_name="kumar")  """            

  # PADK
  #parameter 
  # args
  # default parameters
  #kwargs

""" def func(name, *args, last_name= "unknwon", **kwargs):
  print(name)
  print(args)
  print(last_name)
  print(kwargs)
func('harshit',1,2,3, a=1, b=2)  """ 


        # reverse of strning using kwarge
""" def func(l,**kwarge):
  if kwarge.get("reverse_str")==True:
    return [name[::-1]for name in l]
  else:
    return [name for name in l]
name= ["harsit","mohit"]
print(func(name, reverse_str=True))  """     

# lambda expression.
""" def is_even(a):
  return a%2==0
print(is_even(3))

is_even2= lambda a: a%2==0
print(is_even2(4)) """

""" def func(s):
  return len(s)>5

func= lambda s: len(s)>5
print(func("rohan")) """

            # enumerate function.
"""  name=["abc","xyz","rachit"]            
 pos=0
for name in name:
  print(f"{pos}----->>{name}")
  pos+=1     

  # using EF
 for pos,name in enumerate(name):
  print(f"{pos}--->{name}")      

 # to find position of string .
 def position_finder(l,target):
   for pos ,name in enumerate(l):
     if name == target:
       return pos
   else :
         return -1
print(position_finder(name,"xyz")) """

                                # map function
""" number =[1,3,4,5] 
square= list(map(lambda a:a**2,number))
print(square)                               

squares =[i**2 for i in number]
print(squares)

name=["abcv","xysdf","vgftyhgg"]
length= list(map(len,name))
print(length)
for i in length:
  print(i)
for j in length:
  print(j)  """

  # filter function
""" def is_even (a):
  return a%2==0
number=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda a: a%2==0,number))
print(evens)   

new_evens=[i for i in number if i%2==0]
print(new_evens) """

                      # zip function
""" user_id= ["user1","user2","user3"]
name=["nikhil","mohit","ram","sita"]
print(list(zip(user_id,name)) )    
print(dict(zip(name,user_id)) )   """        

""" l=[(1,2),(2,3),(3,4),(5,4)]
new_list=[]
# * operator with zip
l1,l2= list(zip(*l))
print(list(l1))
print(list(l2))
for pair in zip (l1,l2):
  new_list.append(max(pair))
print(new_list)  """ 

# any or all function:                              # any : it check condition if any one satisfied than it will return true.
""" number1=[1,2,4,6,8,9]                                # all : it check condition if any one not satisfied than it will return false.
number2=[1,2,3,4,5,6,7,8,9]
print(any([num%2==0 for num in number1]))
print(all([num%2==0 for num in number1])) """

# min() and max() function

""" name=["nikhil","mohit","ram","sita"]
print(max(name,key=lambda item: len(item))) """

# sorted 
""" guitars=[
  {"model":"yamha765","price":84000},
  {"model":"faith naptune","price": 50000},
  {"model":"taylor 814ce","price":65000}
]
print(sorted(guitars,key=lambda d:d["price"])) """

# doc function":
""" def add(a,b):
  '''add of two number '''
  return a+b
print(add.__doc__)
print(add(2,3)) """

# function as argument:
""" def my_map2(func,l):
  return[func(item) for item in l]
print(my_map2)  
l=[1,2,3,4]
print(list(my_map2(lambda a: a**3,l))) """

# function returning function (closuer) particles :
""" def to_power(x):
  def calc_power(n):
    return n**x
  return calc_power
cube=to_power(3)
print(cube(2))  

square=to_power(2)
print(square(8)) """

# decorators function:
""" def decorators_function(any_function):
  def wrapper_function():
    print("this is awesome function")
    any_function()
  return wrapper_function

def func1():
  print("this is function 1")
def func2():
  print("this is function 2")
var= decorators_function(func1)   
var() 
var= decorators_function(func2) 
var() """

""" def decorators_function(any_function):
  def wrapper_function():
    print("this is awesome function")
    any_function()
  return wrapper_function
@ decorators_function             ############# short cut method ############
def func1():
  print("this is function 1")
func1()
def func2():
  print("this is function 2")
func2() """

""" def decorators_function(any_function):
  def wrapper_function(*args,**kwarge):
    print("this is awesome function")
    return any_function(*args,**kwarge)
  return wrapper_function
@ decorators_function
def func(a):
  print(f"this is function with argument {a}")
func(5)    

@ decorators_function
def add(a,b):
  return a+b
print(add(2,3)) """

                #################### to add doc ################
""" from functools import wraps
def decorators_function(any_function):
  @ wraps(any_function)
  def wrapper_function(*args,**kwarge):
    ''' this is wraps function '''
    print("thid is awesome function")                
    return any_function(*args,**kwarge)
  return wrapper_function

@ decorators_function
def add(a,b):
    ''' enter two number than we get sum of two number '''
    return a+b
print(add(2,3))
print(add.__doc__) """

              ############### next example ################
""" from functools import wraps
def print_functon_data(function):
  @ wraps(function)
  def wrapper(*args,**kwargs):
    print(f"you are calling {function.__name__} function ")
    print(f"{function.__doc__}")
    return function(*args,**kwargs)
  return wrapper  
@ print_functon_data
def add(a,b):
    ''' enter two number than we get sum of two number '''
    return a+b
print(add(2,3))  """

###### next question #####
""" from functools import wraps
import time
def calculate_time(function):
  @ wraps(function)
  def wrapper(*args,**kwarge):
    print(f"you are calling a {function.__name__} function ")
    t1= time.time()
    return_value= function(*args,**kwarge)
    t2=time.time()
    total_time=t2-t1
    print(f"the function took total time {total_time}")
    return return_value
  return wrapper

@ calculate_time
def square_finder(n):
  return[i**2 for i in range (1,n+1)]
print(square_finder(100)) """

  ######## 
""" from functools import wraps
def only_it_allow(function):
  @ wraps(function)
  def wrapper(*args,**kwarge):
    if all([type(args)==int for args in args]):
      return function(*args,**kwarge)
  print("invalied arguments") 
  return wrapper 

@ only_it_allow
def add_all(*args):
  total=0
  for args in args:
    total +=args
  return total
print(add_all(1,2,3,4,5,"nukhil")) """


""" from functools import wraps
def only_data_type_allow(data_type):
  def decorators(function):
    @ wraps(function)
    def wrapper(*args,**kwarge):
      if all([type(args)==data_type for args in args]):
        return function(*args,**kwarge)
      print("invalied arguments")
    return wrapper 
  return decorators

@ only_data_type_allow(str)
def string(*args):
  string=" "
  for i in args:
    string +=i
  return string
print(string("nukhil","kumar", "ram")) """

##### generators : it is used when we want to use once .
#####      list : it is uses when we want to use many time in pogram.

""" def num(n):
  for i in range(1,n+1):
    yield(i)

for number in num(10):
  print(number) """

""" def num(n):
  for i in range (1,n+1):
    yield(i)

number = num(10)
for num in number:
  print(num)
for num in number:
  print(num) """

""" def even_generator(n):
   for num in range (1,n+1):
    if num%2==0: 
      ##### OR ###
   for num in range(2,n+1,2): 
      yield(num)
even_nums=even_generator(10)
for num in even_nums:
  print(num)       """

##### generator comprehension #####               -> it is same as list comprehesion in list we use -> [] and in -> we use (). 
""" square=(i**2 for i in range(1,11))    
for num in square:
  print(num)  
for num in square:
  print(num)  """


                                      ##################  class and object #######
""" class person:
  def __init__(self,first_name,last_name,age):
    print("init method called")
    self.first_name=first_name
    self.last_name=last_name 
    self.age=age

p1=person("nikhil","kumar",34)
p2=person("rohan","kumar",54)
print(p1.first_name)
print(p2.last_name)    """

##### next question ######
""" class laptop:
  def__init__(self,brand,model_name,price):
  print("init method called")
  self.brand=brand
  self.name=model_name
  self.price=price
  self.laptop_name=brand+" "+model_name
  laptop1=laptop("HP","fff2x3n",65000)
  print(laptop1.laptop_name)  """ 


      ####### next important question #####
""" class person:
  def __init__(self,first_name,last_name,age):
    print("init method called")
    self.first_name=first_name
    self.last_name=last_name 
    self.age=age
  def full_name(self):
    return f"{self.first_name}  {self.last_name}"  
  def is_above_18(self):
    return self.age>18
p1=person("nikhil","kumar",34)
p2=person("rohan","kumar",54)
print(p1.full_name() ,p1.is_above_18())
print(p2.full_name())  """

""" class laptop:
  def__init__(self,brand,model_name,price):
  self.brand=brand
  self.name=model_name
  self.price=price

  def apply_discount(self,num):
    off_price= (num/100)*self.price
    return=self.price-off_price


laptop1=laptop("HP","fff2x3n",65000)
print(laptop1.apply_discount(10))  """

########  class variable ####
""" class circle:
  pi=3.14  #### class variable
  def __init__(self,radius):
    self.radius= radius
  def calc_circumference(self):
      return 2*circle.pi*self.radius
c=circle(4)
print(c.calc_circumference())  """  

""" class laptop:
  applied_discount=50
  def __init__(self,brand,model_name,price):
    self.brand=brand
    self.name=model_name
    self.price=price
  def apply_discount(self):
      off_price= (self.applied_discount/100)*self.price     # if we use self in discount than we check first in object " or" if we use class(laptop) name than we will check from class whether it is present or not.
      return self.price-off_price


laptop1=laptop("HP","fff2x3n",65000)
laptop1.applied_discount=10
print(laptop1.apply_discount())  """

""" class person:
  count_instance=0                                               # to count how must object class is created.
  def __init__(self,first_name,last_name,age):
    person.count_instance +=1
    print("init method called")
    self.first_name=first_name
    self.last_name=last_name 
    self.age=age
  def full_name(self):
    return f"{self.first_name}  {self.last_name}"  
  def is_above_18(self):
    return self.age>18
p1=person("nikhil","kumar",34)
p2=person("rohan","kumar",54)
print(p1.full_name() ,p1.is_above_18())
print(p2.full_name()) 
print(person.count_instance) """


#########    class method  ######

""" class person:
  count_instance=0                                              
  def __init__(self,first_name,last_name,age):
    person.count_instance +=1
    print("init method called")
    self.first_name=first_name
    self.last_name=last_name 
    self.age=age
  @classmethod
  def count_instances(cls):     # class method 
    return f"you have created {cls.count_instance}  of {cls.__name__} class"  
  def full_name(self):
    return f"{self.first_name}  {self.last_name}"  
  def is_above_18(self):
    return self.age>18
p1=person("nikhil","kumar",34)
p2=person("rohan","kumar",54)
print(person.count_instances()) """


#####################  class method as constructor  ##################

""" class person:
  count_instance=0                                              
  def __init__(self,first_name,last_name,age):
    person.count_instance +=1
    print("init method called")
    self.first_name=first_name
    self.last_name=last_name 
    self.age=age

  @classmethod
  def from_string(cls,string):                 #############  class method as constructor
    first,last,age=string.split(",")
    return cls(first,last,age)  
  @classmethod
  def count_instances(cls):     # class method 
    return f"you have created {cls.count_instance}  of {cls.__name__} class"  
  def full_name(self):
    return f"{self.first_name}  {self.last_name}"  
  def is_above_18(self):
    return self.age>18
p1=person("nikhil","kumar",34)
p2=person("rohan","kumar",54)
#print(person.count_instances())
p3=person.from_string("Nikhil,Kumar,23")
print(p3.full_name(),p3.age) """

######### static method #######

""" class person:
  count_instance=0                                              
  def __init__(self,first_name,last_name,age):
    person.count_instance +=1
    print("init method called")
    self.first_name=first_name
    self.last_name=last_name 
    self.age=age

  @classmethod
  def from_string(cls,string):           # class method as constructor
    first,last,age=string.split(",")
    return cls(first,last,age)  
  @classmethod
  def count_instances(cls):     # class method 
    return f"you have created {cls.count_instance}  of {cls.__name__} class"  
  @staticmethod          # static method
  def hello():
    print("hello, static method is called.")  
  def full_name(self):
    return f"{self.first_name}  {self.last_name}"  
  def is_above_18(self):
    return self.age>18
p1=person("nikhil","kumar",34)
p2=person("rohan","kumar",54)
#print(person.count_instances())
p3=person.from_string("Nikhil,Kumar,23")
print(p3.full_name(),p3.age)
person.hello()       # printing static method.       """


  ##### encapsulation :- creating of class  and define function inside class is known as encapsulation abvoe example show that encapulsation. 
    ####  abstraction : user se hiding karn hi abstraction means how programe is runing user do not know alog of these ,it increase the performance.for example:-
""" l=[15,6,3,4,1,2]
l.sort()     # tim sort()        # how it is arrange in order is known as abstraction.
print(l)    """ 

  # abstraction will done when encapsulation is done.
# in python all are public know one is private. put to define in private we use ( _ ) symbols.
# __name___ =dunder/magic name. 

""" class person:
  def __init__(self,first_name,last_name,age):
    print("init method called")
    self.first_name=first_name
    self.last_name=last_name 
    self._age=age
    self.__age=age # this become more private .

p1=person("nikhil","kumar",34)
p2=person("rohan","kumar",54)
print(p1._person__age) do """


###### inheritance  intro  #########
""" class Phone:
  def __init__(self,brand,price,model_name):
    self.brand=brand
    self._price=max(price,0)
    self.model_name=model_name

  def full_name(self):
    return f"{self.brand} {self.model_name}"

  def make_a_call(self,number):
    return f"calling {number}"

class smartphone(Phone):
  def __init__(self,brand,price,model_name,ram,interal_memory,rear_camer):
    Phone.__init__(self,brand,price,model_name)
    self.ram=ram
    self.interal_memory=interal_memory
    self.rear_camer=rear_camer    
phone= Phone("nokia",1000,"llmxbn")
smartphone=smartphone("oneplus",30000,"5","4gb","64gb","20 MP")
print(phone.full_name())
print(smartphone.full_name() + f" and price is  {smartphone._price}") """

# method overriding: it define that if we create same func in dervied class than it will call first dervied class than check base class.
# isinstance:- it is used to check whether it is object of class or not.
# issubclass:- it is used o check whether it is sub class odf class or not.


######################  multiple inheritance  #######################

""" class A:
  def class_a_define(self):
    return "I/m just a class A method"
  def hello(self):
    return "hello from class A"
class B:
  def class_b_define(self):
    return "I/m just a class B method"
  def hello(self):
    return "hello from class B"   
class C(A,B):
  pass
instance_c=C()
print(instance_c.class_a_define())
print(instance_c.class_b_define())       
print(instance_c.hello()) """

#operator overloding :- means using operator such as add, mul,div etc function  is operator oveloading .such eg shown down. 

#polymorphism :- it means many form . for eg operator overloding and method overriding.                       


""" class Phone:
  def __init__(self,brand,price,model_name):
    self.brand=brand
    self._price=max(price,0)
    self.model_name=model_name

  def full_name(self):
    return f"{self.brand} {self.model_name}"

  def make_a_call(self,number):         
    return f"calling {number}"
  def __add__(self,other):                  # operator oveloading
    return self._price + other._price

class smartphone(Phone):
  def __init__(self,brand,price,model_name,ram,interal_memory,rear_camer):
    Phone.__init__(self,brand,price,model_name)
    self.ram=ram
    self.interal_memory=interal_memory
    self.rear_camer=rear_camer   
  def __add__(self,other):
    return self._price + other._price   
phone= Phone("nokia",1000,"llmxbn")
phone1=Phone("oneplus",30000,"5")
print(phone + phone1)               # operator overloading printing. """

###### Raise errors ######
""" def add(a,b):
  if(type(a) is int and type(b) is int):
    return a+b
  else:
    return TypeError("opps you are passing different data")
print(add(2,"nikh"))  """     

##### Exception handling ####
 #try except else finally:

""" while True:
  try:
    age= int(input("enter a age: "))             # we will insert try case where we het error by seeing these condition we get valueerror so we create valueerror. 
    break
  except ValueError:
    print("maybe you entered string insted of number , try again")
  except:
    print("unexpected error.....")
if age<18:
  print("you can play this game. ")
if age>18:
  print("you can't play this game. ") """   

####   else and finally clause in exception handling ###

""" while True:
  try:
    number=int(input("enter a number "))
  except ValueError:
     print("may be you entrered string insted of number, try again")
  except:
    print("unexpected error...... ")
    break
  else:
    print(f"number you entered{number}")
    break
  finally:
    print("finally block.......!!!! ")  """      


 # custom Exception:
 
""" class nametoshort(ValueError):
  pass
def validate(name):
  if len(name)<8:
    raise nametoshort("name entered is very short ")
username=input("enter your name ")
validate(username)
print(f"hello{validate}")   """ 

### file handling  ######

# f.read()
# f.tell()  its tells  how many word in file from statring to end.
# f.close()
# f.readline()  its read line by line in file ????? and to decrease space between line we use end=''. for eg print(f.readline(),end='')
# f.readlines()  it will convert each line into string. for eg shown below.

""" f=open("file1.txt")
#print(f"cursor position - {f.tell()}")
#print(f.read())
#print(f"cursor position - {f.tell()}")
#print(f.read())
#lines=f.readlines()
for line in f.readlines()[:2]:
  #print(line,end='')
 print(line)
print(len(line))
f.close() """

### with block

""" with open("file1.txt") as f:
  data=f.read()
  print(data)


print(f.closed) """
# w: it is used write any thing in file ,It is generally used when file is empty.
#for eg:-

""" with open('file2.txt') as f:
  f.write('hello') """

# a: it used to insrt a some text in file viedo no 217.
""" with open('file.txt','a') as f:
  f.write("\n please do it") """

# r+ :- it is used read and write fuction 
""" with open("file2.txt","r+") as f:
  f.seek(len(f.read()))
  f.write("/ntoday input") """
#a
""" with open ("file1.txt","a") as f:
  f.write("\nplease do it") """

""" with open ("file3.txt","a") as f:
  f.write("\nplease do it")   """       


# file read and write   from file 2 it will write file 1.
""" with open("file2.txt","r") as rf:

  with open("file1.txt","w") as wf:
    wf.write(rf.read()) """

# example :-
""" with open("salary.txt","r") as rf:
     with open ("output.txt","a") as wf:
       for line in rf.readlines():
         name,salary=line.split(",")
         wf.write(f"{name}\'s salaray is {salary}") """

 ######   we will see viedo no 221 to 223 later on.
        
#### os module(2)  ################

""" import os
os.chdir(r"E:\css")
fileiter = os.walk(r"E:\css")
for current_path, folder_name,file_name in fileiter:    #### in tis program we read what are there in file img and docs,document.
  print(f"current path : {current_path}")
  print(f"folder name : {folder_name}")
  print(f"file name : {file_name}") """

    #    to create a file  
""" import os
os.makedirs("new/movies")  """  

""" import shutil
# shutil.rmtree("n")  # it is used to delete a file here file name is ("n") 
shutil.copytree("new","document/new") # in this the new file will cpy in document file we change file name by changeing name of new which are written down the document just new equal to new 123.
shutil.copy("file.txt","document/file.txt") # in this we will copy file in document.
shutil.move("file.txt","new/file34.txt")  # in this we will move file in new folder. """

    #################          dice programe          ##########################

""" import random
print("This is a dice stimulator")
x = "y"

while x == "y":
    number = random.randint(1,6)

    if number == 1:
        print("----------")
        print("|        |")
        print("|    O   |")
        print("|        |")
        print("----------")
    if number == 2:
        print("----------")
        print("|        |")
        print("| O    O |")
        print("|        |")
        print("----------")
    if number == 3:
        print("----------")
        print("|    O   |")
        print("|    O   |")
        print("|    O   |")
        print("----------")
    if number == 4:
        print("----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------")
    if number == 5:
        print("----------")
        print("| O    O |")
        print("|    O   |")
        print("| O    O |")
        print("----------")
    if number == 6:
        print("----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------")
    x = input("Press y to roll again")
     """


     ########################          Hangman game    ##################

""" import random
def hangman():

    word = random.choice(["pugger" , "littlepugger" , "tiger" , "superman" , "thor" , "pokemon" , "avengers" , "savewater" , "earth" , "annable" ])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("You win!")
            break

        print("Guess the word:" , main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break


name = input("Enter your name")
print("Welcome" , name )
print("-------------------")
print("try to guess the word in less than 10 attempts")
hangman()
print()
 """


########################             QR code               ##############################
""" import pyqrcode
msg=pyqrcode.create("Hello I am Nikhil Kumar , belong to Begusarai Bihar. Now i am a student who studies in UPES Dehardun Uttarakhand .  ")
msg.png("E:/Nikhil.png",scale=8) 
print("your QR code is ready in C drive") """