''' if given string,
  "1"    -1
 "11"    -2
 "111"   -3
 "1111"  -5
 "11111" -8
 as for this
 here : x = count of  given string'''


string = input()
x1 =1
x2 =2
x = len(string)
if x==1:
    print("1")
elif x==2:
    print("2")
else:
    for i in range(0,x-3):
        x1,x2 =x2,x1+x2
    print("count is",x1+x2)
