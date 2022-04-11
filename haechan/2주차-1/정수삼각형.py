'''프로그래머스 - 정수 삼각형
         
         [0, 7, 0]
      [0, 10, 15, 0]
    [0, 18, 16, 15, 0]
  [0, 20, 25, 20, 19, 0]
[0, 24, 30, 27, 26, 24, 0]
'''

def solution(triangle):
    
    for i in range(1, len(triangle)):
        before_list = [0] + triangle[i-1] + [0]

        # 왼쪽 가장자리
        left = triangle[i][0] + before_list[1]
        
        # 오른쪽 가장자리
        right = triangle[i][-1] + before_list[-2]
        
        # 가운데 나머지들
        for j in range(1, len(triangle[i])):
            # 값이 최대가 되는 루트로 가야되므로 두 수 중 큰 값을 더한다.
            triangle[i][j] += max(before_list[j], before_list[j+1])

        triangle[i] = [left]+ triangle[i][1:-1] + [right] # 해당 층 갱신
    
    total_max = max(triangle[-1]) # 가장 아래 층의 리스트 중 가장 큰 값 리턴
           
    return total_max