poids = int(input("Saisissez votre poids :"))
taille = int(input("Saisissez votre taille (en cm) :"))
IMC = poids/(taille*taille)*10000
print("Tu as un IMC de :", round(IMC,1))

if IMC < 16.5 :
    print("Tu es dans la classe : Anorexie ou dénutrition")

if (IMC >= 16.5 and IMC < 18.5) :
    print("Tu es dans la classe : Maigreur")

if IMC >= 18.5 and IMC < 25:
    print("Tu es dans la classe : Corpulence normale")

if IMC >= 25 and IMC < 30 :
    print("Tu es dans la classe : Surpoids")

if IMC >= 30 and IMC < 35 :
    print("Tu es dans la classe : Obésité modérée (Classe 1)")

if IMC >= 35 and IMC < 40 :
    print("Tu es dans la classe : Obésité élevée (Classe 2)")

if IMC > 40 :
    print("Tu es dans la classe : Obésité morbide ou massive")