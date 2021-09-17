import csv

def calc_annuity_monthly_tableau(darlehenssumme, zinssatz, tilgungssatz, monate):

    # Listen für return
    fields = ["monat", "zinsen", "tilgung"]
    rows = []

    # Ermittlung Restschuld  >> Zinsen auf Restschuld >> neue Tilgung >> ..
    i = 1
    while i < int(monate) + 1:
        if i == 1:
            rate_tilgung_mtl = round((darlehenssumme * tilgungssatz)/12, 2)
            rate_zinsen_mtl = round((darlehenssumme * zinssatz)/12, 2)
            rate_gesamt_mtl =  rate_tilgung_mtl + rate_zinsen_mtl
            rows_1 = []
            rows_1.append(i)
            rows_1.append(rate_zinsen_mtl)
            rows_1.append(rate_tilgung_mtl)
            rows.append(rows_1)
            i += 1
            continue

        darlehenssumme = darlehenssumme - rate_tilgung_mtl
        rate_zinsen_mtl = round((darlehenssumme * zinssatz)/12, 2)
        rate_tilgung_mtl = round(rate_gesamt_mtl - rate_zinsen_mtl, 2)
        if rate_gesamt_mtl != rate_zinsen_mtl + rate_tilgung_mtl:
            break
        rows_1 = []
        rows_1.append(i)
        rows_1.append(rate_zinsen_mtl)
        rows_1.append(rate_tilgung_mtl)
        rows.append(rows_1)
        i += 1
    
    # Export .csv
    with open('tableau.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        writer.writerows(rows)

def calc_annuity_monthly_graph(darlehenssumme, zinssatz, tilgungssatz, monate):

    # Listen für return
    fields = ["zinsen", "tilgung"]
    rows = []

    # Ermittlung Restschuld  >> Zinsen auf Restschuld >> neue Tilgung >> ..
    i = 1
    while i < int(monate) + 1:
        if i == 1:
            rate_tilgung_mtl = round((darlehenssumme * tilgungssatz)/12, 2)
            rate_zinsen_mtl = round((darlehenssumme * zinssatz)/12, 2)
            rate_gesamt_mtl =  rate_tilgung_mtl + rate_zinsen_mtl
            rows_1 = []
            rows_1.append(rate_zinsen_mtl)
            rows_1.append(rate_tilgung_mtl)
            rows.append(rows_1)
            i += 1
            continue

        darlehenssumme = darlehenssumme - rate_tilgung_mtl
        rate_zinsen_mtl = round((darlehenssumme * zinssatz)/12, 2)
        rate_tilgung_mtl = round(rate_gesamt_mtl - rate_zinsen_mtl, 2)
        if rate_gesamt_mtl != rate_zinsen_mtl + rate_tilgung_mtl:
            break
        rows_1 = []
        rows_1.append(rate_zinsen_mtl)
        rows_1.append(rate_tilgung_mtl)
        rows.append(rows_1)
        i += 1
    
    # Export .csv
    with open('graph.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        writer.writerows(rows)

# Ausführung
darlehen_sum = 311000
zins_percent = 0.0183
tilgung_percent = 0.03

calc_annuity_monthly_tableau(darlehen_sum, zins_percent, tilgung_percent, monate=360)
calc_annuity_monthly_graph(darlehen_sum, zins_percent, tilgung_percent, monate=360)






