from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

date_string = input("Entrez une date au format jj/mm/yyyy : ")

try:
    date = datetime.strptime(date_string, "%d/%m/%Y")

    nom_jour = date.strftime("%A")
    
    print(f"Le jour correspondant à la date {date_string} est : {nom_jour}")
    
except ValueError:
    print("Format de date incorrect. Assurez-vous d'utiliser le format jj/mm/yyyy.")
