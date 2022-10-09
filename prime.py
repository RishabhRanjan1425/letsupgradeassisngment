num = int(input("please enter the number you want to check\n"))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("the number is not prime")
            print(str(i) + " times " + str(num//i) + " is "+ str(num))
            break
        else:
            print("the number is prime")
elif(num == 1):
    print("the number is not prime")
else:
    print('enter a positive value')
