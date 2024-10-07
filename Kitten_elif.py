import time
age = float(input("How old is the cat? (months) "))
kitten = age <= 6
teen = 7 < age <= 11
adult = 12 < age <= 96
senior = 97 < age < 336
dead = 337 < age

print('Approach 1'.center(20,'-'))
if kitten:
    print("Price: $250")
elif teen:
    print("price: $200")
elif adult:
    print("Price: $125")
elif senior:
    print("Price: $85")
elif dead:
    print("Dead")

time.sleep(1)
print('Approach 2'.center(20,'-'))
if senior:
    print("Price: $85")
elif adult:
    print("price: $125")
elif teen:
    print("Price: $200")
elif kitten:
    print("Price: $250")
elif dead:
    print("Dead")

time.sleep(1)
print('Approach 3'.center(20,'-'))
if kitten:
    print("Price: $250")
if teen:
    print("price: $200")
if adult:
    print("Price: $125")
if senior:
    print("Price: $85")
if dead:
    print("Dead")

time.sleep(1)
print('Approach 4'.center(20,'-'))
if senior:
    print("Price: $85")
if adult:
    print("price: $125")
if teen:
    print("Price: $200")
if kitten:
    print("Price: $250")
if dead:
    print("Dead")