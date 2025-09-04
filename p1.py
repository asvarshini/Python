#WEIGHT CONVERTER
w =int(input("enter the weight"))
unit  =input("(L)bs o(k)g:")
if unit.upper() =='L':
    converter = w *0.4536
    print(f"you are {converter } in kilos")
else:
    converter = w /0.4536
    print(f"your weight is {converter} in pounds")