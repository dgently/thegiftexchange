import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','xmasList.settings')

import django
django.setup()


from django.contrib.auth.models import User
from wishlist.models import UserInfo

def populate():
	family=[
	('Michael','Weilert'),
	('Genevive',"W"),
	('Christiana','Weilert'),
	('Carl','Weilert'),
	('Lynne','Weilert'),
	('Sara','Gillette'),
	('Clay','Gillette'),
	('Sam','Weilert'),
	('Rachel','Weilert'),
	('CarlS','Sauvey'),
	('Philip','Sauvey'),
	('Gretchen','Sauvey'),
	('David','Sauvey'),
	('Marian','Sauvey'),
	('Barb','Kramer'),
	('Rich','Kramer'),
	('Jeff','Kramer'),
	('Teresa','Kramer'),
	('Joe','Kramer'),
	('Laura','Weilert'),
	('Andrew','Weilert'),
	('Julie','Weilert'),
	('Ben','Weilert'),
	('Stephanie','Weilert'),
	('Tim','Weilert'),
	('Mark','Weilert'),
	('Hsin-yi','Weilert'),
	]

	for person in family:
		print "adding %s" % (person[0])
		addUser(person)


def addUser(person):
	first,last=person
	u=User.objects.get_or_create(first_name=first,last_name=last,username=first.lower())[0]
	u.set_password('xmas')
	u.save()
	info=UserInfo.objects.get_or_create(user=u)
	return u

if __name__=='__main__':
	print "Populating!"
	populate()