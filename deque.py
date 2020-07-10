from collections import deque
n = int(input())
deq = deque()
for _ in range(n):
    com = input().split(" ")
    if com[0] == "append":
        deq.append(int(com[1]))
    elif com[0] == "appendleft":
        deq.appendleft(int(com[1]))
    elif com[0] == "pop":
        deq.pop()
    elif com[0] == "popleft":
        deq.popleft()
print(*deq, sep=" ")
