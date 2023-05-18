import numpy as np 
import sys

number_of_nodes = 64
side = 4
mu = 0
sigma = 0.9
noise = np.random.normal(mu, sigma, [number_of_nodes])
original_stdout = sys.stdout
name = "noise.txt"
with open(name,'a') as f:
    sys.stdout = f
    print(noise)

sys.stdout = original_stdout

print(len(noise))
n = 0
node_loc = [{'x':0, 'y':0, 'z':0} for i in range(0,number_of_nodes+1)]
while n < number_of_nodes:
    for i in range(1,side+1):
        for j in range(1,side+1):
            for k in range(1,side+1):
                node_loc[n]['x'] = i + noise[n]
                node_loc[n]['y'] = j + noise[n]
                node_loc[n]['z'] = k + noise[n]
                n += 1

original_stdout = sys.stdout
name = "network.txt"
with open(name,'a') as f:
    sys.stdout = f
    print(node_loc)

sys.stdout = original_stdout


