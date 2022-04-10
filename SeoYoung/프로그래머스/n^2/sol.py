def solution(n, left, right):
    answer = []
    
    # 처음부터 1차원 배열 형태로 생각하면
    # index-2*2일때의 index: 0-(0,0) 1-(0,1) 2-(1,0) 3-(1,1) => idx-(idx//n, idx%n)
    # value-2*2일때의 index: 0-(0,0) 1-(0,1) 1-(1,0) 1-(1,1) => value-(l,r)=>value=max(l,r)
    
    for i in range(int(left),int(right+1)):
        l=i%n
        r=i//n
        answer.append(max(l,r)+1)
    
    return answer