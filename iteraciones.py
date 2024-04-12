contador_1 =0
contador_2 =0

""" while contador_1 < 10:
    while contador_2 < 5:
        print(contador_1, contador_2)
        contador_2 +=1
    contador_1 += 1
    contador_2 = 0 """

frutas = ['manzana', 'pera', 'mango']
iterador = iter(frutas)
print(iterador)
ab = next(iterador)
for a in frutas:
    print(a)
print(ab)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

""" c= 6
b = iter(c)
print(b) """

x = 0.0
for i in range(10):
    x += 0.1

if x == 1.0:
    print(f'x = {x}')
else:
    print(f'x != {x}')