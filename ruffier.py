txt_index = "Ваш индекс Руфье: "
txt_workheart = "Работоспособность сердца: "
txt_nodata = '''
нет данных для такого возраста'''
txt_res = []
txt_res.append('''низкая. 
Срочно обратитесь к врачу!''')
txt_res.append('''удовлетворительная. 
Обратитесь к врачу!''')
txt_res.append('''средняя. 
Возможно, стоит дополнительно обследоваться у врача.''')
txt_res.append('''
выше среднего''')
txt_res.append('''
высокая''')

def ruffier_index(P1, P2, P3):
    r_index = (4 * (P1 + P2 + P3)-200)/10
    return r_index

def neud_level(age):
    norm_age = (min(age, 15) - 7) // 2  # каждые 2 года разницы от 7 лет превращаются в единицу - вплоть до 15 лет
    result = 21 - norm_age * 1.5 # умножаем каждые 2 года разницы на 1.5, так распределены уровни в таблице
    return result

def ruffier_result(r_index, level):
    if r_index >= level:
        return 0
    level = level - 4
    if r_index >= level:
        return 1
    level = level - 5
    if r_index >= level:
        return 2
    level = level - 5.5
    if r_index >= level:
        return 3
    return 4

def test(P1, P2, P3, age):
    r_index = ruffier_index(P1, P2, P3)
    level = neud_level(age)
    res = ruffier_result(r_index, level)
    return txt_index + str(r_index) + '\n' + txt_workheart + txt_res[res]
