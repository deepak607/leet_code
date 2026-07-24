def self_dev(left,right):
    my_list=[]
    for i in range(left,right+1):
        num=i
        flag=True
        while num>0:
            temp=num%10
            if temp==0:
                flag=False
                break
            elif i%temp!=0:
                flag=False 
                break
            num//=10
        if flag: 
            my_list.append(i)
    return my_list