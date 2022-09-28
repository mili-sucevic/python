#!/usr/bin/python3

def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def multi(n1, n2):
    return n1*n2

def div(n1, n2):
    if n2 == 0:
        return "ERROR: Cannot divide by 0. Second parameter cannot be a 0!"
    else:
        return n1/n2

n1 = 10
n2 = 11

print(add(n1, n2))
print(sub(n1, n2))
print(multi(n1, n2))
print(div(n1, n2))
