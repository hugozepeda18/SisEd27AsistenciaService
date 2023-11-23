import requests
import datetime

url = 'http://52.53.174.157:9000/asistencia'

while(True):
    matricula = input("Escanee matricula de alumno: ")
    fecha = datetime.datetime.now()
    fechaHoy = str(fecha.year) + "-" + str(fecha.month) + "-" + str(fecha.day)
    myObj = {
        'alumno_id': matricula,
        'fecha' : fechaHoy
    }
    x = requests.post(url, data = myObj)
    if x.status_code == 201:
        print("Alumno con matrícula" + matricula + "con asistencia")
    else: 
        print("Por favor volver a escaneer credencial")