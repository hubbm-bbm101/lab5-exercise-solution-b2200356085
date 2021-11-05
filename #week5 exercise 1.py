#week5 exercise1
n = int(input("please write a number: "))
odd_num= 0
even_num=0
for i in range (1, n+1):
    if i%2==0:
        even_num += i
    else:
        odd_num += i
print("average of the even numbers: ", even_num/n)
print("sum of the odd numbers: ", odd_num)
