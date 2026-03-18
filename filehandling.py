#opening a file
'''
file=open("python.txt","r")
#reading files
content=file.read()
print(content)
line1=file.readline()
print(line1)
file.close()
'''
#write in to files
'''
file=open("python.txt","w")
file.write("abc")
file=open("python.txt","r")
content=file.read()
print(content)
'''
#appending to a file
'''
file=open("python.txt","a")
file.write("abcdefg")

file=open("python.txt","r")
content=file.read()
print(content)
file.close()
'''
#closeing file using  WITH statement
'''
with open("python.txt","r") as file:
    content=file.read()
    print(content)

file.write("adith")  # automatically  file is closed.so that we cant do i/o operations further

'''
#open with WITH statement and read and write
''' 
with open("python.txt","w") as file:
    file.write("abc")

with open("python.txt","r") as file:
    content=file.read()
    print(content)    

    '''
#file handling exception
try:
 file=open("pyth.txt","r")
 content=file.read()
 print(content)

except FileNotFoundError:
 print("file not found")
#OR
except Exception as e:
 print(e)
  
  
