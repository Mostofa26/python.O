amount = int(input("enter sale price: "))
if(amount>0):
    if amount >=100:
        dis = amount*0.10
    elif amount <100:
        dis = amount*0.05
    print("discount :",dis)
    print("net pay : ",amount-dis)
else:
    print("invalid amount")