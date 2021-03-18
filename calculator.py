#calculator by ClosHub 2021

from multiprocessing.connection import answer_challenge
import math

print("Welcome to my first calculator in Python")

a = input("type your first number: ")
b = input("type your second number: ")

ans = input("so you typed your numbers choose what do u want... ( 1 is +, 2 is -, 3 is %, 4 is *, 5 is /, 6 is // ) : " )
'''
num = a 
num1 = b
choose = c
'''
if ans is 1 :
    print("\nthe results is: ")
    print(float(a + b) )

if ans is 2 :
    print("\nthe results is: ")
    print(float(a - b) )

if ans is 3 :
    print("\nthe results is: ")
    print(float(a % b) )

if ans is 4 :
    print("\nthe results is: ")
    print(float(a * b) )

if ans is 5 :
    print("\nthe results is: ")
    print(float(a / b) )

if ans is 6 :
    print("\nthe results is: ")
    print(float(a // b) )

print("so yeah thas my first program oh \n i forget that type plz the number 4 to reveal a secret tip")

a = input()

if a is 4:
    print("thats P :D")
    print(math.pi)
