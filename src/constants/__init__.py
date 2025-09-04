import datetime

# constants for log configurations
LOG_DIR = 'logs'
LOG_FILE = f"{datetime.now().strftime('%m-%d-%Y-%H-%M-%S')}.log"
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3