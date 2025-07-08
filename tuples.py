#Create Tuple With One Item
thistuple = ("Mari Gold",)
print(type(thistuple))

#NOT a tuple
thistuple = ("Mari Gold")
print(type(thistuple))

flowers = ["Rose", "Tulip", "Daisy", "Lily", "Sunflower", "Orchid", "Carnation", "Peony", "Iris", "Lavender"]
regular_boquet = tuple(flowers)
print("Type :",type(regular_boquet))
print("Regular Boquet :",regular_boquet)
print("Type Flowers :",len(regular_boquet))
print("First Flower in the row:",regular_boquet[1])
if 'Lavender' in flowers:
    print("Yes Lavender will be there in your boquet.")

#Add item to tuple
new_flowers=list(regular_boquet)
new_flowers.append('Hydrangea')
regular_boquet=tuple(new_flowers)
print("Latest Flower Catalogue:", regular_boquet)

fresh_arrival = ("Peony","Chrysanthemum",)
regular_boquet+=fresh_arrival
print("Updated Flower Catalogue:", regular_boquet)

#Update item to tuple
updating_flowers=list(regular_boquet)
updating_flowers[-1]="Dahlia"
regular_boquet=tuple(updating_flowers)
print("Due to unavailabilty of Chrysanthemum. Updated Flower Catalogue:", regular_boquet)

#Remove item to tuple
updating_flowers=list(regular_boquet)
updating_flowers.remove('Carnation')
regular_boquet=tuple(updating_flowers)
print("Due to unavailabilty of Carnation. Updated Flower Catalogue:", regular_boquet)

#Upacking tuple
red_flowers = ("Geranium", "Begonia", "Asiatic lily", "Poppy", "Gerbera")
(single_order1,single_order2,single_order3,single_order4,single_order5) = red_flowers
print("Sinlge Order 1:",single_order1)
print("Sinlge Order 2:",single_order2)
print("Sinlge Order 3:",single_order3)
print("Sinlge Order 4:",single_order4)
print("Sinlge Order 5:",single_order5)

(single_flower_order1, single_flower_order2, *boquet_order1) = red_flowers
print("Sinlge Order 1:",single_flower_order1)
print("Sinlge Order 2:",single_flower_order2)
print("Boquet Order 1:",boquet_order1)

regular_boquet += red_flowers

# Multiple starred expressions cannot be done
# (*boquet_order1, *boquet_order2, *boquet_order3, *boquet_order4) = regular_boquet
# print("Boquet Order 1:",boquet_order1)
# print("Boquet Order 2:",boquet_order2)
# print("Boquet Order 3:",boquet_order3)
# print("Boquet Order 4:",boquet_order4)

print("Flowers we have:")
for flower in regular_boquet:
    print(flower)

leaves_boquet = ("Maple", "Oak", "Birch", "Pine", "Willow", "Palm", "Eucalyptus", "Magnolia", "Aspen", "Cedar")
print("Leaves we have:")
for leaf in range (len(leaves_boquet)):
    print(leaves_boquet[leaf])