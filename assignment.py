#Write a program to print a right-angled number triangle pattern based on the user input n

#answer
""""
a=int(input("Enter the number of rows:"))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

"""

#Question

"""
Write a function that compresses consecutive repeating characters but only if the
count > 2.
Example:
Input : "aaabbccccd"
Output : "a3bb c4d"
"""
"""
def compress(s):
    abc= ""
    count=1

    for i in range(1,len(s)+1):
        if i<len(s)and[i]==s[i-1]:
            count +=1
        else:
            if count>2:
                abc+= s[i-1]+str(count)
            else:
                abc+=s[i-1]*count
            count=1
    return abc
print(compress("aaabbccccd"))
"""

#QUESTION:
"""
Rearrange String So Adjacent Characters Are Different
Question
Rearrange characters so no adjacent characters are the same.
Example
Input
aaabbc
Possible Output
ababac
"""
"""
from collections import Counter

def rearrange(s):
    count =Counter(s)
    result = ""
    while len(result)<len(s):
        for i in count:
            if count[i]>0 and(not result or result[-1]!=i):
                result+=i
                count[i]-=1
                break
    return result
print(rearrange("aaabbc"))
"""
#question
"""
Find word with highest number of repeated letters in string
Problem Statement: Write a program to find a word in a given string that has
the highest number of repeated letters. If not found, return -1.
Examples
Example 1:Input: string = "abcdefghij google microsoft"
Output: google
Explanation:
In “google”, the letter g appears 2 times, and o appears 2
times — which is the highest frequency of any letter among
all words.
Example 2:Input: string = "cameron blue"
Output: -1
Explanation:
No word has any letter that repeats. Hence, return -1.
"""
"""
s = "abcdefghij google microsoft"
words=s.split()
result =-1
max_repeat=1
for i in words:
    for j in i:
        count=i.count(j)
        if count>max_repeat:
            max_repeat=count
            result=i
print(result)
"""