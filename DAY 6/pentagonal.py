num= int(input())
def pentagonal(num):
    dots=1
    angle =5 # pentagon so angle =5
    for i in range(num):
        dots=dots+angle*i
    print(dots)
    return num
pentagonal(num)

---------------------------
output:
---------------------------
6
76
