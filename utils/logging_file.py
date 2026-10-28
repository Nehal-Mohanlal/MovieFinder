import logging 

logging.basicConfig(
    level=logging.INFO,
    filename="./logs/app_logs.log", 
    filemode='a',
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
) 

logger = logging.getLogger()

