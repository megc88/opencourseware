balance = float(raw_input("Please enter the outstanding balance on your credit card: "))
apr = float(raw_input("Please enter your annual interest rate as a decimal: "))
monthly_interest = apr/12.0
monthly_payment = 10.0
month = 12.0

##while month in range (1,13):
##    new_balance = balance * (1 +(apr/12.0)) - monthly_payment
##    balance = new_balance
##    month += 1
##if balance >0:
##    monthly_payment += 10.0
##    month = 1
##else:
##    print "RESULT"
##    print "Monthly payments to pay off debt in 1 year: " + str(monthly_payment)
##    print "Number of months needed: " + str(month)
##    print "Balance: " + str(round(balance,2))
##while balance > 0:
##    if monthly_payment(1.0 + monthly_interest)(((1.0 +monthly_interest)**month - 1.0)/monthly_interest) <= 0.0:
##        print "RESULT"
##        print "Monthly payments to pay off debt in 1 year: " + str(monthly_payment)
##        print "Number of months needed: " + str(month)
##        print "Balance: " + str(round(balance,2))
##    else:
##        monthly_payment += 10.0
##



while balance*((1.0+monthly_interest)**(month)) + ((-monthly_payment)*(((1.0 + monthly_interest)**month - 1.0)/ monthly_interest)) > 0:
    monthly_payment += 10.0
if balance*((1.0+monthly_interest)**(month)) + ((-monthly_payment)*(((1.0 + monthly_interest)**month - 1.0)/ monthly_interest)) <=0:
    new_balance = balance*((1.0+monthly_interest)**(month)) + ((-monthly_payment)*(((1.0 + monthly_interest)**month - 1.0)/ monthly_interest))
    print "RESULT"
    print "Monthly payments to pay off debt in 1 year: " + str(monthly_payment)
    print "Number of months needed: " + str(month)
    print "Balance: " + str(round(new_balance,2))
else:
    print "failure"

