# OOPS Object Oriented Prograimming programming.


### Class : Class is a blueprint of object.
1. Structure , pattern , prototype of an objects
2. Contains logical description.
3class do not occupy much memory as object.

#### class
> in class we define state and behavior of an object inside a class
#### How to achieve class in python ,
1. How to define class in python.
```python
class <class_name> : # <class_name> should be a identifier
    # implimentation of state and behavior
```
>  python is a functional programming language. <br>
> functional programming : functions inside libraries.
2. Implimentation
```python 
class Students :
    # variables :
    s_id = ""
    roll_no = 0
    email = "ex@example.com"
```
3. Class Members : who would be the members of a class., class contains following things
    - variables also known as data members.
    - constructors
    - methods or functions also known as member functions.
4. 
5. Memory Representation
#### AI ML GenAI Agentic AI
// java has inner class and blocks , complex rules of java , nested class.
ex. Design and structure of class.

# Everything which takes space in the world is a real object.

### objects : Real Entity or instance of class,

1. object will occupy memory. 
2. physical representation of a class.
3. object is a run time entity as memory is allocated 
4. When an object is created memory is allocated to it based on class definition
5. objects and instance means same.
6. object is an working instance of a class created at run time.
ex , real car entity.

### How to access and use members of class
> using objects via dat operator '.' , <br>
> dot operator is used for reference <br>
> we can access variables and methods outside class using dot operator.

## constructor

```pycon
def __init__(self) :
    pass
```
### self 
1. self is a keyword and reference to the current object. 
> self reference current invoking object , 
2. self is a reference variable to the current object or instance of the class.
3. self helps methods to know the current working object.
4. self is used inside class methods to access instance variables of current working object.
5. self work as instance variable 
6. self must be the first parameter in instance method , method of function.
> `` def __init__(self,id,name) :``
7. We do not need to pass 'self' explicitely while calling method or functions.
> Every time we call a method or an object , python automatically passes object as a first parameter or as a first argument <br>
> `` c1 = Customer(101,"AT")`` # we didn't passed self  <br>
> c1 is the current object passed in the self automatically by python
 
? Who carry the actual value : 
reference variable v/s variables { Actual real time storage }
reference variables holds the address of actual variable.

### Types of variable : level 2
> named storge location , variable name known as Domain Name
1. Instance variable : 
> variables related to the instance are called instance variables
2. Class variable  : also called static variable .
> variables related to the class are known as static variable 
3. Local variable
4. Global variable

#### Instance Variable
1. Instance variables are defined inside special method called '__init__' also known as constructor. using 'self' <br> ``self.var_name``
2. instance variables belongs to the specific object.
````python
def __init__(self,name,id) :
   self.name = name # name is called instance variable
   self.id = id # id in self.id is called instance variable
    pass
````
3. Different objects will have different copy of instance variable.
4.  change in one instance variable of an object do not change instance variable of another object.
5.  instance variables are unique for unique objects.
```python
class Student:
    def __init__(self, name, age):
        self.name = name      # instance variable d
        self.age = age        # instance variable

s1 = Student("Rahul", 20)
s2 = Student("Anita", 22)

print(s1.name)  # Rahul
print(s2.name)  # Anita

```
6. instance variables can be declared inside '__init__' function and can be accessed inside 'init' or outside 'init' using 'self' instance.
7. We can declare any number of instance varialbes.
8. memory allocated to instance variable depends on number of objects.

### class variables  or static variable
1. class variables are common for all objects.
2. class variables declared inside class but initialized outside class.
3. class variables can be accessed using className , self or Object.
4. Only one copy of memory is shared among all objects for the static variable.
```python
# class
class Car:
    wheels = 4  # class variable

    def __init__(self, brand):
        self.brand = brand  # instance variable

car1 = Car("Toyota") # object declaration
car2 = Car("Honda")

print(car1.wheels)  # 4 # class variable accessed using objectName
print(car2.wheels)  # 4
print(Car.wheels) #  class variable accessed using class name
```

### local variables 
1. local variables :  variables which are accessed within a scope ,
2. local variables defined in the functions
3. local variables not accessible outside class

### global variables 
1. Those variables which are declared inside main function.
2. variables accessible throughout program


## Constructor 
1. Constructor is a special method which is initialized when object of the class is declared.
2. instance variables are declared inside constructor.
3. python's constructor's name is not same as className
> In python constructor special function always named as '__init__' <br>
> python provides a fixed constructor name called '__init(self)' <br>
> constructor of the class automatically called when object of the class is created or initialized.
4. Constructor's task is to initialize the instances variables for different objects.

## Types of Constructors
1. Default constructors : Without parameters
2. Default Argument constructors , with default parameters