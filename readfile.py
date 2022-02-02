f = open('file.txt', 'r')
L = f.readlines()
 
count = 0

for line in L:
    count += 1
    print("L{}: {}".format(count, line.strip()))