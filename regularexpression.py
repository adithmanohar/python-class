import re
"""
text="hello 123,welcome 456!"
abc=re.sub(r"\d","number",text)
print(abc)


#Example:

pattern = r"\d" # Matches any digit
text = "There are 3 apples and 5 oranges."
matches = re.findall(pattern, text)
print(matches) # Output: ['3', '5']


#re.match(): Matches the pattern only at the beginning of the string.

text = "Hello world"
match = re.match(r"Hello",text)
print(match) # Output: <re.Match object>

#re.search(): Searches for the pattern throughout the string
text = "Hello world"
match = re.search(r"world",text)
print(match) # Output: <re.Match object>

#re.findall() : Returns all matches of the pattern as a list
text = "The price is 45 dollars, 30 cents, and 50 rupees."
numbers = re.findall(r"\d+",text)
print(numbers) # Output: ['45', '30', '50']

 #re.sub(): Replaces occurrences of a pattern with a specified string.

text = "Hello 123, welcome 456!"
new_text = re.sub(r"\d+", "number", text)
print(new_text) # Output: "Hello number, welcome number!"

#re.split(): Splits the string wherever the pattern is found.

text = "apple, orange; banana, grape"
fruits = re.split(r"[;,]", text)
print(fruits) # Output: ['apple','orange','banana','grape']

#Grouping and Capturing--  You can use parentheses () to create groups in regular expressions

text = "John:34, Alice:45, Bob:23"
matches = re.findall(r"(\w+):(\d+)",text)
print(matches) # Output: [('John','34'), ('Alice','45'), ('Bob','23')]

#Compiling Regular Expressions: You can compile regular expressions using the re.compile().This is useful for reusing the same pattern multiple times.

pattern = re.compile(r"\d+")
text = "123 apples and 456 oranges"
matches = pattern.findall(text)
print(matches) # Output: ['123', '456']

"""
#Flags in Regular Expressions

#re.IGNORECASE (or re.I): Ignore case while matching

text = "HELLO world"
match = re.search(r"hello", text, re.IGNORECASE)
print(match) # Output: <re.Match object>

#re.MULTILINE (or re.M): Treat each line in a string as aseparate string.

import re

text = """Hello world
Hi there
Hello again"""
matches = re.findall(r"^Hello", text, re.MULTILINE)
print(matches)

#re.DOTALL (or re.S): Make the dot (.) match all characters,including newline.

import re

text = "Hello\nWorld"
print(re.search("Hello.World", text, re.DOTALL))  # ✅ Match