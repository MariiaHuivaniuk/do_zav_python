print('task1')
names=['Vika', 'Tamara', 'Martina', 'Masha', 'Lukash']
for name in names:
    print(name)

print('task2')
transport=['велосипед', 'авто', 'автобус','мотоцикл']
print('Я хотів би купити '+transport[0])

print('task3')
years_list=[2004, 2005, 2006, 2007, 2008, 2009]
print("Мені 3 рочки було у "+str(years_list[3])+" році")
years_list.append(2022)
print(years_list)
print("У "+str(years_list[-1])+" році мені було 18 ")

print('task4')
things=['wallet', 'mirror', 'umbrella']
print(things[2])
j=things[2].title()
print(j)
print(things[0], things[1], things[2].title())
things[2]=things[2].title()
print(things)
things[2]=things[2].upper()
print(things)
things.pop(-1)
print(things)

print('task5')
languages=['Georgian', 'Estonian', 'Ukrainian']
languages[2]=languages[2].lower()
print(languages)
languages.reverse()
print(languages)
languages[0]=languages[0].title()
print(languages)

print('task6')
hardware=("прінтер", "сканер", "клавіатура", "мишка")
software=['світло', 'сигнал', 'роутер']
software[0]='vfdv'
print(software)

for hardware in hardware:
    print(hardware)
for software in software:
    print(software)
