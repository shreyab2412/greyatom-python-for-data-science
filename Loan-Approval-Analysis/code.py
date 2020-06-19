# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
bank=pd.DataFrame(bank_data)
categorical_var=bank.select_dtypes(include='object')
print(categorical_var.shape)

numerical_var=bank.select_dtypes(include='number')
print(numerical_var.shape)

banks=pd.DataFrame(bank.drop(columns='Loan_ID'))
print(banks.isnull().sum())
for column in banks.columns:
    banks[column].fillna(banks[column].mode()[0], inplace=True)
print(banks.shape)
print(banks.isnull().sum().values.sum())

avg_loan_amount=pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount',aggfunc='mean')
print(avg_loan_amount['LoanAmount'][1],2)

loan_approved_se=banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')].count()
loan_approved_nse=banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')].count()

Loan_Status=614

percentage_se=(loan_approved_se['Self_Employed']/Loan_Status)*100
print(round(percentage_se,2))

percentage_nse=(loan_approved_nse['Self_Employed']/Loan_Status)*100
print(round(percentage_nse,2))

#Step 5
def conv(num):
    return num/12
loan_term=banks['Loan_Amount_Term'].apply(conv)
big_loan_term=banks[loan_term>25].count()['Loan_Amount_Term']
print(big_loan_term)

#Step 6
#loan_groupby=banks.groupby('Loan_Status')

loan_groupby=banks.groupby('Loan_Status')['ApplicantIncome', 'Credit_History']
mean_values=loan_groupby.mean()
print(round(mean_values.iloc[1,0],2),2)




