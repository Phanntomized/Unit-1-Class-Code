ingredient1 = input("Enter ingredient 1: ")
ounces1 = float(input(f"Ounces of {ingredient1}: "))
ingredient2 = input("Enter ingredient 2: ")
ounces2 = float(input(f"Ounces of {ingredient2}: "))
ingredient3 = input("Enter ingredient 3: ")
ounces3 = float(input(f"Ounces of {ingredient3}: "))
servings = float(input("Number of servings: "))
total1 = servings * ounces1
total2 = servings * ounces2
total3 = servings * ounces3
print(f"Total ounces of {ingredient1}: {total1}")
print(f"Total ounces of {ingredient2}: {total2}")
print(f"Total ounces of {ingredient3}: {total3}")