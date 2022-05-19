def solution(gems):
    gemSet = set()
    for gem in gems:
        if gem not in gemSet:
            gemSet.add(gem)
    kinds = len(gemSet)

    gemDict = {gems[0]: 1}
    answer = [1, len(gems)]
    left = 0;
    right = 0
    while left <= right and right < len(gems):
        if len(gemDict) == kinds:
            if answer[1] - answer[0] > right - left:
                answer = [left + 1, right + 1]

            gemDict[gems[left]] -= 1
            if gemDict[gems[left]] == 0:
                del gemDict[gems[left]]
            left += 1

        elif len(gemDict) < kinds:
            right += 1
            if right >= len(gems):
                break

            if gems[right] not in gemDict:
                gemDict[gems[right]] = 1
            else:
                gemDict[gems[right]] += 1

    return answer

'''
gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
gems = ["XYZ", "XYZ", "XYZ"]
gems = ["AA", "AB", "AC", "AA", "AC"]
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]




시간초과
def solution(gems):
    gems_set = set(gems)
    min_len = len(gems_set)
    for i in range(min_len,len(gems)+1):
        for j in range(len(gems)-min_len+1):
            if gems_set == set(gems[j:i+j]):
                answer = [j+1,i+j]
                return answer
'''