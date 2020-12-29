prices=[3, 1, 2, 4, 2]

def solution(prices):
    st=[]
    answer = [0]*len(prices)
    
    for i in range(len(prices)):
        if st == []:
            st.append(i)
            continue
        else:
            if prices[i] >= prices[i-1] :
                st.append(i)
            else:
                while prices[i] < prices[i-1] :
                    top = st.pop()
                    answer[top] = i-top
                    if st == []:
                        st.append(i)
                        break
                    top = st.pop()
                    st.append(top)
                    if prices[i] >= prices[top] :
                        st.append(i)
                        break
    top = st.pop()
    st.append(top)
    while st != []:
        n=st.pop()
        answer[n] = top - n
    return answer
print(solution(prices))
