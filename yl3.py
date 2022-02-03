# harjutus 3
# Caroline Samarajev
# 03.02.2022


#palindroom
palin = input("Sisesta palindroom: ")
print([::-1])

#tundide ajad
start = input("Algusaeg: ")
lopp = input("Lõpuaeg: ")
#tükeldus
hh1,mm1 = start.split(":")
hh2,mm2 = lopp.split(":")
#teisendamine minutiteks
minutid = int(hh1)*60+int(mm1)
minutid2 = int(hh2)*60+int(mm2)
#absoluutväärtus
ajavahe = abs(minutid-minutid2)
#teisendamine hh:mm
hh = ajavahe // 60 #täisarvuline jagamine
mm = ajavahe % 60 #jääk

print(f"Õpilase päeva pikkus on {hh}:{mm}")




#emaili kontroll
#TRUE/FALSE
email = input("Sisesta email: ")
print('@' in email)
#TRUE/FALSE in/not in

#vandumine
vanne = input("Ära kurat ütle: ")
vanne = vanne.lower().replace("kurat","*****")
print(vanne)

#korralik kasutajanimi
nimi = input("Sisesta nimi: ")
nimi = nimi.strip().capitalize()
print("Tere "+nimi+"!")

