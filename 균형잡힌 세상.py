list = [input()for _ in range(8)]
stack_1 = []
stack_2 = []
j = 0

for i in list:
    stack_1.append(i)
    print(i)
    if (stack_1[j] == "("):
        stack_1.append(i)
        if (list.find(")")):
            stack_1.pop()
            print("yes")
        else:
            print("no")
        
    if (stack_2[j] == "["):
        stack_2.append(i)
        if (list.find("]")):
            stack_2.pop()
            print("yes")
        else:
            print("no")
            
    j += 1

if (stack_1 == 0 and stack_2 == 0):
    print("yes")
else:
    print("no")
