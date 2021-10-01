num=int(input("Enter the number: "))
base=int(input("Base(2-9): "))
if not(2<= base <=9):
    quit()
newNum =' '
while num>0:
    newNum = str(num%base)+ newNum
    num//=base
print(newNum)
