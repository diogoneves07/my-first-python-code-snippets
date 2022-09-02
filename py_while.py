"""Using loops"""

import random

roll = 0
count = 0

print("The first person to get 5 will win :)")
while roll!=5:
      name = input('Enter a name, or \'q\' to quit:   ') 
      if name.strip()=='':
            continue
      if name.strip()=='q':
            break
      count+= 1
      roll = random.randint(1, 5)
      print(f"{name} \t rolled: \t {roll}")
else:
      print(f"{name} Wins!!!")

print(f" You rolled the dice {count} times.")