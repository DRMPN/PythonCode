balance=104 #the outstanding balance on the credit card
annualInterestRate=0.25 #annual interest rate as a decimal
minimumFixedMonthlyPayment=0
while True:
    n=12
    bal=balance
    minimumFixedMonthlyPayment=minimumFixedMonthlyPayment+10
    while n !=0:
        monthlyInterestRate=annualInterestRate/12.0 
        monthlyUnpaidBalance = bal - minimumFixedMonthlyPayment
        updatedBalanceEachMonth = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        bal=updatedBalanceEachMonth
        n-=1
    if bal<0:
        break
print("Lowest Payment: "+str(minimumFixedMonthlyPayment))
