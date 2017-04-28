# Chapter 6 Python Datatypes
# Using python3 instead of 2.7

fruit = 'banana'
for letter in fruit:
    print(letter)

count = 0
for letter in fruit:
    if letter == 'n':
        count = count + 1
    print(count)

'nan' in fruit

if fruit < 'banana':
    print('bananas!')

if fruit == 'banan':
    print('bananas!')

if fruit == 'banana':
    print('bananas!')

if fruit < 'banan':
    print('bananas!')

if fruit > 'banan':
    print('bananas!')

if fruit > 'bann':
    print('bananas!')

print('Hi there'.lower())

frukt = fruit.replace('banana', 'apple')
print(frukt)

frukt.startswith('a')
frukt.startswith('A')
