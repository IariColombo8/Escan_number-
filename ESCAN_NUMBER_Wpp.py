
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Configuración de opciones del navegador
options = Options()
options.headless = False  # Cambiar a True si quieres que se ejecute en modo headless

# Inicializar el controlador de Firefox
driver = webdriver.Firefox(options=options)

# Lista de números de destino
numeros_destino = ["5491150158659", "5491150158664", "5491150158669", "5491150158674", "5491150158679", "5491150158684", "5491150158689", "5491150158694", "5491150158699", "5491150158704", "5491150158709", "5491150158714", "5491150158719", "5491150158724", "5491150158729", "5491150158734", "5491150158739", "5491150158744", "5491150158749", "5491150158754", "5491150158759", "5491150158764", "5491150158769", "5491150158774", "5491150158779", "5491150158784", "5491150158789", "5491150158794", "5491150158799", "5491150158804", "5491150158809", "5491150158814", "5491150158819", "5491150158824", "5491150158829", "5491150158834", "5491150158839", "5491150158844", "5491150158849", "5491150158854", "5491150158859", "5491150158864", "5491150158869", "5491150158874", "5491150158879", "5491150158884", "5491150158889", "5491150158894", "5491150158899", "5491150158904", "5491150158909", "5491150158914", "5491150158919", "5491150158924", "5491150158929", "5491150158934", "5491150158939", "5491150158944", "5491150158949", "5491150158954", "5491150158959", "5491150158964", "5491150158969", "5491150158974", "5491150158979", "5491150158984", "5491150158989", "5491150158994", "5491150158999", "5491150159004", "5491150159009", "5491150159014", "5491150159019", "5491150159024", "5491150159029", "5491150159034", "5491150159039", "5491150159044", "5491150159049", "5491150159054", "5491150159059", "5491150159064", "5491150159069", "5491150159074", "5491150159079", "5491150159084", "5491150159089", "5491150159094", "5491150159099", "5491150159104", "5491150159109", "5491150159114", "5491150159119", "5491150159124", "5491150159129", "5491150159134", "5491150159139", "5491150159144", "5491150159149", "5491150159154"]  # Agrega los números que desees


# Abrir la página de WhatsApp Web
url_whatsapp = f"https://web.whatsapp.com"
driver.get(url_whatsapp)
print("Página cargada completamente")
sleep(25)
print("fin 25s")

# Iterar sobre la lista de números de destino
for numero_destino in numeros_destino:
    # URL de WhatsApp con el número de teléfono
    url_whatsapp = f"https://web.whatsapp.com/send/?phone={numero_destino}"
    # Abrir la página de WhatsApp Web
    driver.get(url_whatsapp)
    sleep(7)

    # Verificar si hay un mensaje de error que indica que el número es inválido
    mensaje_error = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/span[2]/div/span/div/div/div/div/div/div[1]")
    if mensaje_error:
        continue
    else:
        print(numero_destino)
