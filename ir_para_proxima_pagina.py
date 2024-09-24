from time import sleep  # Importa sleep para pausar la ejecución
import random  # Importa random para generar pausas aleatorias
import logging  # Importa logging para registrar errores
# Permite seleccionar elementos en la página por su localización
from selenium.webdriver.common.by import By
# Permite esperar explícitamente a que un elemento esté disponible
from selenium.webdriver.support.ui import WebDriverWait
# Condiciones esperadas para WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Importa funciones de scroll y verificación de ventana
from scroll import scroll_pagina_totalmente_para_baixo, verificar_ventana_abierta
# Importa la función de conexión
from conectar_com_pessoas_na_pagina_atual import conectar_com_pessoas_na_pagina_atual


def ir_para_proxima_pagina(driver, conexoes_enviadas):
    limite_diario = 1  # Definir el límite diario aquí también
    # Espera explícita de hasta 10 segundos para que los elementos aparezcan
    wait = WebDriverWait(driver, 10)

    while conexoes_enviadas < limite_diario:
        try:
            # Verifica si la ventana sigue abierta antes de realizar cualquier acción
            if not verificar_ventana_abierta(driver):
                break  # Detiene si la ventana ya está cerrada

            # Conectar con personas en la nueva página
            conexoes_enviadas = conectar_com_pessoas_na_pagina_atual(
                driver, conexoes_enviadas)

            # Verifica si se ha alcanzado el límite de conexiones después de intentar conectar
            if conexoes_enviadas >= limite_diario:
                logging.info(
                    "Se alcanzó el límite diario de conexiones. Deteniendo el avance.")
                break  # Detiene el bucle sin avanzar de página si ya se alcanzó el límite

            # Hace scroll hacia abajo para cargar más elementos en la página
            scroll_pagina_totalmente_para_baixo(driver)

            # Intenta encontrar el botón "Avançar" (para avanzar a la siguiente página) usando un XPath
            try:
                # Uso de una espera explícita para esperar a que el botón sea clicable
                botao_ir_para_proxima_pagina = wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Avançar']")))
            except Exception as e:
                logging.error(f"No se encontró el botón 'Avançar': {e}")
                break  # Sale del bucle si no encuentra más páginas

            # Pausa por un tiempo aleatorio entre 2 y 5 segundos simulando el comportamiento humano
            sleep(random.randint(2, 5))

            # Verifica si el botón está habilitado y hace clic
            if botao_ir_para_proxima_pagina.is_enabled():
                botao_ir_para_proxima_pagina.click()
                sleep(random.randint(2, 5))
            else:  # Si no hay botón "Avançar", se llegó al final
                logging.info("Se llegó a la última página.")
                break

        except Exception as e:
            # Registra el error en el archivo de logs y cierra la aplicación
            logging.error(f"Error al intentar avanzar de página: {e}")
            break
