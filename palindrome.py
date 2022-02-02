num=input("Enter a number")
num=int(num)

temp=num
reverse=0

while (num>0):
    last=num%10
    reverse=reverse*10+last
    num=num//10

print(reverse)

if temp==reverse:
    print("No is palindrome")

else:
    print("No. is not palindrome")