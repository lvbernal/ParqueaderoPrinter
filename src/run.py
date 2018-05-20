# -*- coding: utf-8 -*-
"""Application server"""

import time
from queue import Queue
from threading import Thread
import cherrypy
from printer_manager import PrinterManager


class Server(object):
    """CherryPy HTTP server"""

    def __init__(self):
        self.queue = Queue()
        self.printer_manager = PrinterManager()

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def printreceipt(self):
        """Server's print endpoint. Queue the print request and return a 200 code"""
        query = cherrypy.request.json
        self.queue.put_nowait(query)
        return "Ok"

    def process_queue(self):
        """Read items from queue and send them to print"""
        while True:
            item = self.queue.get()

            if item is not None:
                printed = self.printer_manager.print(item)

                if not printed:
                    self.queue.put_nowait(item)

            time.sleep(1)

    def configure(self):
        """Initialize printer manager"""
        return self.printer_manager.configure()


if __name__ == "__main__":
    # Configure cherrypy server
    CONFIG = {"server.socket_host": "0.0.0.0", "server.socket_port": 80}
    cherrypy.config.update(CONFIG)

    # Create server and worker thread instances
    SERVER = Server()
    READY = SERVER.configure()

    if READY:

        WORKER = Thread(target=SERVER.process_queue)

        # Run application
        WORKER.start()
        cherrypy.quickstart(SERVER)
