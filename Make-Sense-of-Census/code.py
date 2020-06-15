# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
#print("\n Data: \n",data)
#Code starts here
census=np.concatenate((data,new_record),axis=0)
print(np.shape(data))
print(np.shape(census))
#print(census)

age=np.array(data[:, [0]])
max_age=np.max(age)
print(max_age)
min_age=np.min(age)
print(min_age)
age_mean=np.mean(age)
print(age_mean)
age_std=np.std(age)
print(age_std)

race_0=[]
race_1=[]
race_2=[]
race_3=[]
race_4=[]
for i in range (0,1001):
    if census[i][2]==0:
        race_0.append(i)
print(race_0)
for i in range (0,1001):
    if census[i][2]==1:
        race_1.append(i)
#print(race_1)
for i in range (0,1001):
    if census[i][2]==2:
        race_2.append(i)
#print(race_2)
for i in range (0,1001):
    if census[i][2]==3:
        race_3.append(i)
#print(race_3)
for i in range (0,1001):
    if census[i][2]==4:
        race_4.append(i)
#print(race_4)
len_0=len(race_0)
print(len_0)
len_1=len(race_1)
print(len_1)
len_2=len(race_2)
print(len_2)
len_3=len(race_3)
print(len_3)
len_4=len(race_4)
print(len_4)

m=min(len_0,len_1,len_2,len_3,len_4)
minority_race=3

senior_citizens=[]
for i in range(0,1001):
        if census[i][0]>60:
                senior_citizens.append(i)

working_hours_sum=0
for i in range(0,1001):
        if census[i][0]>60:
                working_hours_sum=working_hours_sum+census[i][6]
print(working_hours_sum)

senior_citizens_len=len(senior_citizens)

avg_working_hours=working_hours_sum/senior_citizens_len
print(round(avg_working_hours,2))

high=[]
low=[]
for i in range(0,1001):
        if census[i][1]>10:
                high.append(i)

for i in range(0,1001):
        if census[i][1]<=10:
                low.append(i)
avg_p=0
for i in range(0,1001):
        if census[i][1]>10:
                avg_p=avg_p+census[i][7]

avg_pay_high=avg_p/len(high)
print(round(avg_pay_high,2))

avg_l=0
for i in range(0,1001):
        if census[i][1]<=10:
                avg_l=avg_l+census[i][7]

avg_pay_low=avg_l/len(low)
print(round(avg_pay_low,2))




