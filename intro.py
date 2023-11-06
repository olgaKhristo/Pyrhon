
my_cat = 'Oreo'

# // cant change the value of a variable
MY_OTHER_CAT = 'Pumpkin'

# // indentaiton matters - one tap
def my_function():
    print('hello world')

my_function()

def add_together (a, b):
    return a + b
    print (add_together
    (1, 2))

#LISTS
shop_list = ['apple', 'banana', 'orange']
num =   [1, 2, 3, 4, 5]
mixed = ['apple', 1, 'banana', 2, 'orange', 3, [1, 2, 3]]

#  TUPLES (inmutebel)
my_fruits = ('apple', 'banana', 'orange')

# SET (unique values)
my_fruits = {'apple', 'banana', 'orange', 'apple'}
my_other_set = {'apple', 'banana', 'orange', 'apple'}

# DICTIONARY (key value pairs)
my_fruits = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}
print(shop_list[0])
print(my_fruits['apple'])

# FOR LOOP
# for(i=0; i<10; i++){
   
# }
#  for i in mixed(10):
#      print(i)
# num = 5
# if number > 10:
#     print('greater than 10')
# elif number < 10:
#     print('less than 10')
# else:
#     print('equal to 10')


# language = 'javascript'
# match language:
#     case 'python':
#     print('python')
#     case 'javascript':
#     print('javascript')
#     case _:
#     print('default case')


#LOOPS
animals = ['cat', 'dog', 'bird']
for animal in animals:
    print(animal)
    if animal == 'dog':
        break

floor = 1
while floor <= 10:
    print(floor)
    floor += 1


#without walrus operator
while True:
    line = input()
    if not line:
        break
    print(line)

# := // walrus operator
while (line := input()) :
    print(line)

# // walrus operator
items = []
while (value := input('Enter a value:')) :
    items.append(value)





