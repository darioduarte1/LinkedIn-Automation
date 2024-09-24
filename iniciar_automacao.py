import random  # Importa random para generar pausas aleatorias
from time import sleep  # Importa sleep para pausar la ejecución
# Importa la función para iniciar el driver
from iniciar_driver import iniciar_driver
# Importa la función para conectar
from conectar_com_pessoas_na_pagina_atual import conectar_com_pessoas_na_pagina_atual
# Importa la función para avanzar a la próxima página
from ir_para_proxima_pagina import ir_para_proxima_pagina
import logging  # Importa logging para registrar errores


def iniciar_automacao():
    # Inicia el driver y el objeto de espera
    driver, wait = iniciar_driver()

    # Verificar si el driver fue inicializado correctamente
    if driver is None or wait is None:
        logging.error(
            "No se pudo iniciar el driver. Finalizando la automatización.")
        return

    # Define la palabra clave para la búsqueda en LinkedIn
    palavra_chave = "Full%20Stack%20Developer"

    # URL de búsqueda en LinkedIn con la palabra clave
    link_pesquisa_por_palavra_chave = f'https://www.linkedin.com/search/results/people/?keywords={
        palavra_chave}&origin=SWITCH_SEARCH_VERTICAL&sid=oJd'

    # Abre el enlace de búsqueda en LinkedIn
    driver.get(link_pesquisa_por_palavra_chave)

    # Espera 30 segundos para permitir que el usuario inicie sesión en LinkedIn si aún no lo ha hecho
    sleep(30)

    # Conecta con personas en la página actual
    conexoes_enviadas = conectar_com_pessoas_na_pagina_atual(driver, 0)

    # Avanza a la siguiente página de resultados
    ir_para_proxima_pagina(driver, conexoes_enviadas)

    # Pausa la ejecución por un tiempo aleatorio entre 2 y 5 segundos simulando el comportamiento humano
    sleep(random.randint(2, 5))
