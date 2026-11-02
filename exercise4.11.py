pizzas = ["pepperoni", "mushroom", "pineapple"]
friends_pizzas = pizzas[:]
pizzas.append("jamur")
friends_pizzas.append("sosis")
print("Pizza favorit saya adalah:")
for pizza in pizzas:
    print(pizza) 
print("Pizza favorit teman saya adalah:")
for pizza in friends_pizzas:
    print(pizza)