import random

#print(my_module.my_favorite_number) #returns the number in your module you createx

#random_integer = random.randint(1, 10)
#print(random_integer) #returns integers within the range you gave but not inclusive of the numbers

#random_number_0_to_1 = random.random() * 10
#print(random_number_0_to_1) #returns floating point numbers between 0 and 1 but not inclusive of 0 and 1

#random_float = random.uniform(5, 10)
#print(random_float) #returns floating point numbers but inclusive of the numbers in the range you give


random_heads_tails = random.randint(0, 1)

if random_heads_tails == 1:
    print("heads")
else:
    print("tails")