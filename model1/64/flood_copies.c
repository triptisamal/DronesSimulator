#include<stdio.h>
#include<math.h>
#define TOTAL 500

int main(){

	int sum = 0;

	int arr[TOTAL]={10 ,
6 ,
10 ,
5 ,
13 ,
6 ,
11 ,
7 ,
13 ,
12 ,
6 ,
9 ,
6 ,
4 ,
17 ,
7 ,
11 ,
10 ,
6 ,
8 ,
11 ,
12 ,
6 ,
3 ,
4 ,
7 ,
9 ,
11 ,
7 ,
7 ,
12 ,
8 ,
13 ,
10 ,
6 ,
6 ,
6 ,
8 ,
10 ,
9 ,
7 ,
7 ,
5 ,
10 ,
15 ,
3 ,
12 ,
11 ,
5 ,
7 ,
13 ,
13 ,
8 ,
11 ,
16 ,
10 ,
15 ,
8 ,
17 ,
9 ,
6 ,
13 ,
7 ,
8 ,
16 ,
10 ,
10 ,
17 ,
15 ,
6 ,
16 ,
13 ,
6 ,
7 ,
12 ,
8 ,
6 ,
7 ,
11 ,
11 ,
6 ,
15 ,
6 ,
13 ,
12 ,
4 ,
6 ,
9 ,
7 ,
5 ,
11 ,
5 ,
11 ,
11 ,
13 ,
5 ,
12 ,
9 ,
13 ,
15 ,
7 ,
11 ,
9 ,
5 ,
6 ,
4 ,
10 ,
6 ,
7 ,
9 ,
7 ,
11 ,
7 ,
7 ,
11 ,
11 ,
12 ,
5 ,
8 ,
8 ,
13 ,
7 ,
3 ,
8 ,
12 ,
9 ,
14 ,
13 ,
7 ,
5 ,
6 ,
11 ,
8 ,
9 ,
9 ,
16 ,
9 ,
14 ,
9 ,
7 ,
5 ,
10 ,
8 ,
16 ,
9 ,
6 ,
11 ,
5 ,
8 ,
5 ,
6 ,
6 ,
11 ,
7 ,
8 ,
3 ,
8 ,
11 ,
9 ,
6 ,
12 ,
16 ,
14 ,
17 ,
5 ,
7 ,
10 ,
11 ,
9 ,
12 ,
9 ,
13 ,
6 ,
7 ,
6 ,
5 ,
7 ,
5 ,
16 ,
8 ,
15 ,
13 ,
8 ,
15 ,
13 ,
7 ,
5 ,
9 ,
6 ,
9 ,
10 ,
10 ,
8 ,
11 ,
6 ,
4 ,
6 ,
14 ,
8 ,
0 ,
8 ,
13 ,
10 ,
7 ,
6 ,
13 ,
14 ,
13 ,
6 ,
9 ,
5 ,
7 ,
14 ,
9 ,
13 ,
10 ,
9 ,
10 ,
15 ,
5 ,
11 ,
13 ,
10 ,
4 ,
6 ,
6 ,
15 ,
12 ,
4 ,
10 ,
5 ,
3 ,
6 ,
5 ,
9 ,
11 ,
6 ,
12 ,
7 ,
12 ,
10 ,
7 ,
4 ,
12 ,
6 ,
7 ,
7 ,
4 ,
10 ,
13 ,
7 ,
15 ,
7 ,
6 ,
10 ,
10 ,
5 ,
12 ,
8 ,
8 ,
13 ,
8 ,
11 ,
13 ,
14 ,
8 ,
11 ,
16 ,
5 ,
13 ,
8 ,
8 ,
11 ,
7 ,
6 ,
7 ,
6 ,
2 ,
6 ,
4 ,
7 ,
9 ,
9 ,
8 ,
11 ,
11 ,
12 ,
7 ,
9 ,
11 ,
5 ,
12 ,
8 ,
6 ,
5 ,
12 ,
13 ,
6 ,
9 ,
7 ,
7 ,
7 ,
10 ,
6 ,
8 ,
6 ,
14 ,
11 ,
8 ,
7 ,
11 ,
17 ,
10 ,
7 ,
8 ,
3 ,
11 ,
16 ,
6 ,
12 ,
9 ,
8 ,
6 ,
8 ,
8 ,
6 ,
10 ,
5 ,
6 ,
12 ,
9 ,
7 ,
13 ,
14 ,
8 ,
11 ,
14 ,
12 ,
12 ,
17 ,
10 ,
15 ,
7 ,
7 ,
13 ,
11 ,
12 ,
10 ,
9 ,
10 ,
11 ,
11 ,
9 ,
14 ,
11 ,
13 ,
13 ,
14 ,
9 ,
7 ,
8 ,
7 ,
7 ,
7 ,
9 ,
7 ,
5 ,
7 ,
12 ,
8 ,
11 ,
7 ,
11 ,
12 ,
11 ,
11 ,
3 ,
9 ,
9 ,
6 ,
9 ,
11 ,
9 ,
7 ,
10 ,
11 ,
8 ,
9 ,
13 ,
11 ,
2 ,
15 ,
3 ,
6 ,
13 ,
9 ,
14 ,
8 ,
7 ,
6 ,
9 ,
12 ,
5 ,
11 ,
9 ,
10 ,
14 ,
10 ,
12 ,
15 ,
13 ,
8 ,
10 ,
5 ,
10 ,
5 ,
4 ,
15 ,
8 ,
4 ,
16 ,
8 ,
6 ,
8 ,
8 ,
8 ,
12 ,
8 ,
7 ,
10 ,
6 ,
10 ,
8 ,
11 ,
14 ,
17 ,
13 ,
6 ,
12 ,
10 ,
9 ,
15 ,
9 ,
8 ,
13 ,
12 ,
7 ,
5 ,
11 ,
8 ,
5 ,
8 ,
6 ,
8 ,
13 ,
6 ,
19 ,
10 ,
8 ,
6 ,
9 ,
6 ,
9 ,
19 ,
6 ,
6 ,
12 ,
12 ,
14 ,
7 ,
14 ,
6 ,
4 ,
16 ,
14 ,
16 ,
7 ,
8 ,
2 ,
5 ,
11 ,
5 ,
6 ,
7 ,
8 ,
9 ,
13 ,
11 ,
14 ,
6 ,
13 ,
4 ,
10 ,
9 ,
13 ,
12 ,
14 ,
9 ,
13 ,
9};

for (int i=0;i<TOTAL;i++){
	sum += arr[i];
}

float mean = 0;
mean=sum/TOTAL;
printf("Average:%f\n",mean);

float summ=0;
for (int i=0;i<TOTAL;i++){
	summ += pow((arr[i]-mean),2);
}
float sd=0;
sd = sqrt(summ/TOTAL);
printf("Standard Deviation:%f\n",sd);
//https://www.indeed.com/career-advice/career-development/how-to-calculate-confidence-interval
//standard error
float se=0;
se = sd/TOTAL;


//margin of error
float margin=0;
margin = se/2;

//confidence interval or z-value 99%
//    Confidence interval (CI) = ‾X ± Z(S ÷ √n)

//In the formula, ‾X represents the sample mean, Z represents the Z-value you get from the normal standard distribution, S is the population standard deviation and n represents the sample size you're surveying.
float ci_upper = mean+0.99*(sd/sqrt(TOTAL));
float ci_lower = mean-0.99*(sd/sqrt(TOTAL));
float ci = 0.99*(sd/sqrt(TOTAL));
printf("ci = (%f,%f)\n",ci_lower,ci_upper);
printf("ci=%f\n",ci);


return 0;
}
