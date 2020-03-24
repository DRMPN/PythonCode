    #not changable
'''
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''

#for month0
def eachMonth(balance,annualInterestRate,monthlyPaymentRate):
    n=12  
    while n!=0:
        monthlyInterestRate=annualInterestRate/12.0
    
        minimumMonthlyPayment=monthlyPaymentRate*balance
    
        monthlyUnpaidBalance=balance-minimumMonthlyPayment
    
        updatedBalanceEachMonth=monthlyUnpaidBalance+monthlyInterestRate*monthlyUnpaidBalance
    
        monthlyInterest=monthlyInterestRate*monthlyUnpaidBalance
    
        balance=monthlyUnpaidBalance+monthlyInterest
        
        n-=1
    else:
        return "Remaining balance: " + str(round(balance,2))


balance=5000
annualInterestRate=0.18
monthlyPaymentRate=0.02

n=12  
while n!=0:
    monthlyInterestRate=annualInterestRate/12.0
    
    minimumMonthlyPayment=monthlyPaymentRate*balance
    
    monthlyUnpaidBalance=balance-minimumMonthlyPayment
    
    updatedBalanceEachMonth=monthlyUnpaidBalance+monthlyInterestRate*monthlyUnpaidBalance
    
    monthlyInterest=monthlyInterestRate*monthlyUnpaidBalance
    
    balance=monthlyUnpaidBalance+monthlyInterest
        
    n-=1
else:
    print("Remaining balance: " + str(round(balance,2)))