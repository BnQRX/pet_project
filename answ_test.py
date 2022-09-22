import json
import re
from datetime import datetime, date, time
from operator import itemgetter

with open('competitors2.json','r',encoding='utf-8') as open_json:#Считываем данные из json
    data_json = json.load(open_json)

proces_json=[]
for key, value in data_json.items():#Из .json и создаем список (меняем 1 значение на нормальное)
    proces_json.append(f'{key} {value["Surname"]} {value["Name"]}')
dict_json=[]
for dat in proces_json:
    dict_json.append(dat.split())
    dict_json[0][0]=266

with open('results_RUN.txt','r',encoding='utf-8') as open_txt:#Считываем данные из .тхт и создаем список (меняем 1 значение на нормальное)
    proces_data=[[]]
    data_txt = open_txt.readlines()
    inp_str=[str(text.strip('\n)')) for text in data_txt]
    for k in inp_str:
        proces_data.append(re.split(',| ',k))
    del(proces_data[0])
    proces_data[0][0]=287

dict_time=[]#Считаем время каждого участника
for i in range(0,len(proces_data)):
    if i%2==0:
        time_start=datetime.strptime(proces_data[i][2], '%H:%M:%S')
    else:
        time_end=datetime.strptime(proces_data[i][2], '%H:%M:%S')
        dict_time.append(f'{proces_data[i][0]} {time_end-time_start} {proces_data[i][3]}')
dict_r=[]
for ex in dict_time:#Приводим к удобному виду (разбиваем на подсписки)
    dict_r.append(ex.split())

result=[]#Собираем данные в один список
for x in dict_r:
    for y in dict_json:
        if x[0]==y[0]:
            result.append(f'{x[0]} {y[1]} {y[2]} {x[1]} {x[2]}')

stek=[]
for es in result:#Разбиваем данные и сортируем по времени
    stek.append(es.split())
newstek=sorted(stek,key=lambda x:x[3])

result_out=['Занятое_место Нагрудный_номер Имя Фамилия Результат']
step=0
for ii in newstek:#Формируем данные на выход
    step+=1
    result_out.append(f'{step} {ii[0]} {ii[1]} {ii[2]} {ii[3]}')

table=[]
for dj in result_out:#Приводим к табличному виду
    table.append(dj.split())
result_exit=[[table[iii][jjj].rjust(14) for jjj in range(len(table[iii]))] for iii in range(len(table))]

for look in result_exit:
    print(*look)
