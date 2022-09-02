"""Using list."""
import random

colors = ['red', 'green', 'blue', 'neymar']
red = colors.pop(0)

colors.append('dioog')
colors.remove('blue')

new_colors = ['pink']
new_colors.extend(colors)

print(new_colors)
colors.clear()
print(colors)
print("dioog" in new_colors)
print("dioog" not in new_colors)

for i in new_colors:
      print(i)
else:
      print("m")

my_choice=random.choices(new_colors, k=2)

print(my_choice)










my_list =[1,2,3,3,4,5,6,7,8,9]
my_list[2:3] = "Diogo Neves";
my_another_list =my_list[2:8];
my_another_list.extend(["Neves", "Pereita"])
concat_lists =my_list + my_another_list;
del concat_lists[2:8];


