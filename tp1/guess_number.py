from random import randint
number_to_guess = randint(0, 100)
has_won = False
i = 0
while has_won is False and i < 10:
    user_propal = int(input("Donner un nombre compris entre 0 et 100 : "))
    while user_propal < 0 or user_propal > 100:
        print("Veuillez entrer un nombre entre 0 et 100")
        user_propal = int(input("Donner un nombre compris entre 0 et 100 : "))
    if number_to_guess == user_propal:
        has_won = True
    elif number_to_guess > user_propal:
        print("Le nombre que vous avez saisi est trop petit.")
    elif number_to_guess < user_propal:
        print("Le nombre que vous avez saisi est trop grand.")
    i += 1
if has_won is False:
    print("Vous n'avez pas trouvé le nombre ! Dommage, le nombre était", number_to_guess)
if has_won is True:
    print("Vous avez trouvé le bon nombre en ",i ,"essai ! Le nombre était bien", number_to_guess)
