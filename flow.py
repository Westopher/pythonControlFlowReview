""" spam = 0
while spam < 5:
    print("spam")
    spam = spam + 1
 """

""" Shift + Option + A  """


""" name = ''
while not name:
    print("Enter your name")
    name = input()
print("how many guests?")
numGuests = int(input())
if numGuests:
    print(f"you have {numGuests} comming")
print("done") """

""" print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i+1) + ')')

while  """

""" for i in range(50,100):
    print(i) """

""" import random

for i in range(10):
    print(random.randint(1,50)) """

import sys

while True:
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + ', type exit instead.')
