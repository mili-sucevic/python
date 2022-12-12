# Random Password Generator using Python

#import the necessary modules!
import random as r
import string as s

print('Hello, Welcome to Password Generator!')

#input the length of password
length = int(input('\nEnter the length of password: '))                      

#define data
lower = s.ascii_lowercase
upper = s.ascii_uppercase
num = s.digits
symbols = s.punctuation
# letters = s.ascii_letters

#combine the data
all = lower + upper + num + symbols

#use random 
temp = r.sample(all,length)

#create the password, join together without spaces
password = "".join(temp)

#print the password
print(password)
