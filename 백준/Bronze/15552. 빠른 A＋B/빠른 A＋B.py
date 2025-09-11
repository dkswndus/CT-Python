from sys import*
hap = 0
input_count = int(stdin.readline().rstrip())
for i in range (input_count):
    line = stdin.readline().rstrip().split()
    a = int(line[0])
    b = int(line[1])
    hap = a+b
    print(a+b)