'''
Name: Phann  Boon
Date: 9/26/24
Description: Unit 2 Homework 1
'''

print('Problem 1'.center(20,'-'))
print('''
1. Scary horror game
2. Goofy silly game
3. Maze game
''')

print('Problem 2'.center(20,'-'))
print(r'''
                     _______________
                    |,----------.  |\
                    ||           |=| |
                    ||          || | |
                    ||       . _o| | | __
                    |`-----------' |/ /~/
                     ~~~~~~~~~~~~~~~ / /
                                    ~~
''')

print('Problem 2'.center(20,'-'))
distance = 173.8
mpg = float(input("How many miles per gallon does you car get? "))
gallon_cost = float(input("How much doas a gallon of gas cost where you live? "))
hold = float(input("How many gallons of gas does your car hold? "))
needed = distance / mpg
tanks = needed / hold
total_cost = tanks * hold * gallon_cost
print(f"Your total cost to drive from Portland to Seattle is ${total_cost:.2f}")