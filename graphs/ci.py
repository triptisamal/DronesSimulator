import numpy as np
import scipy.stats as st

# define sample data
data1 = []
with open("petal_numberofbcast_64_0.400000_1.txt", "r") as f:
    for line in f:
        line = line.strip()
        data1.append(int(line))

gfg_data=np.array(data1)
#gfg_data = [1, 1, 1, 2, 2, 2, 3, 3, 3,
#			3, 3, 4, 4, 5, 5, 5, 6,
#			7, 8, 10]

# create 99% confidence interval
print(np.mean(gfg_data))
#tup=st.norm.interval(confidence=0.99, 
 #                loc=np.mean(gfg_data),
  #               scale=st.sem(gfg_data))
tup=st.norm.interval(confidence=0.99, 
                 loc=np.mean(gfg_data),
                 scale=np.std(gfg_data)/np.sqrt(len(gfg_data)))

print(tup)
print(tup[0])
print(np.mean(gfg_data)-tup[0])
