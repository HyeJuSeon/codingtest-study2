def get_binary_cnt_one(num):
    cnt = 0
    while num >= 2:
        num, rest = divmod(num, 2)
        cnt += rest
    cnt += num
    
    return cnt

def solution(n):
    n_one_cnt = get_binary_cnt_one(n)
    
    while True:
        n += 1
        now_one_cnt = get_binary_cnt_one(n)
        if n_one_cnt == now_one_cnt:
            break
            
    return n