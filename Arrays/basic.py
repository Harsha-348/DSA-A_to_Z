# 1. Declare and Print an Array
print("1. Declare and Print an Array")
arr1 = [1, 2, 3, 4, 5]
print("Array:", arr1)

# 2. Input and Output Elements of an Array
print("\n2. Input and Output Elements of an Array")
arr2 = []
n = int(input("Enter number of elements: "))
for i in range(n):
    arr2.append(int(input(f"Enter element {i+1}: ")))
print("Array elements:", arr2)

# 3. Find the Sum of Elements in an Array
print("\n3. Sum of Elements")
print("Sum:", sum(arr2))

# 4. Find the Average of Elements
print("\n4. Average of Elements")
print("Average:", sum(arr2) / len(arr2))

# 5. Find the Maximum Element
print("\n5. Maximum Element")
print("Maximum:", max(arr2))

# 6. Find the Minimum Element
print("\n6. Minimum Element")
print("Minimum:", min(arr2))

# 7. Count Even and Odd Numbers
print("\n7. Count Even and Odd Numbers")
even = odd = 0
for num in arr2:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even, "Odd:", odd)

# 8. Print Elements at Even Indices
print("\n8. Elements at Even Indices")
for i in range(0, len(arr2), 2):
    print(arr2[i], end=' ')
print()

# 9. Print Elements at Odd Indices
print("\n9. Elements at Odd Indices")
for i in range(1, len(arr2), 2):
    print(arr2[i], end=' ')
print()

# 10. Count Positive and Negative Numbers
print("\n10. Count Positive and Negative Numbers")
pos = neg = 0
for num in arr2:
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
print("Positive:", pos, "Negative:", neg)

# 11. Replace All Negative Numbers with Zero
print("\n11. Replace All Negative Numbers with Zero")
arr11 = arr2.copy()
for i in range(len(arr11)):
    if arr11[i] < 0:
        arr11[i] = 0
print("Updated Array:", arr11)

# 12. Search an Element (Linear Search)
print("\n12. Search an Element (Linear Search)")
target = int(input("Enter number to search: "))
found = False
for num in arr2:
    if num == target:
        found = True
        break
print("Element found" if found else "Element not found")

# 13. Copy an Array
print("\n13. Copy an Array")
copy_arr = arr2.copy()
print("Copied array:", copy_arr)

# 14. Reverse an Array
print("\n14. Reverse an Array")
reversed_arr = arr2.copy()
reversed_arr.reverse()
print("Reversed array:", reversed_arr)

# 15. Swap First and Last Elements
print("\n15. Swap First and Last Elements")
arr15 = arr2.copy()
arr15[0], arr15[-1] = arr15[-1], arr15[0]
print("Swapped array:", arr15)

# 16. Print Array in Reverse Order
print("\n16. Print Array in Reverse Order")
for i in range(len(arr2)-1, -1, -1):
    print(arr2[i], end=' ')
print()

# 17. Count Frequency of a Given Number
print("\n17. Count Frequency of a Number")
num_to_count = int(input("Enter number to count: "))
print(f"Frequency of {num_to_count}:", arr2.count(num_to_count))

# 18. Find Index of a Specific Element
print("\n18. Find Index of a Specific Element")
num_to_find = int(input("Enter number to find index: "))
if num_to_find in arr2:
    print("Index:", arr2.index(num_to_find))
else:
    print("Element not found")

# 19. Replace All Even Numbers with -1
print("\n19. Replace All Even Numbers with -1")
arr19 = arr2.copy()
for i in range(len(arr19)):
    if arr19[i] % 2 == 0:
        arr19[i] = -1
print("Updated array:", arr19)

# 20. Multiply All Elements of the Array
print("\n20. Multiply All Elements of the Array")
product = 1
for num in arr2:
    product *= num
print("Product of all elements:", product)
