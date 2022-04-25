class Node:
    def __init__(self):
        self.remove = False
        self.next = None
        self.prev = None

def solution(n, k, cmd):
    node_rows = [Node() for _ in range(n)]
    
    for i in range(1, n): # 링크드 리스트 초기화
        node_rows[i].prev = node_rows[i-1]
        node_rows[i-1].next = node_rows[i]
    
    cur = node_rows[k]
    del_stack = []
    for c in cmd:
        if c[0] == "U":
            move = int(c[1:])
            for _ in range(move):
                cur = cur.prev # up이니까 이전 노드로

        elif c[0] == "D":
            move = int(c[1:])
            for _ in range(move):
                cur = cur.next

        elif c[0] == "C":
            cur.remove = True
            del_stack.append(cur)
            up = cur.prev # 삭제할 행의 윗 행
            down = cur.next # 삭제할 행의 아래 행
            if up: # 현재 행이 0번째가 아닌 경우
                up.next = down
            if down: # 현재 행이 마지막이 아닌 경우
                down.prev = up
                cur = down
            else: # 마지막 행인 경우 => 윗행 선택
                cur = up # 삭제한 행의 윗행을 현재 행으로
                
        else:
            re_node = del_stack.pop()
            re_node.remove = False # 삭제 행 복구
            up = re_node.prev
            down = re_node.next
            if up:
                up.next = re_node
            if down:
                down.prev = re_node
                
    result = ""
    for node in node_rows:
        if node.remove: result += "X"
        else: result += "O"
        
    return result