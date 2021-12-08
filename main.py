a,b=int(input("Enter a number whose Inverse to be found:")),int(input("Enter The Field:"))
if b<a:
    print('Field Size is less than given number.')
    exit(0)

a1,a2,a3=1,0,b
b1,b2,b3=0,1,a

while(b3!=1):
    Q=a3//b3
    p,q,r=b1,b2,b3
    b1=a1-Q*b1
    b2=a2-Q*b2
    b3=a3-Q*b3
    a1,a2,a3=p,q,r

    if b3==0:
        print("The Given numbers are not relatively Prime to One another.")
        break

if b3==1:
    print("The Inverse of {} in {} is {}".format(a,b,b2%b))    