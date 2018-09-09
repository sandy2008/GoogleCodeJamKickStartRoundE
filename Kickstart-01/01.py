f = open("A-small-attempt1.in.txt")
sb = open('output.txt', 'w')
t = int(f.readline())  # read a line with a single integer
for j in range(1, t + 1):
  n, k = [int(s) for s in f.readline().split(" ")]  # read a list of integers, 2 in this case
  a = [int(i) for i in f.readline().split()]
  a = sorted(a)
  output = 0
  daycount = 1
  now = 0
  for i in a:
  	if i >= daycount and now < k:
  		output += 1
  		now += 1
  	if now >= k:
  		now = 0
  		daycount += 1
  		
  sb.write("Case #{}: {}\n".format(j, output))
  # check out .format's specification for more formatting options