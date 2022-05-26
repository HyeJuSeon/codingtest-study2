def solution(land):

    for i in range(1,len(land)):
        for j in range(4):
            max_row=[0,-1]
            for k in range(4):
                if j==k: continue
                if max_row[0]<land[i-1][k]:
                    max_row=[land[i-1][k], k]
            land[i][j]+=land[i-1][max_row[1]]
    
    return max(land[len(land)-1])