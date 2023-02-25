#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sheetal Yadav
#
# Created:     24-02-2023
# Copyright:   (c) Sheetal Yadav 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# mini project (making a calculator)

A=input("please enter the first number ")
operator=input("please enter operator(+,-,*,/,%) : ")
B=input("please enter the second number ")
A=int(A)
B=int(B)
if operator=="+":
    print(A+B)
elif operator=="-":
    print(A-B)
elif operator=="*":
    print(A*B)
elif operator=="/":
    print(A/B)
elif operator=="%":
    print(A%B)
else:
    print("You have enter invalid operator")
