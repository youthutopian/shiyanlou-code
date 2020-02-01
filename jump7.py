for value in range(1,101):
    if value%7!=0 and value-int(value/10)*10!=7 and int(value/10)!=7:
        print("{}".format(value))
