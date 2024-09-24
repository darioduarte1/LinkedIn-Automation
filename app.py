import logging
from iniciar_automacao import iniciar_automacao


# Configura el sistema de logging. Los mensajes de error se escribirán en el archivo erros.log en modo "append" (agregar al final del archivo sin sobrescribir)
logging.basicConfig(filename='erros.log', filemode='a', level=logging.ERROR)

iniciar_automacao()
