#bisection search. I think mistake in % and something wrong with lowestPayment
#balance = 320000; annualInterestRate = 0.2; Lowest Payment: 29157.09
#balance = 207035; annualInterestRate = 0.18; Lowest Payment: 18700.46
#balance = 387778; annualInterestRate = 0.18; Lowest Payment: 35026.09
balance=999999
annualInterestRate=0.18
lowestPayment=1/12*balance
answ=lowestPayment
while True:
    n=12
    bal=balance
    while n !=0:
        monthlyInterestRate=annualInterestRate/12 
        monthlyUnpaidBalance = bal - answ
        updatedBalanceEachMonth = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        bal=updatedBalanceEachMonth
        n-=1
    if bal<0:
        break
    highestPayment=1/12*bal 
    answ=(highestPayment+lowestPayment)/2
    if answ**2<highestPayment:
        lowestPayment=1/12*bal
        answ=lowestPayment
    elif answ**2>highestPayment:
        answ=highestPayment
print("Lowest Payment: "+str(round(answ,2))) 