import itertools

f = open("1.txt")
sb = open('output.txt', 'w')
t = int(f.readline())  # read a line with a single integer
for j in range(1, t + 1):
	n = int(f.readline())
	bahu = [int(i) for i in f.readline().split()]
	bala =  [int(i) for i in f.readline().split()]
	bahuallshit = [x for x in itertools.combinations(bahu,3)]
				
	sb.write("Case #{}: ".format(j))
	sb.write("%.9f" % prec/362880)