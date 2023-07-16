from datetime import datetime

user_input = input("Digite seu objetivo com um prazo separado por dois pontos \n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
time_till = deadline_date - today_date

print(f"Querido User! Tempo restante para o seu objetivo: {goal} is {time_till.days} days")
