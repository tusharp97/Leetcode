def robber_house(num:list[int]):
    rob1,rob2=0,0
    for n in num:
        temp=max(n+rob1,rob2)
        rob1=rob2
        rob2=temp
    return rob2
print(robber_house([1,2,3,1]))