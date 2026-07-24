def perfect(num):
    sum=1
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            sum+=i
            pair=num/i
            if pair!=i:
                sum+=pair
    return num==sum
if perfect(6):
    print("yes")
else:
    print("not")