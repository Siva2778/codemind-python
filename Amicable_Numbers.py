a=int(input())
b=int(input())
cnta=0
for i in range(1,a):
    if a%i==0:
        cnta+=i
cntb=0   
for i in range (1,b):
    if b%i==0:
        cntb+=i
if cnta==b and cntb==a:
    print("Amicable")
else:
    print("Not Amicable")
