def solution(clothes):
    clothesKindSet = set()
    answer = 1

    for i in range(len(clothes)):
        clothesKindSet.add(clothes[i][1])
    
    num = len(clothesKindSet)
    
    for i in clothesKindSet:
        count = 0
        for j in range(len(clothes)):
            if clothes[j][1] == i:
                count += 1
            
        answer = answer * (count + 1)
        print(answer)
    
    return answer-1

print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))