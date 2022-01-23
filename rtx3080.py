# NBB RTX 3080 GRABBER made by human on earth.

# Don't be evil.

#import sys
#sys.stdout = open('C:\Users\nicla\Desktop\console_log.txt', 'w') # kleines Hurensohn Skript

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random
import time

browser  = webdriver.Chrome(ChromeDriverManager().install())

random_wait_time = random.uniform(0.5, 10.0)
print(random_wait_time)

# Notebooksbilliger Seite mit der RTX 3080 aufrufen.
# "#" in der nächsten Zeile wieder entfernen, wenn fertig mit testen!
# browser.get('https://www.notebooksbilliger.de/nvidia+geforce+rtx+3080+founders+edition+690362?nbb=pn.&nbbct=1002_10#Q0C10')

# Alternativer Test Link zu einem Billig Handy, um den Prozess zu testen.
# "#" in der nächsten Zeile wieder hinzufügen, wenn fertig mit testen!
browser.get('https://www.notebooksbilliger.de/nokia+105+2019+dual+sim+blau+629020/eqsqid/15a2179b-eeb7-4b5f-9ae5-e054125726b5')

# "Nur Notwendige Cookies" akzeptieren.
time.sleep(random_wait_time)
browser.find_element_by_xpath('//*[@id="uc-btn-deny-banner"]').click();

# "In den Warenkorb" anklicken.
time.sleep(random_wait_time)
browser.find_element_by_xpath('//*[@id="right-side-widget"]/div[8]/form/section/div/button').click();

# "Direkt zur Kasse" anklicken.
time.sleep(random_wait_time)
browser.find_element_by_xpath('//*[@id="cartlayer_link_checkout"]').click();

# "Anmelden" anklicken.
time.sleep(random_wait_time)
browser.find_element_by_xpath('//*[@id="epoq_searchresult"]/div/div[2]/div/div[4]/div/div[2]/form/div[3]/div[2]/button').click();

# Variable für Handynummer.
handynummer = "+49 1111 1111111"

# Feld "Handynummer" ausfüllen.
time.sleep(random_wait_time)
browser.find_element_by_xpath('//*[@id="delivery_address_box"]/div[2]/div/input').send_keys(handynummer)

# "Adresse wählen" anklicken.
time.sleep(random_wait_time)
browser.find_element_by_xpath('//*[@id="delivery_private"]/div[3]/div[1]/button').click();

# "Kauf auf Rechnung" (Klarna) anklicken.
time.sleep(random_wait_time)
browser.find_element_by_xpath('//*[@id="idpayklarnapaylater"]/label/span').click();

# AGB & Belehrung akzeptieren.
time.sleep(random_wait_time)
browser.find_element_by_xpath('//*[@id="checkout_box_terms_and_conditions"]/div/label[3]/span').click();

# Variable für mein Geburtsdatum für die Klarna Altersbestätigung.
geburtsdatum = "20082000"

# Altersbestätigungsfeld ausfüllen. Klarna setzt nach TT/MM/JJJJ automatisch Punkte.
time.sleep(random_wait_time)
browser.find_element_by_xpath('//*[@id="invoice_kp-purchase-approval-form-date-of-birth"]').send_keys(geburtsdatum)

# "Bestätigen" anklicken.
time.sleep(random_wait_time)
browse.find_element_by_xpath('//*[@id="invoice_kp-purchase-approval-form-continue-button"]/div/div[1]').click();

# Wenn alles erfolgreich ist, dann Bestätigung senden.
print('Alle Befehle wurden erfolgreich ausgeführt.')

#sys.stdout.close()

#      >(o)
#       (  / )
