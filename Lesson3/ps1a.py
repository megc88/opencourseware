original_balance = float(raw_input ("Please enter the outstanding balance on your credit card: "))
apr = float(raw_input ("Please enter your annual interest rate as a decimal: "))
payment_rate = float(raw_input ("Please enter your minimum montly payment rate as a decimal: "))
month = 1
total_paid = 0.0

for month in range(1, 13):
    monthly_payment = (payment_rate*original_balance)
    interest_paid = (apr/12.0*original_balance)
    principle_paid = monthly_payment - interest_paid
    balance = original_balance - principle_paid
    original_balance = balance
    print "Month: " + str(month)
    print "Minimum monthly payment: " + "$" + str(round(monthly_payment, 2))
    print "Principle paid: " + "$" + str(round(principle_paid, 2))
    print "Remaning balance: " + "$" + str(round(original_balance, 2))
    month += 1
    total_paid = total_paid + monthly_payment
print "RESULT"
print "Total amount paid: " + "$" + str(round(total_paid, 2))
print "Remaining balance: " + "$" + str(round(original_balance, 2))
    
    


