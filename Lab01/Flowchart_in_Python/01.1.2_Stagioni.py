m=input("Inserire mese: ")
d=input("Inserire giorno:")

month=int(m)
day=int(d)

if month<4:
    stagione="Winter"
elif month<7:
    stagione="Spring"
elif month<10:
    stagione="Summer"
else:
    stagione="Fall"

rest=month%3

if rest==0:
    if day>=21:
        if stagione=="Winter":
            stagione="Spring"
        elif stagione=="Spring":
            stagione="Summer"
        elif stagione=="Summer":
            stagione="Fall"
        else:
            stagione="Winter"

print("Stagione: ",stagione)
