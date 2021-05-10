liste = []
for i in range(1, 101):
  if i % 15 == 0:
    liste.append("FizzBuzz")
  elif i % 3 == 0:
    liste.append("Fizz")
  elif i % 5 == 0:
    liste.append("Buzz")
  else:
    liste.append(i)
print(liste)