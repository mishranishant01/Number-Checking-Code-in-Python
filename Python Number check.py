print("*********HELLO USER!******************")
while True:
    print("------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("----[Read The Following Options and Then Choose One]----\n")
    print("--> Press 1 to Check Prime Number.\n\n","--> Press 2 to Check Armstrong Number.\n\n","--> Press 3 to Check Palindrome Number.\n\n","--> Press 4 to Check Strong Number.\n")
    print("--> Press 5 to Exit")

    print("-------------------------------------------------------------------------------------------------------------------------------------------")

    choice=int(input("\nPlease Enter Any One Option: "))

    if choice==1:
        print("\n**Hey! You Have Selected -[To Check Prime Number]**")
        n1=int(input("\nEnter the Number:"))

                                                        
        if n1>1:                                                     #Code For Checking the Prime Number.
            for i in range(2,int(n1/2)+1,1):
                if(n1%i==0):
                    print(n1,"is not a Prime Number")
                    break
            else:
                print(n1,"is a Prime Number" )

    elif choice==2:
        print("\n**Hey! You Have Selected -[To Check Armstrong Number]**")
       
        num=int(input("\nEnter the Number:"))                         #Code For Checking the Armstrong Number

        sum=0
        temp=num
        

        while temp > 0:
            arm = temp % 10
            sum = sum +(arm*arm*arm)
            temp = temp//10
           
        if(sum==num):
            print(num,"is an Armstrong Number")
        else:
            print(num,"is not Armstrong Number")

    elif choice==3:
 
        print("\n**Hey! You Have Selected -[To Check Palindrome Number]**")
                                                                         #Code For Checking the Palindrome Number.
        n=int(input("\nEnter a Number:"))
        start=n
        order=0
        while(n>0):
            r=(n%10)
            order=order*10+r
            n=n//10
        if(start==order):
            print(order,"is Palindrome Number")
        else:
            print(order,"is not Palindrome Number")
            

    elif choice==4:
        print("\n**Hey! You Have Selected -[To Check Strong Number]**")
                                                                             #Code For Checking the Strong Number.
        num=int(input("\nEnter a Number:"))
        sum=0
        temp=num

        while(temp>0):
            fact=1
            rem=temp % 10
            for i in range(1,rem+1):
                fact=fact * i
            sum=sum + fact
            temp=temp//10
        if(sum==num):
            print("\nThe Given Number is Strong Number")
        else:
            print("The Given Number is not Strong Number")

    elif choice==5:
        print(".........Thank You............")
        break
        
    print("\n**** Do You Want To Continue? [Please  Press Y]: Do You Want To Exit? [Please Press N ]**** ")
    contnu=input()
    if(contnu=='n'or contnu=='N'):
        print("alright! Thank You...")
        break
    elif(contnu=='Y' or contnu=='y'):
            continue
    else:
        print("wrong key....Click on Right Button.")
        break
        
    


        


