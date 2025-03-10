import calculatrice


# def demandeage(age, prenom):
#     if age < 18:
#         print(f"Tu es encore un padawan, jeune {prenom} !")
#     elif 18 <= age <= 40:
#         print(f"Bienvenue dans le monde des responsabilités, {prenom} !")
#     elif 41 <= age <= 60:
#         print(f"Tu es une personne expérimentée dans la vie, {prenom} !")
#     else:
#         print(f"Vous êtes une personne mature, {prenom} !")

#     return age, prenom

# # prenom = str(input("Entrer votre prenom  : " ))
# # try :
# #     age = int(input("Entrer votre age  : "))
# #     resultat = demandeage(age,prenom)
    
# #     print (resultat)
# # except : 
# #     print('erreur')
   

nb1 = int(input("Entrez votre nombre1  : "))
nb2 = int(input("Entrez votre nbr2  : "))


print(calculatrice.addition(nb1,nb2))
print(calculatrice.quotient(nb1,nb2))
print(calculatrice.diference(nb1,nb2))
print(calculatrice.multiplication(nb1,nb2))




# prenom = str(input("Entrer votre prenom  : " ))

# age_non_defini = True
# while age_non_defini :

#     try:
#         age = int(input("Entrer votre age  : "))

#         age_non_defini= False
       
#         resultat = demandeage(age,prenom)
       

#         print(resultat)
#     except : 
#        print('erreur')    


