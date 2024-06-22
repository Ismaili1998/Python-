x = txt.startswith("ell", 1, 4)
from datetime import date
# random Person
class Person:
    class_var = "hello"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)
    
    def display(self):
        print(self.name + "'s age is: " + str(self.age))
    
    @classmethod  
    def get_class_var1(cls):
        cls.class_var = "hello from this class method"

    @classmethod  
    def get_class_var2(cls):
        return cls.class_var

person = Person('Adam', 19)
person.display()

person1 = Person.fromBirthYear('John',  1985)
print(person1)
person1.display()
Person.get_class_var1() # hello from this class method
print(Person.get_class_var2()) # hello from this class method
# hasattr built in functions 
# isinstance(obj, a type here )

class Base :
    
    def __init__(self, a, b, c):
        self.a = a
        self._b = b
        self.__c = c
    def get_c(self):
        return self.__c 

class Child(Base):
    
    def __init__(self, a, b, c):
        super().__init__(a, b, c)  # Corrected line
    
Correct! This code demonstrates polymorphism because the add function can work with different types (integers and strings) without explicit type checking.   
        
b = Base(1, 2, 3) # fine 
print(b.a, b._b) # fine 
#print(b.a, b.__c) # Nope, not allowed 
child = Child(10, 20, 30) # fine 
print(child.a, child.get_c()) # fine 


# magic methos : These are commonly used for operator overloading. 
# __ge__ __le__ __add__ __sub__ __neg__ __del__ (when we delete)
# __floor__

Initialization and Construction

__new__: To get called in an object’s instantiation.
__init__: To get called by the __new__ method.
__del__: It is the destructor.
Numeric magic methods

__trunc__(self): Implements behavior for math.trunc()
__ceil__(self): Implements behavior for math.ceil()
__floor__(self): Implements behavior for math.floor()
__round__(self,n): Implements behavior for the built-in round()
__invert__(self): Implements behavior for inversion using the ~ operator.
__abs__(self): Implements behavior for the built-in abs()
__neg__(self): Implements behavior for negation
__pos__(self): Implements behavior for unary positive 
Arithmetic operators

__add__(self, other): Implements behavior for math.trunc()
__sub__(self, other): Implements behavior for math.ceil()
__mul__(self, other): Implements behavior for math.floor()
__floordiv__(self, other): Implements behavior for the built-in round()
__div__(self, other): Implements behavior for inversion using the ~ operator.
__truediv__(self, other): Implements behavior for the built-in abs()
__mod__(self, other): Implements behavior for negation
__divmod__(self, other): Implements behavior for unary positive 
__pow__: Implements behavior for exponents using the ** operator.
__lshift__(self, other): Implements left bitwise shift using the << operator.
__rshift__(self, other): Implements right bitwise shift using the >> operator.
__and__(self, other): Implements bitwise and using the & operator.
__or__(self, other): Implements bitwise or using the | operator.
__xor__(self, other): Implements bitwise xor using the ^ operator.

Instance methods need a class instance and can access the instance through self.
Class methods don’t need a class instance. They can’t access the instance (self) but they have access to the class itself via cls.
Static methods don’t have access to cls or self. They work like regular functions but belong to the class’s namespace.
Static and class methods communicate and (to a certain degree) enforce developer intent about class design. This can have maintenance benefits.

Because the class method only has access to this cls argument, it can’t modify object instance state. That would require access to self. However, class methods can still modify class state that applies across all instances of the class.