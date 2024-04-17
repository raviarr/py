#Defining a Function
def create_group(person1, person2):
    group = [person1, person2]
    return group 
person1 = "Ravia"
person2 = "Roshnee"

my_group = create_group(person1, person2)

print(f"Group members: {my_group}")

def generate_brand_name():
    print("welcome to the band name generator.")

    city = input("Which city did you grow up in?\n")
    pet = input("What is the name of your pet?\n")

    brand_name = f"{city.capitalize()} {pet.capitalize()}"
    return brand_name

brand_name = generate_brand_name()
print("your band name is:", brand_name)  

import time

my_timer = int(input("Enter the time in seconds:"))

for sec in range (my_timer,0, -1):
    print(sec)
    time.sleep(1)


     




