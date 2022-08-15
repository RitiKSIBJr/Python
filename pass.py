import random
import string

characters = string.ascii_letters+string.digits+string.punctuation
myList = []

length = int(input("Enter the length of the password: "))

while length > len(myList):
    myList.append(random.choice(characters))
  

Password = ''.join(myList)

print(f"Password : {Password}")