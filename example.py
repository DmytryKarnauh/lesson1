def get_vat(payment, percent=18):
	try:
		payment = float(payment)
		percent = int(percent)
		vat = payment / 100 * percent
		vat = round(vat, 2)
		return 'Сумма НДС: {}'.format(vat)
	except(TypeError, ValueError):
		print('Не могу посчитать, проверьте вводимые данные.')


result = get_vat(100, 10)
print(result)
print("На этом всё!")
