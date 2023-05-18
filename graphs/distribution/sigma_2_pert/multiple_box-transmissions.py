# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Creating dataset
np.random.seed(10)
data1 = []
with open("petal_numberofbcast_27_0.400000_1.txt", "r") as f:
    for line in f:
        line = line.strip()
        data1.append(int(line))

arr1=np.array(data1)
# finding the 1st quartile
q1 = np.quantile(arr1, 0.25)
# finding the 3rd quartile
q3 = np.quantile(arr1, 0.75)
med = np.median(arr1)
# finding the iqr region
iqr = q3-q1
# finding upper and lower whiskers
upper_bound = q3+(1.5*iqr)
lower_bound = q1-(1.5*iqr)
print(iqr, upper_bound, lower_bound)


outliers = arr1[(arr1 <= lower_bound) | (arr1 >= upper_bound)]
print('The following are the outliers in the boxplot:',format(outliers))


data2 = []
with open("petal_numberofbcast_64_0.400000_1.txt", "r") as f:
    for line in f:
        line = line.strip()
        data2.append(int(line))
arr2=np.array(data2)
# finding the 1st quartile
q1 = np.quantile(arr2, 0.25)
# finding the 3rd quartile
q3 = np.quantile(arr2, 0.75)
med = np.median(arr2)
# finding the iqr region
iqr = q3-q1
# finding upper and lower whiskers
upper_bound = q3+(1.5*iqr)
lower_bound = q1-(1.5*iqr)
print(iqr, upper_bound, lower_bound)


outliers2 = arr2[(arr2 <= lower_bound) | (arr2 >= upper_bound)]
print('The following are the outliers in the boxplot:',format(outliers2))


data3 = []
with open("petal_numberofbcast_125_0.400000_1.txt", "r") as f:
    for line in f:
        line = line.strip()
        data3.append(int(line))
arr3=np.array(data3)
# finding the 1st quartile
q1 = np.quantile(arr3, 0.25)
# finding the 3rd quartile
q3 = np.quantile(arr3, 0.75)
med = np.median(arr3)
# finding the iqr region
iqr = q3-q1
# finding upper and lower whiskers
upper_bound = q3+(1.5*iqr)
lower_bound = q1-(1.5*iqr)
print(iqr, upper_bound, lower_bound)


outliers3 = arr3[(arr3 <= lower_bound) | (arr3 >= upper_bound)]
print('The following are the outliers in the boxplot:',format(outliers3))


data4 = []
with open("petal_numberofbcast_216_0.400000_1.txt", "r") as f:
    for line in f:
        line = line.strip()
        data4.append(int(line))
arr4=np.array(data4)
# finding the 1st quartile
q1 = np.quantile(arr4, 0.25)
# finding the 3rd quartile
q3 = np.quantile(arr4, 0.75)
med = np.median(arr4)
# finding the iqr region
iqr = q3-q1
# finding upper and lower whiskers
upper_bound = q3+(1.5*iqr)
lower_bound = q1-(1.5*iqr)
print(iqr, upper_bound, lower_bound)


outliers4 = arr4[(arr4 <= lower_bound) | (arr4 >= upper_bound)]
print('The following are the outliers in the boxplot:',format(outliers4))


data5 = []
with open("petal_numberofbcast_343_0.4_1.txt", "r") as f:
    for line in f:
        line = line.strip()
        data5.append(int(line))
arr5=np.array(data5)
# finding the 1st quartile
q1 = np.quantile(arr5, 0.25)
# finding the 3rd quartile
q3 = np.quantile(arr5, 0.75)
med = np.median(arr5)
# finding the iqr region
iqr = q3-q1
# finding upper and lower whiskers
upper_bound = q3+(1.5*iqr)
lower_bound = q1-(1.5*iqr)
print(iqr, upper_bound, lower_bound)


outliers5 = arr5[(arr5 <= lower_bound) | (arr5 >= upper_bound)]
print('The following are the outliers in the boxplot:',format(outliers5))



data = np.array([arr1,arr2,arr3,arr4,arr5]) 
data = data.transpose()
df = pd.DataFrame(data, columns = ['27','64','125','216','343'])
#print(df)
fig = plt.figure()

plt.title('Perturbed Lattice, Petal Eccentricity = 0.4, source-destination distance ~ 75 feet, 500 iterations, 99 % CI', wrap=True,fontsize=15)

plt.suptitle('With fixed source-destination distance',fontsize=18, wrap=True)
plt.subplots_adjust(top=0.85)

plt.xlabel("Number of Nodes",fontsize=15)
plt.ylabel("Number of Transmissions",fontsize=15)
df.boxplot(showmeans=True)
plt.show()
fig.savefig('box_petal.png',
            format='png',
            dpi=100,
            bbox_inches='tight')
