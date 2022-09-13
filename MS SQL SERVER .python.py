import pyodbc
exit_key=0 #глобальная переменная на выход из программы
def answer(input_str): #функция отслеживания ответа пользователя
    if (('y' in input_str) or ('n' in input_str)) and len(input_str)==1: #проверка ввода Y или N
        if 'y' in input_str:
            return 1
        else:
            return 0
    else:
        print('Некорректный ответ\n')
        return 3



def connect_DB (serv_adr,base_name): #функция подключения к БД
    try:
        connectionString = ("Driver={SQL Server Native Client 11.0};" #Соединение к БД (MS SQL Server) авторизацией Windows
                                   "Server=PORT;"
                                   "Database=BNAME;"
                                   "Trusted_Connection=yes;").replace('PORT', serv_adr).replace('BNAME', base_name)
        connection = pyodbc.connect(connectionString)
    except pyodbc.OperationalError: #Обработка исключения по неверным данным входа
        print('Неверный адрес сервера или пароль\n')
        return 0
    else:
        try:
            dbCursor = connection.cursor() #создаем курсор для работы с БД
            print('Введите SQL запрос')
            insert_sql=input().lower() #считываем SQL запрос (MS SQL Server)
            requestString = '''sql'''.replace('sql',insert_sql)
            dbCursor.execute(requestString) #Выполняем SQL запрос
        except pyodbc.ProgrammingError: #Ловим исключение на некорректный SQL запрос
            print('Неверный SQL запрос\n')
            return 0
        else:
            for answer in dbCursor: #Выподим результат на экран (в планах вывод в файл по выбору пользователя)
                print(answer)
            print('Запрос выполнен')
            return 0
            connection.commit() #Закрываем соединение с БД

while exit_key==0: #Запускаем программу в работу пока пользователь не решит выйти exit_key==1)
    info_db=[] #заполняем данные по подключению к БД
    print('Введите адрес сервера')
    info_db.append(input())
    print('Введите имя базы данных')
    info_db.append(input())    
    x=connect_DB (info_db[0],info_db[1])# открываем подключение к БД с помощью функции
    if x == 0:# ловим возврат от функции 0 если пользователь сделал что то неверно
        exit_key2=0 
        while exit_key2==0:#запускаем опрос пользователя на действие(выход по exit_key2==1) "пользователь вводит n)
            print('Попробуете еще раз? (y/n)')
            answ=input().lower()
            y=answer(answ)#проверяем ответ пользователя возвратом функии answ
            if y==1:#пользователь ввел y, выходим из цикла опроса запускаем цикл работы программы
                exit_key2=1
            elif y==0:# пользователь ввел n, выходим из цикла опроса и цикла работы программы
                exit_key=1
                exit_key2=1
                print('Спасибо за пользование сервисом :)')
            elif y==3:# пользователь ввел другие буквы, опрашиваем заново
                continue
        
        
        
        