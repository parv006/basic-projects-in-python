fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))

print(fruits.count('tangerine'))

print(fruits.index('banana'))

print(fruits.index('banana', 4))  # Find next banana starting at position 4

print(fruits.reverse())
fruits

print(fruits.append('grape'))
fruits

print(fruits.sort())
print(fruits)

print(fruits.pop())

squares = [x**2 for x in range(10)]
print(squares)
squares2 = list(map(lambda x: x**2, range(10)))
print(squares2)