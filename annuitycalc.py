# Eingabewerte
darlehen_sum = 311000
zins_percent = 0.0183
tilgung_percent = 0.03

def calc_annuity_monthly(darlehenssumme, zinssatz, tilgungssatz):
    
    # Ermittlung Startraten
    rate_tilgung_mtl = round((darlehenssumme * tilgungssatz)/12, 2)
    rate_zinsen_mtl = round((darlehenssumme * zinssatz)/12, 2)
    rate_gesamt_mtl =  rate_tilgung_mtl + rate_zinsen_mtl
    print("m1 Zinsen: " + str(rate_zinsen_mtl) + " Tilgung: " + str(rate_tilgung_mtl))
    
    # Ermittlung Restschuld  >> Zinsen auf Restschuld >> neue Tilgung >> repeat
    i = 2
    restschuld = darlehenssumme
    while i < 13:
        restschuld = restschuld - rate_tilgung_mtl
        rate_zinsen_mtl = round((restschuld * zinssatz)/12, 2)
        rate_tilgung_mtl = round(rate_gesamt_mtl - rate_zinsen_mtl, 2)
        print("m" + str(i) + " Zinsen: " + str(rate_zinsen_mtl) + " Tilgung: " + str(rate_tilgung_mtl))
        i += 1

def calc_annuity_annualy(darlehenssumme, zinssatz, tilgungssatz):
    
    # Ermittlung Startraten
    rate_tilgung_ann = round((darlehenssumme * tilgungssatz), 2)
    rate_zinsen_ann = round((darlehenssumme * zinssatz), 2)
    rate_gesamt_ann =  rate_tilgung_ann + rate_zinsen_ann
    print("j1 Zinsen: " + str(rate_zinsen_ann) + " Tilgung: " + str(rate_tilgung_ann))
    
    # Ermittlung Restschuld  >> Zinsen auf Restschuld >> neue Tilgung >> repeat
    i = 2
    restschuld = darlehenssumme
    while i < 11:
        restschuld = restschuld - rate_tilgung_ann
        rate_zinsen_ann = round((restschuld * zinssatz), 2)
        rate_tilgung_ann = round(rate_gesamt_ann - rate_zinsen_ann, 2)
        print("j" + str(i) + " Zinsen: " + str(rate_zinsen_ann) + " Tilgung: " + str(rate_tilgung_ann))
        i += 1

# Ausführung
calc_annuity_monthly(darlehen_sum, zins_percent, tilgung_percent)
calc_annuity_annualy(darlehen_sum, zins_percent, tilgung_percent)

