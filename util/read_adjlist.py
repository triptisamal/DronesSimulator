def process_each_line(line,edgelist):
    words = line.split()
    for word in words:
        edgelist.append(int(word))


file = open('network_15.txt', 'r')
lines = file.readlines()

for index, line in enumerate(lines):
    print(line.strip())
    edgelist = []
    process_each_line(line.strip(),edgelist)
    print(edgelist[0])
    print('\n')
    for i in range(1,len(edgelist)):
        print(edgelist[i])
    print('\n\n')

file.close()
