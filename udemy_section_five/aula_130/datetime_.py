from datetime import datetime, timedelta

# data = datetime(2022, 6, 6, 13, 29, 55)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))  # Diretivas para formatação (Ler documentação)

# normalmente, a data virá como str. Nesses casos é possível jogar essa str em um objeto datetime.

string = '08/02/1999 21:00:00'
data = datetime.strptime(string, '%d/%m/%Y %H:%M:%S')  # é "ensinado" como o método deve interpretar a string
# stamp_data = datetime.fromtimestamp(918442800.0)
data += timedelta(days=5, seconds=2*60*60)  # é possível calcular o tempo
print(data.strftime('%d/%m/%Y %H:%M:%S'))

# é possível comparar dia/horário
data1 = datetime.strptime('01/01/2000 20:00:00', '%d/%m/%Y %H:%M:%S')
data2 = datetime.strptime('06/01/2000 20:55:00', '%d/%m/%Y %H:%M:%S')
dif = data2 - data1
# print(dif)  # 5 days, 0:55:00
# print(dif.seconds)  # 3300
# print(dif.total_seconds())  # 435300.0
# print(dif.days)  # 5

# print(data1.time())  # 20:00:00
# print(data2.time())  # 20:55:00

# é possível usar operadores para resultar bool values
print(data2 > data1)  # True
