hap = 0
hap_list = []
case = int(input())
for i in range(1,case+1):
    a,b = map(int, input().strip().split())
    hap = a + b
    hap_list.append(hap)
   

for j in hap_list:
    print(j)