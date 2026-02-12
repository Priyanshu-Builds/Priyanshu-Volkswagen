conversions = [
    lambda t: t * 1000,
    lambda kg: kg * 1000,
    lambda gm: gm * 1000,
    lambda mg: mg * 0.00000220462
]

tonnes = float(input("Enter weight in tonnes to print the desired output: "))

kg = conversions[0](tonnes)
gm = conversions[1](kg)
mg = conversions[2](gm)
lbs = conversions[3](mg)

print("Weight in kilograms:", kg,"Kg")
print("Weight in grams:", gm,"gm")
print("Weight in milligrams:", mg,"mg")
print("Weight in pounds:", lbs,"lbs")