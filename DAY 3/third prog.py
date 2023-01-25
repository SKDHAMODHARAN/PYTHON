list=[]
list1=[]
n=int(input("Enter a Number:"))
for i in range(n):
    x=int(input())
    list.append(x)
for i in range (1,len(list)+1):
    list1.append(i)
for i in list1:
    if i not in list:
        if i<0:
            continue
        else:
          print(i)

------------------------
output:

=========
Enter a Number:3
0
2
1
[0, 2, 1]
[1, 2, 3]
3
