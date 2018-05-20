# ParqueaderoPrinter

Simple server application that prints receipts for ParqueaderoApp.

## Development environment

Create and activate virtual environment:

``` sh
$ python3 -m venv env
$ source env/bin/activate
```

Install dependencies:

``` sh
# libusb should be installed in the OS.
$ pip install python-escpos cherrypy python-dateutil libusb
```

Obtain printer settings:

``` sh
$ lsusb
    Bus 020 Device 006: ID 0fe6:811e ICS Advent Parallel Adapter

$ lsusb -vvv -d 0fe6:811e | grep bEndpointAddress
    bEndpointAddress     0x02  EP 2 OUT
    bEndpointAddress     0x82  EP 2 IN
```

Configure printer:

``` python
# config.py
ID_VENDOR = 0x0fe6
ID_PRODUCT = 0x811e
IN_EP = 0x82
OUT_EP = 0x02
```

## Running the application

Execute:

``` sh
$ python src/run.py
```

The application obtains the configuration from the server. The expected response is:

``` javascript
{
  "id": 3,
  "config": "http://192.168.1.101/printreceipt",
  "receiptHeader": "Title\r\nIdentifier\r\nAddress\r\nCity, Country",
  "receiptContract": "Usage contract."
}
```

Expected input in the /printreceipt endpoint:

``` javascript
{
    'plate': 'ABC123',
    'vehicle_type': 'pickup',
    'check_in': '2018-03-27T20:11:42.9947971', UTC
    'check_out': '0001-01-01T00:00:00',
    'helmets': 2,
    'done': False,
    'fee': 0.0
}
```
