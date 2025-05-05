#!/usr/bin/env python3

def greet_programmer():
    print(f'Hello, programmer!')
    pass

def greet(name='Guido'):
    print(f'Hello, {name}!')
    pass

def greet_with_default(name="programmer"):
    print(f'Hello, {name}!')
    pass

def add(num1=45,num2= 55):
    return num1+num2
    pass

def halve(number=6):
    return number/2
    pass
def greet_with_default_with_param(name='Guido'):
    print(f"Hello, {name}")