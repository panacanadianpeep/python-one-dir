# Initiliase empty arrways

names = [None]*30
squad_shots = [None]*30
squad_assists = [None]*30
squad_goals = [None]*30
success_index = [None*30]

#Declare global variables

squad_total = 0
squad_highest = 0
player_highest = ￿""

#Validation function

def validate_score(score, score_type):
    try:
        int(score)
    except:
        return False

    # range test
    if score_type == 1 and (int(score) > 100 or int(score) < 0):
        return False
    if score_type == 2 and (int(score) > 50 or int(score) < 0):
        return False
    if score_type == 3 and (int(score) > 40 or int(score) < 0):
        return False

    #pass_tests

    return True

### Main loop

for i in range(30):

    #get inputs and validate all numberical data

    name = input(￿"Enter player￿'s name")
    name[i] = name

    shots = input(￿"Enter shots made:")
    while validate_score(shots, 1) is False:
        print(￿"Error: Unexpected input")
        shots = input(￿"Enter shots made:")

    assist = input()