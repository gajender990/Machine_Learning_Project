import logging
import os
from datetime import datetime

## Creating log file
## Naming convention of log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# place and name where log file will get created
logs_path = os.path.join(os.getcwd(),"","logs",LOG_FILE)

# Creation of log file(if file exist append it)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

## Override logging so that it can be imported
logging.basicConfig(
    filename== LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO()
)