import logging

def logs():
    # Configuração do logger
    logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()
    return logger