#include<stdio.h>
#include<math.h>
#define TOTAL 493

int main(){

	int sum = 0;

	int arr[TOTAL]={65 ,
118 ,
103 ,
61 ,
8 ,
52 ,
10 ,
98 ,
28 ,
85 ,
77 ,
15 ,
2 ,
32 ,
77 ,
67 ,
46 ,
123 ,
78 ,
29 ,
26 ,
94 ,
93 ,
72 ,
28 ,
82 ,
26 ,
30 ,
117 ,
107 ,
51 ,
97 ,
9 ,
2 ,
37 ,
45 ,
88 ,
32 ,
42 ,
78 ,
16 ,
33 ,
60 ,
63 ,
116 ,
92 ,
114 ,
54 ,
8 ,
89 ,
75 ,
53 ,
86 ,
14 ,
97 ,
67 ,
69 ,
94 ,
79 ,
95 ,
63 ,
92 ,
30 ,
38 ,
68 ,
1 ,
92 ,
68 ,
87 ,
53 ,
51 ,
106 ,
35 ,
99 ,
6 ,
55 ,
123 ,
97 ,
21 ,
44 ,
86 ,
41 ,
30 ,
71 ,
86 ,
29 ,
38 ,
73 ,
65 ,
42 ,
64 ,
15 ,
60 ,
13 ,
84 ,
54 ,
72 ,
117 ,
112 ,
70 ,
6 ,
31 ,
7 ,
94 ,
54 ,
76 ,
67 ,
61 ,
122 ,
20 ,
101 ,
91 ,
19 ,
121 ,
91 ,
11 ,
121 ,
115 ,
60 ,
23 ,
113 ,
39 ,
100 ,
79 ,
20 ,
16 ,
4 ,
74 ,
17 ,
74 ,
10 ,
71 ,
52 ,
103 ,
105 ,
105 ,
100 ,
48 ,
120 ,
8 ,
72 ,
115 ,
87 ,
53 ,
56 ,
56 ,
97 ,
3 ,
39 ,
12 ,
40 ,
111 ,
86 ,
8 ,
60 ,
11 ,
103 ,
45 ,
5 ,
2 ,
112 ,
85 ,
118 ,
46 ,
68 ,
3 ,
5 ,
67 ,
52 ,
1 ,
41 ,
60 ,
49 ,
117 ,
97 ,
51 ,
87 ,
20 ,
48 ,
14 ,
35 ,
21 ,
51 ,
108 ,
70 ,
114 ,
83 ,
95 ,
16 ,
24 ,
70 ,
102 ,
113 ,
56 ,
73 ,
34 ,
46 ,
79 ,
94 ,
82 ,
116 ,
86 ,
53 ,
114 ,
94 ,
105 ,
86 ,
105 ,
52 ,
69 ,
64 ,
41 ,
20 ,
43 ,
47 ,
53 ,
94 ,
46 ,
28 ,
54 ,
90 ,
78 ,
98 ,
73 ,
28 ,
109 ,
21 ,
82 ,
45 ,
79 ,
4 ,
40 ,
10 ,
5 ,
109 ,
10 ,
14 ,
104 ,
16 ,
30 ,
105 ,
52 ,
123 ,
36 ,
59 ,
48 ,
112 ,
10 ,
102 ,
92 ,
42 ,
20 ,
45 ,
14 ,
115 ,
23 ,
30 ,
37 ,
120 ,
66 ,
52 ,
113 ,
25 ,
67 ,
40 ,
111 ,
77 ,
63 ,
48 ,
122 ,
105 ,
60 ,
42 ,
105 ,
57 ,
31 ,
64 ,
31 ,
17 ,
37 ,
78 ,
7 ,
50 ,
98 ,
112 ,
59 ,
33 ,
116 ,
24 ,
94 ,
18 ,
103 ,
7 ,
79 ,
13 ,
35 ,
37 ,
58 ,
28 ,
117 ,
51 ,
119 ,
23 ,
117 ,
81 ,
38 ,
72 ,
102 ,
8 ,
106 ,
69 ,
70 ,
39 ,
22 ,
14 ,
12 ,
85 ,
50 ,
15 ,
67 ,
80 ,
103 ,
94 ,
46 ,
36 ,
83 ,
102 ,
35 ,
100 ,
31 ,
55 ,
10 ,
91 ,
42 ,
81 ,
45 ,
111 ,
54 ,
51 ,
30 ,
13 ,
104 ,
117 ,
64 ,
68 ,
18 ,
120 ,
47 ,
32 ,
20 ,
21 ,
103 ,
49 ,
48 ,
51 ,
80 ,
70 ,
105 ,
116 ,
20 ,
79 ,
67 ,
114 ,
123 ,
31 ,
12 ,
32 ,
120 ,
104 ,
48 ,
80 ,
69 ,
15 ,
7 ,
95 ,
53 ,
11 ,
2 ,
104 ,
35 ,
82 ,
46 ,
4 ,
19 ,
103 ,
33 ,
70 ,
45 ,
50 ,
74 ,
6 ,
6 ,
106 ,
6 ,
17 ,
68 ,
66 ,
123 ,
7 ,
23 ,
112 ,
79 ,
115 ,
59 ,
95 ,
119 ,
69 ,
19 ,
77 ,
43 ,
71 ,
110 ,
50 ,
90 ,
11 ,
119 ,
108 ,
2 ,
52 ,
91 ,
96 ,
39 ,
80 ,
52 ,
119 ,
89 ,
28 ,
13 ,
101 ,
107 ,
106 ,
45 ,
64 ,
88 ,
37 ,
94 ,
35 ,
7 ,
81 ,
110 ,
74 ,
85 ,
44 ,
85 ,
21 ,
24 ,
22 ,
8 ,
66 ,
78 ,
56 ,
53 ,
15 ,
60 ,
98 ,
48 ,
98 ,
44 ,
10 ,
35 ,
65 ,
37 ,
73 ,
12 ,
70 ,
10 ,
97 ,
120 ,
69 ,
38 ,
44 ,
113 ,
91 ,
95 ,
107 ,
43 ,
79 ,
6 ,
78 ,
34 ,
37 ,
52 ,
14 ,
74 ,
59 ,
86 ,
17 ,
82 ,
13 ,
37 ,
116 ,
6 ,
42 };

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
