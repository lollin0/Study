import heapq

def solution(scoville, K):
    heap = []
    for x in scoville:
        heapq.heappush(heap, x)
    count = 0
    
    while heap[0] < K:
        if len(heap) == 1:
            count = -1
            break
        heapq.heappush(heap, (heapq.heappop(heap) + heapq.heappop(heap) * 2))
        count = count + 1
    return count

print(solution([10,2,3,5,7,9,11], 3))


'''
def solution(scoville, K):
    count = 0
    
    scoville.sort(reverse = True)
    while scoville[len(scoville)-1] < K:
        if len(scoville) == 1:
            count = -1
            break
        scoville.append(scoville.pop() + scoville.pop() * 2)
        scoville.sort(reverse = True)
        count = count + 1
        
    return count
'''