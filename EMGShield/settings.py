import logging

POSSIBLE_PORTS = [
    # Linux
    '/dev/ttyACM0',
    # MAC
    '/dev/tty.usbmodem1411',
    '/dev/tty.usbmodem1421',
    # Windows
    'com1',
    'com2',
    'com3',
    'com4',
    'com5'
]

BAUDRATE = 57600

LOG_LEVEL = logging.DEBUG
LOG_FORMAT = '%(asctime)s [%(levelname)-5.5s] %(message)s'
LOG_DATE_FORMAT = '%m/%d/%Y %I:%M:%S %p'
LOG_FILE = 'emg_shield.log'
LOG_CONSOLE = True

TEMP_SCAN = 'temp.json'