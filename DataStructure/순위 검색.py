def solution(info, query):
    answer = []
    infoSlice = []
    querySlice = []
    for x in info:
        infoSlice.append(x.split(' '))
    for x in query:
        querySlice.append(x.split(' '))
        
        
    for i in querySlice:
        count = 0
        # i = ['java', 'and', 'backend', 'and', 'junior', 'and', 'pizza', '100']
        for x in infoSlice:
            # x = ['java', 'backend', 'junior', 'pizza', '150']
            temp = 0
            for index in range(0, 4):
                if x[index] == i[index*2]:
                    # 언어 or 직군 or 경력 or 소울푸드가 일치할 때
                    continue
                elif i[index*2] == '-':
                    # 조건이 없을 때
                    #print("continue 된 조건", i)
                    continue
                else:
                    temp = 1
                    break
            if temp == 0:
                if int(x[4]) >= int(i[7]):
                    print("조건", i)
                    print("합격", x, "\n")
                    count += 1
                else:
                    break               
        answer.append(count)
    
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], 
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"] ))