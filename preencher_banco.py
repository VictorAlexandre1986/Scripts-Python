#pip install psycopg2
#pip install faker

con = psycopg2.connect(
    host='localhost',
    database='teste',
    user='postgres',
    password='postgres'
)

cur = con.cursor()

fake = Faker(locale='pt-br')

base_sql = '''Insert into Clientes (nome,email,usuario) values ('{}','{}','{}')'''

for i in range(1000):
    nome = fake.name()
    email = fake.email()
    usuario=fake.user_name()
    sql = base_sql.format(nome,email,usuario)
    cur.execute(sql)

con.commit()
con.close()