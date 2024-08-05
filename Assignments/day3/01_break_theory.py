#break , continue, pass(placeholder)
for i in range(10):
    print(i,end=' ')
    if (i==5):
        break
print("bye")

i=0
while i< 10:
    print(i,end=',')
    i+=1
    if (i==5):
        break
print("bye")

i=0
while i< 10:
    
    i+=1
    if (i==5):
        continue
    print(i,end=' ')    
print("bye")
"""The pass statement is used as a placeholder for future code.
When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
Empty code is not allowed in loops, function definitions, class definitions, or in if statements."""
i=0
while i< 10:
    
    if (i==5):
        pass
    print(i,end=' ')
    i+=1
print("bye")

for i in range(10):
    if (i==5):
        break
    print(i,end=' ')
else:# else will be executed only when we are coming of the loop normally
    print("loop is executed normally")
    
for i in range(10):
    if (i==5):
        continue
    print(i,end=' ')
else:# else will be executed only when we are coming of the loop normally
    print("loop is executed normally")    
