# Imports die Niemand wirklich verstehen muss...
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Nimmt sich das momentane Datum & formatiert es zu '[Stunde:Minute:Sekunde] - '.
now = datetime.now()
prefix = "[" + now.strftime("%H:%M:%S") + "] - "

# Eine Funktion um eine Text-Datei zu beschreiben.
def writeFile(response, name ,fileType):
    with open(name + fileType, "a", encoding="utf8") as f:
        f.write(response)

# Eine Funktion um den Durschnitt zu berechnen.
def calculateAverage(Sum, count):
    return Sum / count

# Eine Funktion um die Summe eines Arrays zu berechnen.
def calculateSum(arr):
    result = sum(arr)
    return result

# Fragt die Query ab die Später in den URL gegeben werden soll (der Suchbegriff)
# query = input(prefix + "Bitte gebe deine Query an << ")

# Fügt die Query in den Ebay-Kleinanzeigen URL ein.
# URL = "https://www.ebay-kleinanzeigen.de/s-" + query + "/k0"
URL = "https://www.ebay-kleinanzeigen.de/s-bielefeld/seite:1/1-zimmer-wohnung/k0l1056"
# URL = "https://www.ebay-kleinanzeigen.de/s-bielefeld/handy/k0l1056"
# Gibt aus welche Query gewählt wurde.
print(prefix + "Es wird nach gesucht nach >> " + URL)

# Setzt die Headers der Anfrage (Den User-Agent), damit Ebay-Kleinanzeigen die Anfrage nicht blockt.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.59',
}

# Gibt den HTML text der Website in eine Variable wieder.
response = requests.get(url=URL, headers=headers)

# Setzt den Content der Website in eine Variable.
page = response.content

# Erstellt eine BeautifulSoup-Instanz mit dem Website-Content und einem passendem Parser.
soup = BeautifulSoup(page, "html.parser")

# Setzt die Search-Results-Content in eine Variable.
srchRsltsContent = soup.find("ul", id="srchrslt-adtable")

# Setzt die Einträge inheralb der Seach-Results und dem Table dortdrinn in eine Variable / Array.
srchRslts = soup.find_all(class_="aditem")

# Setzt einen Counter.
counter = 0

# Setzt einen zweiten Counter.
vbCounter =  0

# Array für Preise
ePrices = []

# Looped durch alle Search-Results durch.
for srchRslt in srchRslts:
    #print(srchRslt.get_text())

    # Nimmt sich das Element mit der class "--price" als Preis.
    entry_price = srchRslt.find(class_="aditem-main--middle--price")

    # Nimmt sich das Element mit der class "--top--right" als Datum.
    entry_date = srchRslt.find(class_="aditem-main--top--right")
    
    # Nimmt sich das Element mit der class "--top--left" als Ort.
    entry_place = srchRslt.find(class_="aditem-main--top--left")
    
    # Nimmt sich das Element mit der class "ellipsis" als Title.
    entry_title = srchRslt.find(class_="ellipsis")
   
    # Nimmt sich das Element mit der class "--middle--descriptin" als Beschreibung.
    entry_desc = srchRslt.find(class_="aditem-main--middle--description")
   
    # Nimmt sich das Element mit dem data-href als Link.
    entry_link = srchRslt.find(href=True)
    print(entry_link)
    # Counter initialisieren auf 1
    counter = counter + 1

    # Ausgabe der Details
    # print("#" + str(counter) + ";" + entry_date.text.strip() + ";" + entry_place.text.strip() + ";" + entry_price.text.strip() + ";" + entry_title.text.strip() + ";" + entry_desc.text.strip())

    # Zählt wieviele Listings mit 'VB' gekennzeichnet sind.
    if("VB" in entry_price.text):
        vbCounter = vbCounter + 1
        
        # Entfernt Chars, wenn das Euro-Zeichen vorhande ist.
        # Konvertiert außerdem den Preis in eine Int und speichert ihn in den Array 'ePrices'.
        if("€" in entry_price.text):
            if("." in entry_price.text):
                if("VB" in entry_price.text):
                    ePrices.append(int(entry_price.text.replace(" ", "").replace("VB", "").replace("€", "").replace(".", "")))
                else:
                    ePrices.append(int(entry_price.text.replace(" ", "").replace("€", "").replace(".", "")))
                ePrices.append(int(entry_price.text.replace(" ", "").replace("VB", "").replace("€", "").replace(".", "")))
            else:
                ePrices.append(int(entry_price.text.replace(" ", "").replace("VB", "").replace("€", "")))
    else:
        if("€" in entry_price.text):
            if("." in entry_price.text):
                ePrices.append(int(entry_price.text.replace(" ", "").replace("€", "").replace(".", "")))
            else:
                ePrices.append(int(entry_price.text.replace(" ", "").replace("€", "")))        

# Gibt verhandelbare Listings aus.
print(prefix + "Verhandelbare Listings >> " + str(vbCounter))

# Gibt die Anzahl aller Listings aus.
print(prefix + "Anzahl der Listings >> " + str(counter))

# Gibt den Durschnitspreis der Listings aus.
print(prefix + "Durschnitts-Preis der Listings >> " + str(calculateAverage(calculateSum(ePrices), counter)))
