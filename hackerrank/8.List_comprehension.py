
# Loop method to append and store data
my_list = ['apple', 'mango', 'banana']

new_list = []
for color in my_list:
  color = color + ' yellow'
  new_list.append(color)


# In list comprehension, we can achieve the above loop calculation in a single line
new_list = [color + ' yellow' for color in my_list]

