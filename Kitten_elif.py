age = float(input("How old is the cat? (months) "))
kitten = age <= 6
teen = kitten < age <= 11
adult = teen < age <= 96
senior= adult < age

if kitten:
    print("Price: $250")
elif teen:
    print("price: $200")
elif adult:
    print("Price: $125")
elif senior:
    print("Price: $85")