# -*- coding: utf-8 -*-
"""Printer configuration file"""

# ----- Local ----- #
PARKING_LOT_ID = "abc-123-xyz-321"
ID_VENDOR = 0x0fe6
ID_PRODUCT = 0x811e
IN_EP = 0x82
OUT_EP = 0x02

# ----- Application texts ----- #
CHECKIN = "Ingreso"
CHECKOUT = "Salida"
BASE = "Base"
CAR = "CARRO"
PICKUP = "CAMIONETA"
TRUCK = "CAMION"
MOTORBIKE = "MOTO"
BIKE = "BICICLETA"
HELMETS = "Cascos"

LOADING_CONFIG = "ParqueaderoApp. Configurando..."
CONFIG_READY = "Impresora lista."
ERROR_BAD_ID = "Error: El Id del parqueadero no es valido."
ERROR_BAD_URL = "Error: La url del servidor no es valida o no hay acceso a internet."

# ----- Fixed variables ----- #
BASE_CONFIG_URL = "server_url"
CONFIG_URL = BASE_CONFIG_URL + PARKING_LOT_ID
DATE_FORMAT = "%d-%m-%Y %I:%M:%S %p"
