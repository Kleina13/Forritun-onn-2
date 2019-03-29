#Ragnar Helgi Breiðfjörð Unnþórsson
listi = []
for i in range(100000):
    if '7' in str(i) or '4' in str(i):
        if '1' or '2' or '3' or '5' or '6' or '8' or '9' in str(i): break
        else: listi.append(i)
print(listi)