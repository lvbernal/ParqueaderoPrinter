# -*- coding: utf-8 -*-
"""Helper methods"""

from datetime import datetime
from dateutil import parser
import config


def get_vehicle_name(v_type):
    """Return vehicle name from config"""
    v_map = {
        "car": config.CAR,
        "pickup": config.PICKUP,
        "truck": config.TRUCK,
        "motorbike": config.MOTORBIKE,
        "bike": config.BIKE
    }

    return v_map[v_type]


def format_date(date):
    """Format date into printable string"""
    dto = parser.parse(date)
    return datetime.strftime(dto, config.DATE_FORMAT)
