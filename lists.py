menus = ['antipasto', 'bruschetta', 'cannoli', 'fettuccine', 'gnocchi', 'lasagna', 'minestrone', 'osso buco', 'panna cotta', 'ravioli', 'spaghetti', 'tiramisu', 'ziti']

#Negetive indexing
print(menus[-1])
print(menus[-2])

#Ranges of index
print(menus[2:5])
print(menus[-5:-2])
print(menus[:5])
print(menus[5:])

#Item present or not
if 'osso buco' in menus:
    print('Food present in Menu!')
else:
    print('Food not present in Menu.')

if 'pasta' not in menus:
    print('Food not present in Menu.')
else:
    print('Food present in Menu!')


#Changing items in list
print(menus)
menus[8] = 'pani câ meusa'
print(menus)
menus[3:6] = ['trippa', 'lampredotto', 'songbirds']
print(menus)
menus[3:4] = ['trippa', 'lampredotto', 'songbirds']
print(menus)

#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
substitute_menu = ['trippa', 'lampredotto', 'songbirds']
substitute_menu[1:3] = ["pasta"]
print(substitute_menu)

#insert()
substitute_menu = ['trippa', 'lampredotto', 'songbirds']
substitute_menu.insert(2,'pasta')
print(substitute_menu)

#append()
substitute_menu.append('sicily')
print(substitute_menu)

#extend()
substitute_menu1 = ['trippa', 'lampredotto', 'songbirds']
substitute_menu2 = ['lombardy', 'campania', 'tuscany']
substitute_menu1.extend(substitute_menu2)
print(substitute_menu1)

#loop or traverse
for item in menus:
    print(item)

for item in range(len(substitute_menu)):
    print(substitute_menu[item])


#List Comprehension
# Expression : newlist = [expression for item in iterable if condition == True]

veg_dishes = ['spinach pasta', 'mushroom risotto', 'margherita pizza', 'eggplant parmesan', 'vegetable lasagna']
veg_dishes_copy_1 = [x for x in veg_dishes]
veg_dishes_copy_2 = [x for x in veg_dishes if 'a' in x]
veg_dishes_copy_3 = [x for x in veg_dishes if 'a' not in x]
print('Vegeterian Dish 1',veg_dishes_copy_1)
print('Vegeterian Dish 2',veg_dishes_copy_2)
print('Vegeterian Dish 3',veg_dishes_copy_3)

#Sorting
fruit_juices = ['apple juice', 'Orange juice', 'grape juice', 'Pineapple juice', 'mango juice', 'cranberry juice', 'Strawberry juice', 'pomegranate juice']
print("Fruit juices:", fruit_juices)

fruit_juices.sort()
print("Sorted Fruit Juices:",fruit_juices) #Ascending

fruit_juices.sort(reverse= True)
print("Sorted Fruit Juices:",fruit_juices) #Descending

fruit_juices.sort(key = str.lower)
print("Sorted Fruit Juices:",fruit_juices)

fruit_juices.reverse()
print("Sorted Fruit Juices:",fruit_juices) #Descending

#Copy and Join

desserts_1 = ['chocolate cake', 'ice cream', 'apple pie', 'cheesecake', 'brownies']
desserts_copy_1 = desserts_1.copy()
print(desserts_copy_1)
desserts_copy_2 = list(desserts_1)
print(desserts_copy_2)
desserts_copy_3 = desserts_1[:]
print(desserts_copy_3)

desserts_2 = ['tiramisu', 'creme brulee', 'banana split', 'pudding', 'fruit tart']
desserts = desserts_1 + desserts_2
print(desserts)
for x in desserts_2:
    desserts_copy_1.append(x)
print(desserts_copy_1)
desserts_copy_2.extend(desserts_2)
print(desserts_copy_2)


