from faker import Faker

fake = Faker('ru_RU')
ru_first_name = fake.first_name()
ru_last_name = fake.last_name()
ru_email = fake.email()
ru_password_field = fake.password(length=8)
ru_confirm_pass = ru_password_field
wrong_email = fake.user_name() + "example.com"
empty_name = ''

fake = Faker()
en_first_name = fake.name()
en_last_name = fake.last_name()
en_email = fake.email()
en_password_field = fake.password(length=10)
en_confirm_pass = en_password_field
