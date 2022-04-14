tc=int(input())

for _ in range(tc):
    n=int(input())
    grades=[list(map(int,input().split())) for _ in range(n)]
    answer=1
    grades.sort()

    grade=grades[0][1]
    for i in range(1,n):
        if grade>grades[i][1]:
            answer+=1
            grade=grades[i][1]
        
    print(answer)