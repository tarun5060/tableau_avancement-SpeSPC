# Bilan de matière de l'équation: CH4 + 2*O2 --> CO2 + 2+H2O

print("Bonjour, nous allons étudier la réaction entre le méthane CH4 et le dioxygène O2")
n1 = float(input(" Entrez la valeur de la quantité de matière de méthane en mol: "))
n2 = float(input(" Entrez la valeur de la quantité de matière de dioxygène en mol: "))

#création des variables de quantités de matieres à compléter après:
n3 = 0
n4 = 0

#hypothese 1:CH4 est le réactif limitant
if n1<n2/2:
        xmax = n1
        n1f = 0
        n2f = n2 - 2*xmax
        n3f = xmax
        n4f = 2*xmax
        print("le méthane est le réactif limitant")

#hypothèse 2:O2 est le réactif limitant
elif n1>n2/2:
        xmax = n2/2
        n2f = 0
        n1f = n1 - xmax
        n3f = xmax
        n4f = 2*xmax
        print("le dioxygène est le reactif limitant")

#hypothèse 3: CH4 et O2 sont les réactifs limitants
else:
        xmax = n1
        n1f =0
        n2f =0
        n3f = xmax
        n4f = 2*xmax
        print("les réactifs ont été introduits dans les proportions stoechiometriques")

#affichage de l'état du systeme à l'état final
print("A l'etat final, la quantité de matière de méthane vaut :",n1f,"mol")
print("A l'etat final, la quantité de matière de dioxygène vaut :",n2f,"mol")
print("A l'etat final, la quantité de matière de dioxyde de carbone vaut :",n3f,"mol")
print("A l'etat final, la quantité de matière d'eau vaut :",n4f,"mol")


