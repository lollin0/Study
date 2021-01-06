import sys
k = int(input())
inp = list(map(int, input().split()))
result = list()

for _ in range(k):
    tempnode = list()

    for i in range(len(inp)):
        if i%2 != 1:
            result.append(inp[i])
            tempnode.append(inp[i])
    for temp in tempnode:
        inp.remove(temp)
        
for i in range(0,k):
    temp = list()
    ptemp = ""
    for _ in range(0,2**i):
        temp.append(result.pop())
    for _ in range(len(temp)):
        ptemp = ptemp+str(temp.pop()) + " "
    print(ptemp)

'''
 인덱스가 짝수인 데이터는 그대로!
 for문 들어가기 전까지 result = [1,4,5,7,6,2,3]
