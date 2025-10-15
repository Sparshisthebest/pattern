#fluids triangle
row=int(input("please enter the number of rows: "))
numb=1
print("floyds triangle")
for i in range(1,row+1):
    for j in range(1,i+1):
        print(numb,end = " ")
        numb=numb+1
    print()