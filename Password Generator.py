#We use random module in python to generate a password at random
import random

#Function for generating password
def passwordgenerator(n):
    required_keys="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()+-*/,.<>"
    password=""

    for i in range(n):
        password += random.choice(required_keys)
    return password

#user input for length of password
n=int(input("Enter the length of the Password:\n"))
password=passwordgenerator(n)
print("The generated password for you is:",password)