import matplotlib.pyplot as plt
y = []
# Using readlines()
file1 = open('total_connection_inside_with_0.700000.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    num = int(line.strip())
    y.append(num)

plt.plot(y)
plt.show()
