import numpy as np

#read the file
data = np.genfromtxt("loans.csv", delimiter=',', skip_header=1, usecols=8)

#Remove NaN values from the loan amount column
loan_amounts = data[~np.isnan(data)]

#Compute basic statistics
mean_loan = np.mean(loan_amounts)
print(mean_loan)

#Compute the median
median_loan = np.median(loan_amounts)
print(median_loan)

#compute for standard deviation
std_loan = np.std(loan_amounts)
print(std_loan)
