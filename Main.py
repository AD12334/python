import numpy as np
import string
import time
import random
symbols = [
    "’", "~", "!", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", "|", ":", ";", '"', "'", "<", ">", ".", "?", "/"
]
numbers = ["0","1","2","3","4","5","6","7","8","9"]

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
symbols = np.array(symbols)
numbers = np.array(numbers)
lower = np.array(lower)
upper = np.array(upper)
potential = np.concatenate((symbols, numbers, lower, upper))

elements = {}



#Make a password
passwordnumber = input("How many password do you want to be made: ")
for i in range(int(passwordnumber)):
    password = []

    for i in range(int(random.randint(1,20))):
        password.append(np.random.choice(upper)[0])  # Access the first element from the array

    for i in range(int(random.randint(1,20))):
        password.append(np.random.choice(lower)[0]) 

    for i in range(int(random.randint(1,20))):
        password.append(np.random.choice(symbols)[0]) 

    for i in range(int(random.randint(1,20))):
        password.append(np.random.choice(numbers)[0])  

    password = np.random.permutation(password)  # Shuffle the password

    password = ''.join(password)  # Convert the array back to a string

    print("Generated Password: ", password)
    for i in range(len(password)):
        if (password[i] in symbols):
            #print("hit" + " " + password[i] + " at index :" + str(i))
            elements[password[i]] = elements.get(password[i], 0) + 1 

    for i in range(len(password)):
        if (password[i] in numbers):
         #print("hit" + " " + password[i] + " at index :" + str(i))
            elements[password[i]] = elements.get(password[i], 0) + 1 

    for i in range(len(password)):
        if (password[i].isalpha()):
         if(password[i].isupper()):
            # print("hit" + " " + password[i] + " at index :" + str(i))
            elements[password[i]] = elements.get(password[i], 0) + 1 

    for i in range(len(password)):
        if (password[i].isalpha()):
            if(password[i].islower()):
             #print("hit" + " " + password[i] + " at index :" + str(i))
             elements[password[i]] = elements.get(password[i], 0) + 1 

#print(elements)

# Guess the password

    guess = ""
    fails = 0
    seconds1 = time.time()
    for i in range(len(password)):
        while True:  # Keep trying until the correct character is guessed
            for char in potential:
                if char == password[i]:  # If the character matches
                    guess += char  # Add the character to the guess
                    print(f"Found '{char}' at index {i}")
                    break
                else:  # If the character does not match
                    fails+=1
            if guess[i] == password[i]:  # Exit the loop when the correct character is found
                break
    seconds2 = time.time()

    execution_time = seconds2 - seconds1

    print(f"The password was guessed in {execution_time} seconds.")
    print(f"Failed attempts: {fails}")
    f = open("analysis.csv", "a")

    f.write(f"Password: {password},Execution Time: {execution_time} seconds,Failed Attempts: {fails}\n")

