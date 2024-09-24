from selenium import webdriver  # Importa el módulo para controlar el navegador
# Permite configurar opciones adicionales del navegador
from selenium.webdriver.chrome.options import Options
# Importa WebDriverWait para manejar esperas explícitas
from selenium.webdriver.support.ui import WebDriverWait
import logging  # Importa el módulo logging para registrar errores


def iniciar_driver():
    try:
        # Crea un objeto de opciones para configurar el navegador
        options = Options()

        # Ejecuta el navegador en modo sin interfaz gráfica (headless)
        options.headless = True

        options.add_argument("--disable-webrtc")  # Desactiva WebRTC
        # Desactiva streaming de medios
        options.add_argument("--disable-media-stream")

        # Inicia el navegador Chrome con las opciones configuradas
        driver = webdriver.Chrome(options=options)

        # Crea un objeto de espera explícita para esperar hasta 10 segundos a que ciertos elementos aparezcan
        wait = WebDriverWait(driver, 10)

        # Retorna el driver y el objeto de espera
        return driver, wait

    except Exception as e:
        # Si ocurre un error, lo registra en el archivo de logs
        logging.error(f"Error al iniciar el driver: {e}")

        # Retorna None para driver y wait si ocurre un error
        return None, None
