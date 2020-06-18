import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

## fake pop script
import random
from AppTwo.models import UserInfo
from faker import Faker 

fake_gen = Faker()

def populate(N=5):

	for entry in range(N):
		fake_name = fake_gen.name().split()
		fake_mail = fake_gen.email()
		usr = UserInfo.objects.get_or_create(first_name = fake_name[0],last_name = fake_name[1],email = fake_mail)[0]

if __name__ == '__main__':
	print("Populating Script")
	populate(10)
	print("Population Completed!")
