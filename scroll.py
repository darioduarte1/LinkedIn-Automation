import logging  # Importa logging para registrar errores

# Función para hacer scroll hacia abajo


def scroll_pagina_totalmente_para_baixo(driver):
    # Desplazar la página totalmente hacia abajo
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Función para hacer scroll hacia arriba


def scroll_pagina_totalmente_para_cima(driver):
    # Desplazar la página totalmente hacia arriba
    driver.execute_script("window.scrollTo(0, 0);")

# Función para verificar si la ventana del navegador sigue abierta


def verificar_ventana_abierta(driver):
    try:
        # Verifica si el navegador está activo
        driver.current_window_handle
        return True
    except Exception as e:
        logging.error(f"Navegador cerrado o ventana no disponible: {e}")
        return False
