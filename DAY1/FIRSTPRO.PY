#PYTHON PROGRAM TWO SUMS...

list = [5,10,15,20]
k = 30
for i in range(len(list)):
    for j in range(1,len(list)):
        if list[i] + list[j] == k:
            print("True")
        break
 
