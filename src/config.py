# -*- coding: utf-8 -*-
"""Printer configuration file"""

# ----- Local ----- #
PARKING_LOT_ID = "1"
ID_VENDOR = 0x0fe6
ID_PRODUCT = 0x811e
IN_EP = 0x82
OUT_EP = 0x02

# ----- Application texts ----- #

# Should have the same length
CI_TEXT = "Ingreso: "
CO_TEXT = "Salida:  "

HELMETS_TEXT = "Cascos"
BASE_TEXT = "Base"
HOURS_TEXT = "Hora adicional"
HOURS_HELMETS_TEXT = "Hora adicional cascos"

CAR = "CARRO"
PICKUP = "CAMIONETA"
TRUCK = "CAMION"
MOTORBIKE = "MOTO"
BIKE = "BICICLETA"

LOADING_CONFIG = "ParqueaderoApp. Configurando..."
CONFIG_READY = "Impresora lista."
ERROR_BAD_ID = "Error: El Id del parqueadero no es valido."
ERROR_BAD_URL = "Error: La url del servidor no es valida o no hay acceso a internet."

# ----- Fixed variables ----- #
BASE_CONFIG_URL = ""
CONFIG_URL = BASE_CONFIG_URL + PARKING_LOT_ID
DATE_FORMAT = "%d-%m-%Y %I:%M:%S %p"