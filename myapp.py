import random
value1=int(input("please enter an integer:\n"))
value2=int(input("please enter an integer:\n"))
if value1<10 or value2< 10:
    print("please enter an integer grater than 10")

x=random.randint(value1,value2)
print("Your Random Number is:",x,sep='')
