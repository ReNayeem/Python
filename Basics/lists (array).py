# ['Nayeem', 'Ahmed']
print(["Nayeem", "Ahmed"])

# Nayeem
print(["Nayeem", "Ahmed"][0])

# My name Nayeem
print("My name "+ ["Nayeem", "Ahmed"][0])

array1= [2, 1, 3]
# 3
print(len(array1))

array2=["Hello", "World"]
# 2
print(len(array2))

# [1, 2, 3]
print(sorted(array1))

array3= ["2", "1", "3", "a", "A", "B", "C", "b"]
# ['1', '2', '3', 'A', 'B', 'C', 'a', 'b']
print(sorted(array3))

# 2
print(array3[0])

# b
print(array3[-1])

# C
print(array3[-2])

# update last value
array3[-1]= 'B'
# ['2', '1', '3', 'a', 'A', 'B', 'C', 'B']
print(array3)

# print first 3 index values
# ['2', '1', '3']
print(array3[0:3])

# add new value inside the list
array3.append('D')
# ['2', '1', '3', 'a', 'A', 'B', 'C', 'B', 'D']
print(array3)

# add new value to second index
array3.insert(1, 0)
# ['2', 0, '1', '3', 'a', 'A', 'B', 'C', 'B', 'D']
print(array3)

# remove a value by using value name
array3.remove('B')
# because there two same values it removed the first one
# ['2', 0, '1', '3', 'a', 'A', 'C', 'B', 'D']
print(array3)

# 2
# 0
# 1
# 3
# a
# A
# C
# B
# D
for item in array3:
    print(item)

# 2
# 0
# 1
# 3
# a
# A
# C
# B
# D
j = 0
while j < len(array3):
    print(array3[j])
    j = j + 1

# remove all values
array3.clear()
# []
print(array3)

