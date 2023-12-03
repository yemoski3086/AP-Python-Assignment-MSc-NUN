cubes = []
for number in range (1,11):
    cube = number ** 3
    cubes.append(cube)
    
for cube in cubes:
    print(cube)
cubes = [number ** 3 for number in range(1, 11)]
print(cubes)        