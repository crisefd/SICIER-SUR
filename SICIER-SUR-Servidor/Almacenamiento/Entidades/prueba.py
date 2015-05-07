import Modelos
import sys
db = Modelos.database
Adm = Modelos.Administrator

try:
	db.connect()
except Exception as err1:
	print err1

finally:
	try:
		db.close()
	except Exception as err2:
		print err2
		sys.exit()

try:
	adm = Adm.create(first_name="Mary", last_name="Jane", city="New York",
				email="mary.jane@example.com", tel_num="555111", id="999", is_active='t')
	print("Creando: ", adm.save())
except Exception as err3:
	print err3
	sys.exit()