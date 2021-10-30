# Bilan de matière de l'équation: 3*H2 + N2 --> 2*NH3

print("Bonjour, nous allons étudier la réaction entre le dihydrogène H2 et le diazote O2")
n1 = float(input(" Entrez la valeur de la quantité de matière de dihydrogène en mol: "))
n2 = float(input(" Entrez la valeur de la quantité de matière de diazote en mol: "))

#création des variables de quantités de matieres à compléter après:
n3 =0

#hypothese 1:H2 est le réactif limitant
if n1/3<n2:
        xmax = n1/3
        n1f=0
        n2f= n2 - xmax
        n3f=2*xmax
        print("le dihydrogène est le réactif limitant")

#hypothèse 2:N2 est le réactif limitant
elif n1/3>n2:
        xmax = n2
        n2f=0
        n1f= n1 - 3*xmax
        n3f=2*xmax
        print("le diazote est le reactif limitant")

#hypothèse 3: H2 et N2 sont les réactifs limitants
else:
        xmax = n2
        n1f=0
        n2f=0
        n3f=2*xmax
        print("les réactifs ont été introduits dans les proportions stoechiometriques")

#affichage de l'état du systeme à l'état final
print("A l'etat final, la quantité de matière de dihydrogène vaut :",n1f,"mol")
print("A l'etat final, la quantité de matière de diazote vaut :",n2f,"mol")
print("A l'etat final, la quantité de matière d'ammoniac vaut :",n3f,"mol")

