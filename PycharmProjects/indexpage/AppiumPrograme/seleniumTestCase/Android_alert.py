#coding:utf-8

######9*9表格

# for i in range(10):
#     for k in range(1,i+1):
#         print(str(k)+"*"+str(i)+'     ',end='',)
#     print('')


####for yield Fun

def iam_yield():
    for i in range(3):
        yield i
        print("iam you fucking father")


def run_yield():
    iam_yield()
c = iam_yield()
print(run_yield())
print(run_yield())
print(run_yield())

