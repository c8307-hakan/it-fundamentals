#Let's create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.
list1 = []
n1, n2 = 0, 1
while n2 < 56:
  list1.append(n2)
  n1, n2 = n2, n1 + n2
print(f"fibonacci →  ", list1)