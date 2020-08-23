from collections import deque

MAX = 10000

def bfs(goal):
    q = deque()
    # (현재 화면의 이모티콘, 클립보드에 있는 이모티콘, time)
    q.append((1, 0, 0))

    check = [[False] * MAX for _ in range(MAX)]
    check[1][0] = True

    while q:
        display_emoticon, clipboard, time = q.popleft()
        if display_emoticon == goal:
            return time
        for next_display_emoticon, next_clipboard, next_time in [
            (display_emoticon, display_emoticon, time + 1),
            (display_emoticon + clipboard, clipboard, time + 1),
            (display_emoticon - 1, clipboard, time + 1)
        ]:
            if 0 <= display_emoticon <= MAX:
                if check[next_display_emoticon][next_clipboard] == 0:
                    q.append((next_display_emoticon, next_clipboard, next_time))
                    check[next_display_emoticon][next_clipboard] = True
    return

def solution():
    goal = int(input())
    print(bfs(goal))

solution()