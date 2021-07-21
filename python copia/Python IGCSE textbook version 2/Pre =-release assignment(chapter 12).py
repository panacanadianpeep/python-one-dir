#Set up lists:￿
name = [None*30]
player_names = [None]*30
squad_shot = [None]*30
squad_assits = [None]*30
squad_goals = [None]*30
success_index = [None]*30

#Variables

index = 0
highest_success = 0
best_player = ￿""

for index in range(0,30):
    name[index] = input(￿"What is your name￿")
    Squad_goals = int(input(￿"Goals?￿"))
    player_names[index] = name
    while True:
        player_Shot = ￿int(input(￿"Number of goals scored"))
        if player_Shot < 100:
            squad_shot[index] = player_Shot
            break
        else:
            print(￿"Error")
    while True:
        player_assist = int(input(￿"Maximum goals"))
        if player_assist < 100:
            squad_assits[index] = player_assist
            break
        else:
            print(￿"Error")
    while True:
        Squad_goals = int(input(￿"Goals?￿"))
        if Squad_goals:
            squad_goals[index] = Squad_goals
            break
        else:
            print(￿"Error￿￿")
    success_index[index] = player_assist+(2*player_Shot)+(3*squad_goals)
    squad_added_sucess =+ success_index[index
    if success_index[index] > highest_success:
        highest_success = success_index
        best_player = name[index]

squad_average_sucess = squad_added_sucess_sucess / 30

print(name)
print(player_names)
print(squad_shot)
print(squad_assits)
print(success_index)
print(squad_goals)
print(￿"The best player is￿￿", best_player, ￿￿"and his success index is", highest_success)
print("￿Average squad average sucess index is￿￿", squad_average_sucess)