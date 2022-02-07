x = True
y = False
z = bool("")
print(z)

# not - логічне "не"
z = not x 
print(z)
z = not y
print(z)

# and логічне "і"
z = x and y
print(z)
z = True and True
print(z)
z = False and True
print(z)
z = False and False
print(z)

# or логічне "або"
z = True or True
print(z)
z = True or False
print(z)
z = False or False
print(z)

print(z or y and (x and y))