def solution(gems):
    answer = []
    min_len=100001
    kind=len(set(gems))
    end=0
    dic={gems[0]:1,}
    for start in range(len(gems)):
        while len(dic)<kind and end<len(gems)-1:
            end+=1
            dic[gems[end]] = dic.get(gems[end], 0) + 1
            
        if len(dic)==kind and min_len>end-start:
            min_len=end-start
            answer=[start+1,end+1]
        
        if dic[gems[start]] == 1:
            del dic[gems[start]]
        else:
            dic[gems[start]] -= 1
    
    return answer