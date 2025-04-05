# and or no  are logical operators
high_income = False
good_credit = True
student = False
if (high_income or good_credit) and not student:
    # ADD OPERATOR BOTH CONIDITONS ARE TRUE  TEH RESULT WILL BE TRUE
    print("eligible")
else:                       # OR operator  at least 1 condition is  true  the answer will be true
    print("Not eligible")
