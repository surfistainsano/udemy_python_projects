from datetime import datetime
from calendar import monthrange

print(monthrange(2024, 2))  # é passado como argumento ANO e MÊS // (3, 29) | 0 é segunda-feira | 29 is last month's day
# para retornar um valor único, por ser uma tupla, é possível desempacotar
day_of_week, last_months_day = monthrange(2024, 2)

# para criar uma lista como mdays, porém baseado no ano atual

ultimo_dia_meses_ano_bissexto = [monthrange(datetime.now().year, mes)[1] for mes in range(1, 13)]
print(ultimo_dia_meses_ano_bissexto)
