# -*- coding: utf-8 -*-
"""Printer configuration file"""

import texts

# ----- Local ----- #
PARKING_LOT_ID = ""
CODE = ""
LANG = "ES"

# ----- Printer ----- #

ID_VENDOR = 0x0fe6
ID_PRODUCT = 0x811e
IN_EP = 0x82
OUT_EP = 0x02

# ----- Application texts ----- #

if LANG == "ES":
    CI_TEXT = texts.CI_TEXT_ES
    CO_TEXT = texts.CO_TEXT_ES
    HELMETS_TEXT = texts.HELMETS_TEXT_ES
    BASE_TEXT = texts.BASE_TEXT_ES
    HOURS_TEXT = texts.HOURS_TEXT_ES
    HOURS_HELMETS_TEXT = texts.HOURS_HELMETS_TEXT_ES
    CAR = texts.CAR_ES
    PICKUP = texts.PICKUP_ES
    TRUCK = texts.TRUCK_ES
    MOTORBIKE = texts.MOTORBIKE_ES
    BIKE = texts.BIKE_ES
    LOADING_CONFIG = texts.LOADING_CONFIG_ES
    CONFIGURING = texts.CONFIGURING_ES
    CONFIG_READY = texts.CONFIG_READY_ES
    ERROR_BAD_ID = texts.ERROR_BAD_ID_ES
    ERROR_BAD_URL = texts.ERROR_BAD_URL_ES
    DATE_FORMAT = texts.DATE_FORMAT_ES
elif LANG == "EN":
    CI_TEXT = texts.CI_TEXT_EN
    CO_TEXT = texts.CO_TEXT_EN
    HELMETS_TEXT = texts.HELMETS_TEXT_EN
    BASE_TEXT = texts.BASE_TEXT_EN
    HOURS_TEXT = texts.HOURS_TEXT_EN
    HOURS_HELMETS_TEXT = texts.HOURS_HELMETS_TEXT_EN
    CAR = texts.CAR_EN
    PICKUP = texts.PICKUP_EN
    TRUCK = texts.TRUCK_EN
    MOTORBIKE = texts.MOTORBIKE_EN
    BIKE = texts.BIKE_EN
    LOADING_CONFIG = texts.LOADING_CONFIG_EN
    CONFIGURING = texts.CONFIGURING_EN
    CONFIG_READY = texts.CONFIG_READY_EN
    ERROR_BAD_ID = texts.ERROR_BAD_ID_EN
    ERROR_BAD_URL = texts.ERROR_BAD_URL_EN
    DATE_FORMAT = texts.DATE_FORMAT_EN

# ----- Fixed config ----- #

SERVER_URL = ""
CONFIG_URL = SERVER_URL + PARKING_LOT_ID
