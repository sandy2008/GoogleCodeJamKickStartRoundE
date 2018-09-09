import itertools

f = open("B-large.in.txt")
sb = open('output.txt', 'w')
t = int(f.readline())  # read a line with a single integer
for j in range(1, t + 1):
    n, m, p = [int(s) for s in f.readline().split(" ")]  # read a list of integers, 2 in this case
    player = [f.readline().strip() for i in range(n)]
    nogo = [f.readline().strip() for i in range(m)]
    output = 102400000
    testcase = ["".join(seq) for seq in itertools.product("01", repeat=p)]
    for test in testcase:
        if test not in nogo:
            summer = 0
            for thing in player:
                summer += sum(1 for a, b in zip(thing, test) if a != b)
            output = min(output, summer)
            
    
    sb.write("Case #{}: {}\n".format(j, output))