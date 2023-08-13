class Person:
  # Class Attribute
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Class methods
  def greet(self):
    print('Hellom my name is ' + self.name + ' and I am ' + str(self.age) + ' years old.')

# Creating an instance of the class
person = Person("Alice", 30)

# Accessing attributes
print(person.name)  # Output: Alice
print(person.age)   # Output: 30

# Calling methods
person.greet()      # Output: Hello my name is Alice and I am 30 years old.

# Inheritance
class Student(Person):
  def __init__(self, name, age, grade):
    # The super() function is to ensure that when we initilize a Student object, we also initilize the Person object with the attributes name and age
    super().__init__(name, age)
    self.grade = grade
  def greet(self):
    print('Hello my name is ' + self.name + ' and I am ' + str(self.age) + ' years old and I am in grade ' + str(self.grade) + '.')

# Creating an instance of the class
student = Student("Bob", 15, 9)
student.greet()     # Output: Hello my name is Bob and I am 15 years old and I am in grade 9.
