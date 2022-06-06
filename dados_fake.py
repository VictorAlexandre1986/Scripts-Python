#pip install faker

from faker import Faker

fake = Faker(['en_US', 'pt_BR'])

nome = fake.name()
primeiro_nome = fake.first_name_female()
usuario = fake.user_name()
senha = fake.password()
mes = fake.month()
endereco = fake.address()
texto=fake.text()