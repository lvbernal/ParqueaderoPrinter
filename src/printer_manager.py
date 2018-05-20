# -*- coding: utf-8 -*-
"""Printer controller"""

import urllib.request
import json
from escpos import printer
from escpos import exceptions
import config


class PrinterManager(object):
    """Perform printer operations"""

    def __init__(self):
        self.header = ""
        self.contract = ""
        self.ready = False

    def configure(self):
        """Obtain configuration from server"""
        ptr = self.get_printer()

        if ptr is None:
            return False

        self._download_printer_config(ptr)
        ptr.cut()
        ptr.close()
        return self.ready

    def _download_printer_config(self, ptr):
        try:
            ptr.text(config.LOADING_CONFIG + "\n")

            with urllib.request.urlopen(config.CONFIG_URL) as url:
                response = json.loads(url.read().decode())
                header = response.get("receiptHeader", "")
                contract = response.get("receiptContract", "")

                self.header = header if header is not None else ""
                self.contract = contract if contract is not None else ""
                self.ready = True

            ptr.text(config.CONFIG_READY + "\n")

        except urllib.error.HTTPError:
            ptr.text(config.ERROR_BAD_ID)
        except urllib.error.URLError:
            ptr.text(config.ERROR_BAD_URL)
        finally:
            ptr.text("\n")

    def print(self, vehicle):
        """Print receipt for vehicle"""
        return vehicle

    def _print_header(self, ptr):
        ptr.set(align='center')
        ptr.text(self.header)
        ptr.text("\n")

    def _print_contract(self, ptr):
        ptr.set(align='left')
        ptr.text(self.contract)
        ptr.text("\n")

    def get_printer(self):
        """Create printer instance from configuration"""
        try:
            return printer.Usb(config.ID_VENDOR, config.ID_PRODUCT, 0, config.IN_EP, config.OUT_EP)
        except exceptions.Error:
            return None
