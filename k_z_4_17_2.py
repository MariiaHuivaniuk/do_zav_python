#print('task 1')
#letters=['a', 'b', 'c', 'd']
#letters=letters[int('3'*2)/11]
#print(letters)
# Помилка через те що число вийде не цілим тому не можна визначити індекс

print('task 2')
letters=['a', 'b', 'c', 'd']
print(letters[-1])

print('task 3')
letters=['a', 'b', 'c', 'd']
print(letters[:2])

print('task 4')
letters=[2, 4, 6, 8, 10]
letters[2]='zero'
print(letters)

print('task 6')
metering=[3.14, 'inch', 2.54, 'inch', 'True']
print(metering.index('inch'))

print('task 7')
metering=[3.14, 'inch', 2.54, 'inch', 'True']
metering.append(99)
print(metering)

print('task 8')
metering=[3.14, 'inch', 2.54, 'inch', 'True']
metering.remove('inch')
print(metering)

print('task 9')
metering=[3.14, 'inch', 2.54, 'inch', 'True']
metering.append(99)
print(metering)
metering.insert(2,58)
print(metering)
# лемент append одає елементи тільки у кінець списку, а функція insert додає у конкретне місце
