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
veg_dishes = ['spinach pasta', 'mushroom risotto', 'margherita pizza', 'eggplant parmesan', 'vegetable lasagna']
veg_dishes_copy_1 = [x for x in veg_dishes]
veg_dishes_copy_2 = [x for x in veg_dishes if 'a' in x]
veg_dishes_copy_3 = [x for x in veg_dishes if 'a' not in x]
print('Vegeterian Dish 1',veg_dishes_copy_1)
print('Vegeterian Dish 2',veg_dishes_copy_2)
print('Vegeterian Dish 3',veg_dishes_copy_3)