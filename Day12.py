# Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....
# Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA". This question was asked in a Facebook interview.

import math

alpha = ['','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
x = int(input())
result = list()

def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele  
    return str1 


if x < 26:
  result.append(alpha[x])
elif x <= 702:
  if x/26 == math.trunc(x / 26):
    result.append(alpha[math.trunc((x-1) / 26)])
    result.append(alpha[26])
  else:
    result.append(alpha[math.trunc(x / 26)])
    result.append(alpha[(x % 26)])


print(listToString(result))
