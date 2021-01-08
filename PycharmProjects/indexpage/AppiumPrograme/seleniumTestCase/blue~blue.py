#coding:utf-8

list = [-20,1,66,21,38,19,-50,99]


length = len(list) - 1
for i in range(length,0,-1):
    for k in range(i):
        if list[k] > list[k+1]:
            list[k+1],list[k] = list[k],list[k+1]
    # if list[i] > list[i + 1]:
    #    list[i+1],list[i] = list[i],list[i+1]

        print(k)
    # print(i)
print(list)
