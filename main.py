# Bilan de matière de l'équation: 2*H2 + 02 --> 2*H20

print("Bonjour, nous allons étudier la réaction entre le dihydrogène H2 et le dioxygène O2")

v1 = float(input(" Entrez la volume de la quantité de matière de dihydrogène en mL: "))
v2 = float(input(" Entrez la volume de la quantité de matière de dioxygène en mL: "))

n1 = (v1*10**-3)/22.4
n2 = (v2*10**-3)/22.4

#création des variables de quantités de matieres à compléter après:
n3 =0

#hypothese 1:H2 est le réactif limitant
if n1/2<n2:
        xmax = n1/2
        n1f=0
        n2f= n2 - xmax
        n3f=2*xmax
        print("le dihydrogène est le réactif limitant")

#hypothèse 2:O2 est le réactif limitant
elif n1/2>n2:
        xmax = n2
        n2f=0
        n1f= n1 - 2*xmax
        n3f=2*xmax
        print("le dioxygène est le reactif limitant")

#hypothèse 2:O2 est le réactif limitant
else:
        xmax = n2
        n1f=0
        n2f=0
        n3f=2*xmax
        print("les réactifs ont été introduits dans les proportions stoechiometriques")

#affichage de l'état du systeme à l'état final
print("A l'etat final, la quantité de matière de dihydrogène vaut :",n1f,"mol")
print("A l'etat final, la quantité de matière de dioxygène vaut :",n2f,"mol")
print("A l'etat final, la quantité de matière d'eau vaut :",n3f,"mol")

#test