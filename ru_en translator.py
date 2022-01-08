from googletrans import Translator
print("Dasturni to'xtatish uchun 'q' ni bosing! " )
while True:
	savol = input("Tilni tanlang(en/ru): ")
	if savol=='en':
		matn_uz = input("Matnni kiriting: ")
		tarjimon = Translator() # Translator bu maxsus klass (tarjimon esa obyekt)
		tarjima = tarjimon.translate(matn_uz, dest='en')
		print("Tarjimasi",tarjima.text)
	if savol == "ru":
		matn_ru = input("Matnni kiriting: ")
		tarjimon = Translator()
		tarjima_ru = tarjimon.translate(matn_ru, dest='ru')
		print("Tarjimasi: ", tarjima_ru.text)
	if savol == 'q':
		print("Bizning translatordan foydalanganingiz uchun minatdormiz!")
		break