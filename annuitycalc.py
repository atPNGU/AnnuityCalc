import csv


def calc_annuity_monthly_tableau(loan_amount, interest, repayment, months):

    # header .csv (ger)
    fields = ["monat", "zinsen", "tilgung"]
    rows = []

    # calculating loop
    i = 1
    while i < int(months) + 1:
        if i == 1:
            repayment_mtl = round((loan_amount * repayment)/12, 2)
            interest_mtl = round((loan_amount * interest)/12, 2)
            total_mtl =  repayment_mtl + interest_mtl
            rows_1 = [i, interest_mtl, repayment_mtl]
            rows.append(rows_1)
            i += 1
            continue

        loan_amount = loan_amount - repayment_mtl
        interest_mtl = round((loan_amount * interest)/12, 2)
        repayment_mtl = round(total_mtl - interest_mtl, 2)
        if total_mtl != interest_mtl + repayment_mtl:
            break
        rows_1 = []
        rows_1 = [i, interest_mtl, repayment_mtl]
        rows.append(rows_1)
        i += 1
    
    # Export .csv
    with open('tableau.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        writer.writerows(rows)


loan_amount = 311000
interest = 0.0183
repayment = 0.03
months = 360
calc_annuity_monthly_tableau(loan_amount, interest, repayment, months)






