# animal_age.py

def calculate_age_in_human_years(animal_type, age):
    if animal_type == "собака":
        human_age = age * 7
    elif animal_type == "кошка":
        human_age = age * 5
    else:
        human_age = age * 3
    return human_age

animal_type = input("Введите тип животного (собака, кошка, другое): ")
age = int(input("Введите возраст животного (в годах): "))

human_age = calculate_age_in_human_years(animal_type, age)

print("Возраст животного в человеческих годах: ", human_age)
