import time
import os
import random

ar = 9
sa = 13
sb = 55
br = 65
a = 31
r = 1
rk = 0
l = 0
food = 100
rab = 'безработный'
status = 0
z = 0
sbor = 0
avto = 0
flat = 0
comp = 0
sgd = 0
dogecoin = 0
fish=0
ud=0
pva=0
ruc=0
print('компания CoolFire Games представляет')
time.sleep(3)
os.system('clear')
print('Ukrain Simulator')
time.sleep(0.3)
print('версия 0.0.5')
time.sleep(2)
os.system('clear')
while True:
	a = a - 1
	l = l + 1
	print('Нажмите Enter чтобы пропустить день')
	print('Прожито дней:', l)
	print('Дней до зарплаты:',a)
	print('гривен:',r)	
	print('Сытость:',food,'%')
	print('работа:', rab,'(зарплата',z, 'гривен в месяц)')
	if status < 10:
		statust = 'Бомж'
	if status > 10 < 30:
		statust = 'Бедняк'
	if status == 10:
		statust = 'Бедняк'
	if status > 30 < 40:
		statust = 'Обычний человек'
	if status == 30:
		statust = 'Обычний человек'
	if status > 40 < 60:
		statust = 'Обеспеченый человек'
	if status == 60:
			statust = 'Милионер'
	if status > 60 < 80:
		statust = 'Милионер'
	if status == 80:
			statust = 'Милиардер'
	if status > 80 < 100:
		statust = 'Милиардер'
	if status == 100:
		statust = 'Милиардер'
	print('Статус:', statust)
	print('Действия:\nкупить ролтон(стоимость 1-ой упаковки 6 грн)\nкупить хлеба(стоимость одного хлеба 12 гривен)\nкупить старый гнилой дом(цена 156 гривен)\nкупить квартиру(цена 1000 гривен)\nкупить машину(цена 300 гривен)\nкупить аксесуары\nкупить комп(цена 500 гривен)\nкупить удочку(40 гривен)\nкупить клей-пва(3 гривны)\nкупить ручку(1 гривна\nмайнить\nвывести доджики\nнайти работу\nрыбачить\nказино(стоимость 50 гривен)')
	vl = input()
	if vl == 'купить ролтон':
		if r < 6:
			print('Недостаточно средств для покупки ролтона')
		else:
			print('Покупка прошла успешно')
			food = food + 10
			r = r - 6
			time.sleep(2)
	elif vl == 'купить хлеба':
		if r < 12:
			print('недостаточно средств')
			time.sleep(2)
		else:
			print('успешно куплено')
			r = r - 12
			food = food + 20
			time.sleep(2)
	elif vl == 'найти работу':
		print('Вакансии:\nрасклейщик обьявлений(чтобы устроиться нужно звание выше бомж)\nпрограмммист\nразводила лохов\nсборщик бутылок')
		print('Выбери свою работу:')
		vibrab = input()
		if vibrab == 'расклейщик обьявлений':
			if ruc <1:
				print("купите ручку")
			else:
				ruc-=1
				if pva == 0:
					print("купите клей-пва")
					time.sleep(2)
				else:
					if status < 10:
						print('Ты еще бомж')
						time.sleep(2)
				else:
					print('Вы успешно устроились')
					rab = 'раскейщик обьявлений'
					z = 49
					time.sleep(2)
		elif vibrab == 'программист':
			if ruc < 1:
				print("купите ручку")
			else:
				ruc-=1
				if comp == 0:
					print('чтобы работать нужен комп')
					time.sleep(2)
				else:
					print('вы успешно устроились')
					rab = 'программист'
					z = 56
					time.sleep(2)
		elif vibrab == 'разводила лохов':
			if ruc < 1:
				print("купите ручку")
			else:
				ruc-=1
				print('ты устроился')
				z = 40
				rab = 'разводила лохов'
				time.sleep(2)
		elif vibrab == 'сборщик бутылок':
			print('ты устроился')
			rab = 'сборщик бутылок'
			z = 36
			time.sleep(2)
		else:
			print('такой работы нет')
			time.sleep(2)
	elif vl == 'купить квартиру':
		if flat == 0:
			if r < 1000:
				print('недостаточно средств')
				time.sleep(2)
			else:
				print('куплено успешно')
				r = r - 1000
				flat = 1
				status = status + 20
				time.sleep(2)
		else:
			print('у вас уже есть квартира')
			time.sleep(2)
			
	elif vl == 'купить машину':
		if avto == 0:
			if r < 300:
				print('недостаточно средств')
				time.sleep(2)
			else:
				print('успешно куплено')
				r = r - 300
				avto = 1
				status = status + 5
				time.sleep(2)
		else:
			print('у вас уже есть автомобиль')
			time.sleep(2)
			
	elif vl == 'купить аксесуары':
		print('аксесуарры:\nцепь(цена 200 гривен)')
		print('выберите аксесуар')
		va = input()	
		if va == 'цепь':
			if r < 200:
				print('недостаточно средств')
				time.sleep(2)
			else:
				print('успешно куплено')
				r = r - 200
				status = status + 3
				time.sleep(2)
				
	elif vl == 'купить комп':
		if comp == 0:
			if r < 500:
				print('недостаточно средств')
				time.sleep(2)
			else:
				print('куплено успешно')
				comp = 1
				r = r - 500
				time.sleep(2)
		else:
			print('у тебя уже есть комп')
			time.sleep(2)
			
	elif vl == 'майнить':
		if comp == 0:
			print('у тебя нет компа')
			time.sleep(2)
		else:
			while True:
				dogecoin = dogecoin + 0.0003
				print(dogecoin, 'доджиков')
				time.sleep(0.5)
				os.system('clear')
				if dogecoin == 0.0084:
					print('ваш комп сгорел')
					comp = 0
					time.sleep(2)
					break
					
	elif vl  == 'вывести доджики':
		if dogecoin == 0:
			print('у тебя нету доджиков')
			time.sleep(2)
		else:
			print('Выводим доджики...')
			time.sleep(2)
			r = r + dogecoin * 10000
			
	elif vl == 'купить старый гнилой дом':
		if sgd == 0:
			if r < 156:
				print('недостаточно средств')
				time.sleep(2)
			else:
				print('успешно куплено')
				status = status + 10
				r = r - 156
				sgd = 1
				time.sleep(2)
		else:
			print('у тебя уже есть старый гнилой дом')
			time.sleep(2)
			
	elif vl == 'купить удочку':
		if ud == 1:
			print('у тебя уже есть удочка')
		else:
			if r < 40:
				print("недостаточно средств")
			else:
				ud=1
				r-=40
				print("покупка успешна")
		time.sleep(2)
		
	elif vl == 'рыбачить':
		if ud == 0:
			print("купи удочку")
		else:
			rfr = random.randrange(1,10)
			print('вы нарыбачили рыбы на',rfr,'гривен')
			r+=rfr
			time.sleep(2)
			
	elif vl == 'казино':
		if r < 50:
			print("недостаточно средств")
		else:
			r-=50
			vvk=random.randrange(1,90)
			print("вам выпало:",vvk,"гривен")
			r+=vvk
		time.sleep(2)
			
	elif vl == 'купить клей-пва':
		if pva == 1:
			print("у тебя есть клей-пва")
		else:
			if r < 3:
				print("недостаточно средств")
			else:
				pva=1
				print("клей-пва куплен успешно")
		time.sleep(2)
	elif vl == 'купить ручку':
		if r < 1:
			print("недостаточно средств")
		else:
			ruc += 1
			print("куплено успешно")
			
			
							
	if a == 0:
		a = 31
		r = r + z
		r-=5
	food = food -1
	if food == 0:
		print('Вы умерли от того что ваш персонаж ниче не хавал')
		break	
	elif food > 100:
		food = 100
	
	if comp == 0:
		if rab == 'программист':
			rab = 'безработний'
			z = 0
	os.system('clear')