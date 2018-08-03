# -*- coding: utf-8 -*-
"""Printer controller"""

import socket
import urllib.request
import json
from escpos import printer
from escpos import exceptions
import config
import helpers


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
        self._print_ip_address(ptr)
        ptr.text("--")
        ptr.cut()
        ptr.close()
        return self.ready

    def _download_printer_config(self, ptr):
        try:
            ptr.set(align='center', width=1, height=1)
            ptr.text(config.LOADING_CONFIG + "\n")
            ptr.set(align='left', width=1, height=1)
            ptr.text(config.CONFIGURING + "\n")

            with urllib.request.urlopen(config.CONFIG_URL) as url:
                response = json.loads(url.read().decode())
                header = response.get("receiptHeader", "")
                contract = response.get("receiptContract", "")

                self.header = header if header is not None else ""
                self.contract = contract if contract is not None else ""
                self.ready = True

            ptr.text(config.CONFIG_READY)

        except urllib.error.HTTPError:
            ptr.text(config.ERROR_BAD_ID)
        except urllib.error.URLError:
            ptr.text(config.ERROR_BAD_URL)
        finally:
            ptr.text("\n")

    def _print_ip_address(self, ptr):
        try:
            skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            skt.connect(("8.8.8.8", 80))
            address = skt.getsockname()[0]
            skt.close()
            ptr.text("http://" + address + "/printreceipt")
        except OSError:
            pass
        finally:
            ptr.text("\n")

    def print(self, vehicle):
        """Print receipt for vehicle"""
        done = vehicle.get("done", False)

        ptr = self.get_printer()
        self._print_header(ptr)
        ptr.text("\n\n")
        self._print_plate(ptr, vehicle)
        ptr.text("\n")
        self._print_common_content(ptr, vehicle)
        ptr.text("\n")

        if done:
            self._print_checkout_info(ptr, vehicle)
            ptr.text("\n\n")
            self._print_fee_details(ptr, vehicle)
        else:
            ptr.text("\n")
            self._print_checkin_info(ptr, vehicle)
            ptr.text("\n")
            self._print_plate_qr(ptr, vehicle)
            ptr.text("\n\n")
            self._print_contract(ptr)

        ptr.text("\n\n")
        self._print_footer(ptr)

        ptr.cut()
        ptr.close()
        return True

    def _print_header(self, ptr):
        ptr.set(align='center', width=1, height=1)
        ptr.text(self.header)

    def _print_plate(self, ptr, vehicle):
        plate = vehicle.get("plate", "")
        vehicle_type = vehicle.get("vehicle_type", "")
        v_str = helpers.get_vehicle_name(vehicle_type)
        ptr.set(align='center', width=2, height=2)
        ptr.text(v_str + " " + plate)

    def _print_common_content(self, ptr, vehicle):
        helmets = vehicle.get("helmets", 0)
        checkin = vehicle.get("check_in", "")
        ci_str = helpers.format_date(checkin)

        ptr.set(align='center', width=1, height=1)
        if helmets > 0:
            ptr.text(config.HELMETS_TEXT + ": " + str(helmets) + "\n")
        ptr.text("\n")
        ptr.text(config.CI_TEXT + ci_str)

    def _print_checkout_info(self, ptr, vehicle):
        checkout = vehicle.get("check_out", "")
        co_str = helpers.format_date(checkout)
        ptr.text(config.CO_TEXT + co_str)

    def _print_fee_details(self, ptr, vehicle):
        fee_detail = vehicle.get("fee_detail", None)
        helmets = vehicle.get("helmets", 0)
        fee = vehicle.get("fee", 0)

        ptr.set(align='left')
        ptr.text(config.BASE_TEXT + ": \t\t$" + str(fee_detail["baseFee"]) + "\n")
        ptr.text(config.HOURS_TEXT + "(" + str(int(fee_detail["additionalHours"])) + "): \t\t$" +
                 str(fee_detail["additionalFee"]) + "\n")

        if helmets > 0:
            ptr.text(config.HELMETS_TEXT + ": \t\t$" + str(fee_detail["helmetsTotal"]) + "\n")

        ptr.set(align='center', width=2, height=2)
        ptr.text("\n")
        ptr.text("$" + str(fee))

    def _print_checkin_info(self, ptr, vehicle):
        fee_detail = vehicle.get("fee_detail", None)
        helmets = vehicle.get("helmets", 0)

        ptr.set(align='left')
        ptr.text(config.BASE_TEXT + ": \t\t$" + str(fee_detail["baseValue"]) + "\n")
        ptr.text(config.HOURS_TEXT + ": \t\t$" + str(fee_detail["feeValue"]) + "\n")

        if helmets > 0:
            ptr.text(config.HELMETS_TEXT + ": \t\t$" + str(fee_detail["helmetsBase"]) + "\n")

            helmets_fee = fee_detail["helmetsFee"]
            if helmets_fee > 0:
                ptr.text(config.HOURS_HELMETS_TEXT + ": \t\t$" + str(helmets_fee) + "\n")

    def _print_plate_qr(self, ptr, vehicle):
        plate = vehicle.get("plate", "")
        ptr.qr(plate, size=8)

    def _print_contract(self, ptr):
        ptr.set(align='left')
        ptr.text(self.contract)

    def _print_footer(self, ptr):
        ptr.set(align='center')
        ptr.text("www.parqueaderoapp.com")

    def get_printer(self):
        """Create printer instance from configuration"""
        try:
            return printer.Usb(config.ID_VENDOR, config.ID_PRODUCT, 0, config.IN_EP, config.OUT_EP)
        except exceptions.Error:
            return None
