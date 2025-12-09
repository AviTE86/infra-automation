import logging

def setup_logging():
    logging.basicConfig(
        filename='provisioning.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger("infra_sim_log")

logger = setup_logging()

def log_message(message, level="info"):
    if level == "error":
        logger.error(message)
    else:
        logger.info(message)
    print(message)