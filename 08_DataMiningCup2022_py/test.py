from datetime import datetime

a = '2020-06-01'
b = '%Y-%m-%d'

c = datetime.strptime(a, b)

print(c)