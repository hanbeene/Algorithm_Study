x, y, w, h = map(int, input().split())
min = h-y
if w - x < min:
    min = w - x
if x < min:
    min = x
if y < min:
    min = y
if h - y < min:
    min = h - y
print(min)