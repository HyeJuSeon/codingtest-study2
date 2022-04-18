## 풀이

## 코드

```from collections import Counter
import math

def solution(str1, str2):
    answer = 0
    
    #2개씩 끊으면서 공백,숫자,특수문자 포함 글자쌍은 버리고 나머지는 리스트로 정리
    str1_list = [str1[i].upper()+str1[i+1].upper() for i in range(len(str1)-1) 
                 if check_alpha(str1[i]) and check_alpha(str1[i+1])]
    str2_list = [str2[i].upper()+str2[i+1].upper() for i in range(len(str2)-1) 
                 if check_alpha(str2[i]) and check_alpha(str2[i+1])]
    
    #교집합, 합집합
    inter_set = set(str1_list).intersection(set(str2_list))
    outer_set = set(str1_list).union(set(str2_list))
    
    #집합 A와 집합 B가 모두 공집합일 경우
    if(len(inter_set) == 0 and len(outer_set) == 0):
        return 65536
    
    #Counter 함수로 갯수 정리
    str1_count = dict(Counter(str1_list))
    str2_count = dict(Counter(str2_list))

    #자카드 유사도 계산
    inter_num = 0
    outer_num = 0
    for i in inter_set:
        inter_num += min(str1_count[i],str2_count[i])
    for o in outer_set:
        if o not in str1_count.keys():
            outer_num += str2_count[o]
        elif o not in str2_count.keys():
            outer_num += str1_count[o]
        else:
            outer_num += max(str1_count[o],str2_count[o])
    
    answer = math.floor(inter_num/outer_num*65536)
    return answer

    #아스키 코드 활용
    #A:65 a:97
def check_alpha(s):
    if 65 <= ord(s) <= 90 or 97 <= ord(s) <= 122:
        return True
    else:
        return False

```





