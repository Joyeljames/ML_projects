import logging
from  datetime import datetime
import os

log_file = f'{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.log'
logs_path = os.path.join(os.getcwd(),'logs',log_file)
os.makedirs(logs_path,exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path,log_file)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    logging.info('Logging has started')
  
