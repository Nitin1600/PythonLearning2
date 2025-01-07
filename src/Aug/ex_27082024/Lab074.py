def make_pizza(*toppings, base):
    print(toppings, base)

def make_pizza2(*toppings, base):
    print(base, toppings)

make_pizza("tomato", "potato", base="thin crust")
make_pizza("dsda", "dsda", base="crust")