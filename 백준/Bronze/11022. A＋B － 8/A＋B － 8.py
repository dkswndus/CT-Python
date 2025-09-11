num = int(input())
for i in range(num):
    i += 1
    a,b = map(int, input().strip().split())
    print("Case #{}: {} + {} = {}".format(i,a,b,a+b))