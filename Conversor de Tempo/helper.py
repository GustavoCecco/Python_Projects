# Funções
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "Unidade não suportada"


def validate_and_execute(days_and_units_dictionary):
    try:
        user_input_number = int(days_and_units_dictionary["days"])

        # Queremos fazer a conversão apenas de números positivos
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_units_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("Voce digitou 0, por favor digite um número válido")
        else:
            print("Não é um número válido")
    except ValueError:
        print("Não é um número válido")


user_input_message = "Olá, insira o número de dias e unidade de conversão. \n"