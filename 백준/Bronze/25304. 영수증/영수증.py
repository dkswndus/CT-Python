X = int(input())
N = int(input())
total_list = []
hap = 0
for i in range(1,N+1):
    a,b = map(int, input().strip().split())
    hap += a * b
 
if X == hap:
    print("Yes")
else:
    print("No")