start1=input("Inserire orario inizio appuntamento 1: ")
end1=input("Inserire orario fine appuntamento 1:")
start2=input("Inserire orario inizio appuntamento 2: ")
end2=input("Inserire orario fine appuntamento 2:")

if start1>start2:
    s=start1
else:
    s=start2

if end1>end2:
    e=end1
else:
    e=end2

if s<e:
    print("\nGli appuntamenti si sovrappongono")
else:
    print("\nGli appuntamenti non si sovrappongono")
