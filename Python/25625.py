x, y = map(int, input().split())

if x > y:
    print(x+y)
elif x < y:
    print(y-x)
else:
    print("다시 입력해주세요.")
