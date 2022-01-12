# -*- coding: utf-8 -*-
"""IntroToCengInheritance.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xRXUuXlKi7_X000YQ5uRmdAeHQjTzi-I
"""

class Person:
  def __init__(self, name, lastname, age):
    self.name = name
    self.lastname = lastname
    self.age = age
  
  def walk(self):
    print("Hello world, I am walking")
  
  def talk(self):
    print("Hey I can walk!")

class Student(Person):
  def __init__(self, studentID, department):
    self.studentID = studentID
    self.department = department
    super().__init__('Eyup', 'Cinar', 18)
  
  
  def study(self):
    print('Hey I am studying .. ')

  def takeExam(self):
    print("Hey I just took the exam and it was hard!")

var1 = Student(15212020200, 'Computer Engineering')
var1.name

print(help(Student))

var1 = Student(152120201220, "Computer Engineering")

print(help(Student))