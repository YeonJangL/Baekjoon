N = int(input())
arr = list(input())
stack = []

for i in arr:
    if i == "(":
        stack.append(i)
        if arr.find(")"):
            stack.pop()
            print("Yes")
    else:
        print("No")