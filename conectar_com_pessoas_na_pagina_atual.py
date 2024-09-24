from time import sleep  # Importa sleep para pausar la ejecución
import logging  # Importa logging para registrar errores
import random  # Importa random para generar pausas aleatorias
# Permite seleccionar elementos en la página por su localización
from selenium.webdriver.common.by import By
# Importa funciones de scroll y la función de verificar ventana
from scroll import scroll_pagina_totalmente_para_baixo, scroll_pagina_totalmente_para_cima, verificar_ventana_abierta

def conectar_com_pessoas_na_pagina_atual(driver, conexoes_enviadas=0):
    # Define el límite de conexiones que se pueden enviar por día
    limite_diario = 20

    if conexoes_enviadas >= limite_diario:
        logging.info("Se alcanzó el límite diario de conexiones.")
        return conexoes_enviadas  # Retorna el valor sin intentar conectar con más personas

    try:
        # Verifica si la ventana está abierta antes de realizar cualquier acción
        if not verificar_ventana_abierta(driver):
            return conexoes_enviadas  # Detiene si la ventana ya está cerrada

        # Hace scroll hacia abajo para cargar más elementos en la página
        scroll_pagina_totalmente_para_baixo(driver)
        # Vuelve a hacer scroll hacia arriba
        scroll_pagina_totalmente_para_cima(driver)

    except Exception as error:
        # Registra cualquier error que ocurra durante el scroll en el archivo de logs
        logging.error(f"Error al hacer scroll: {error}")

    # Pausa la ejecución por un tiempo aleatorio entre 2 y 5 segundos simulando el comportamiento humano
    sleep(random.randint(2, 5))

    try:
        # Encuentra todos los botones "Convidar" (Conectar) en la página, espera hasta que los botones sean visibles
        botoes_conectar = driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'Convidar')]")

        # Si no se encontraron personas, continúa a la siguiente página
        if not botoes_conectar:
            logging.info("No se encontraron personas en esta página.")
            return conexoes_enviadas  # Retorna el mismo número de conexiones sin modificar

        for botao_conectar in botoes_conectar:
            # Verifica que no se hayan enviado más conexiones que el límite diario
            if conexoes_enviadas < limite_diario:
                # Verifica si la ventana sigue abierta antes de realizar acciones
                if not verificar_ventana_abierta(driver):
                    return conexoes_enviadas  # Detiene si la ventana ya está cerrada

                # Pausa la ejecución por un tiempo aleatorio entre 2 y 5 segundos
                sleep(random.randint(2, 5))
                # Usa JavaScript para hacer clic en el botón "Conectar"
                botao_conectar.click()
                # Pausa la ejecución por un tiempo aleatorio entre 2 y 5 segundos
                sleep(random.randint(2, 5))

                try:
                    # Encuentra el botón para enviar la solicitud sin un mensaje personalizado
                    botao_enviar_sem_nota = driver.find_element(By.XPATH, "//button[@aria-label='Enviar sem nota']")
                    # Pausa la ejecución por un tiempo aleatorio entre 2 y 5 segundos
                    sleep(random.randint(2, 5))
                    # Hace clic en el botón "Enviar"
                    botao_enviar_sem_nota.click()
                    # Incrementa el contador de conexiones enviadas
                    conexoes_enviadas += 1
                    # Pausa la ejecución por un tiempo aleatorio entre 2 y 5 segundos
                    sleep(random.randint(2, 5))
                except Exception as e:
                    logging.error(f"Error al enviar la conexión: {e}")
            else:
                logging.info("Se alcanzó el límite diario de conexiones.")
                break

        return conexoes_enviadas  # Devuelve el número actualizado de conexiones

    except Exception as error:
        # Registra cualquier error en el archivo de logs
        logging.error(f"Error al conectar con personas: {error}")
        return conexoes_enviadas
