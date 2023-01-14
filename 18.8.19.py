bileti = int(input('Введите количество билетов: '))
vozrast_ = []
for i in range(0, bileti):
    input_value = int(input(f'Введите возраст участника №{i + 1}: '))
    vozrast_.append(input_value)
    def prise(vozrast):
        if vozrast < 18:
            return 0
        elif 18 <= vozrast < 25:
            return 990
        else:
            return 1390
    full_prise = sum(map(prise, vozrast_))
discount_prise = int(full_prise * 0.9)
if bileti > 3:
    print('Стоимость всех билетов со скидкой: ', discount_prise, "руб.")
else:
    print('Стоимость всех билетов: ', full_prise, "руб.")