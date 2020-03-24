balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate/12.0
monthlyLower = balance/12
monthlyUpper = (balance * (1+monthlyInterestRate)**12)/12.0

while True:     
     updatedBalance = balance
     for n in range(12):
        payment = (monthlyUpper + monthlyLower)/2.0 
        monthlyUnpaidBalance = updatedBalance - payment
        updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
     if updatedBalance < -0.01:
        monthlyUpper = payment
     elif updatedBalance > 0.01:
        monthlyLower = payment
     else:
         break

print("Lowest {:0.2f}".format(payment))