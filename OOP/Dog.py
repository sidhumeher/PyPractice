'''
Created on Oct 4, 2020

@author: sidteegela
'''


class Pet(object):  # Parent
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} old')
    
    def speak(self):
        print('I am a pet')


class Dog(Pet):  # Child
    
    def __init__(self, name, age, color):
        super().__init__(name, age)  # Parent class constructor
        self.color = color
    
    def speak(self):  # Overrides parent method
        print("Bark")

    def show(self):
        print(f'I am {self.color}')


class Cat(Pet):  # Child
    
    def speak(self):  # Overrides parent method
        print('Meow')

        
class Student(object):
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []  # Objects of student class go here
        
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False
        
    def get_avg_grade(self):
        pass
        

class Person:
    
    no_of_people = 0  # Class attribute
    
    def __init__(self, name):
        self.name = name
        # Person.no_of_people += 1
        Person.add_person()

    @classmethod 
    def number_of_people(cls):
        return cls.no_of_people
    
    @classmethod  # Method attributed to class Person
    def add_person(cls):
        cls.no_of_people += 1

    @staticmethod  # Static method dont change anything
    def add(x):
        return x + 5


if __name__ == '__main__':
    
    '''
    d = Dog('Cleo')  # Instance of Dog
    d.bark()
    print(type(d))
    '''
    '''
    s1 = Student('Sid', 31, 95)
    s2 = Student('Mat', 31, 90)
    s3 = Student('Scott', 50, 75)

    course = Course('Computer science', 2)
    course.add_student(s1)
    course.add_student(s2)
    
    print(course.students[0].name)
    '''
    '''
    p = Pet('Cleo', 1)
    p.show()
    p.speak()
    dog = Dog('Ponyo', 2, 'Red heeler')
    dog.show()
    dog.speak()
    cat = Cat('Micky', 3)
    cat.show()
    cat.speak()

    dog1 = Dog('Ponyo', 2, 'Blue heeler')
    dog1.show()
    '''
    p1 = Person('TIme')
    print(p1.no_of_people) 
    p2 = Person('Mat')
    print(p2.no_of_people)
    # Person.no_of_people = 9
    
    print(Person.add(5))  # Static method call
    
