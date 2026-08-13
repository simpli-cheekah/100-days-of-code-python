friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
import random

name = random.choice(friends)
print(name)  # returns any name from the friend group

     #OR

print(random.choice(friends)) #shorter

      #OR
print(friends[random.randint(0,4)])