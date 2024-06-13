import sys 



percent = 100

def calculate_emi(loan_amount, interest_rate, loan_period):

    try:
        monthly_roi = loan_amount * interest_rate / percent  # Monthly interest rate
        n = monthly_roi * loan_period  # Number of periods (months)
        emi = loan_amount + n
        return float(emi)

    except SystemExit as e:
        sys.exit('There was an error {}'.format(e))


#sum_r = loan_amount * interest_rate / 100
#monthly_return = sum_r * loan_period
#emi = monthly_return + loan_amount