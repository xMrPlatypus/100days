#Given an array of elements, return the length of the longest subarray where all its elements are distinct.
#For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].

#Subarray/Substring
#A subarray is a contiguous part of array. An array that is inside another array. For example, consider the array [1, 2, 3, 4], There are 10 non-empty sub-arrays. The subarrays are (1), (2), (3), (4), (1,2), (2,3), (3,4), (1,2,3), (2,3,4) and (1,2,3,4). In general, for an array/string of size n, there are n*(n+1)/2 non-empty subarrays/substrings.

myArray = [5, 1, 3, 5, 2, 3, 4, 1]

result = set()
for x in myArray:
  result.add(x)
  
  
print(len(result))
print(result)


