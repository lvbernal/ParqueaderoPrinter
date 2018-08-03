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
$ pip3 install six>=1.11.0 cheroot portend cherrypy libusb python-escpos python-dateutil
```

Get the printer settings:

``` sh
$ lsusb
    Bus 020 Device 006: ID 0fe6:811e ICS Advent Parallel Adapter

$ lsusb -vvv -d 0fe6:811e | grep bEndpointAddress
    bEndpointAddress     0x02  EP 2 OUT
    bEndpointAddress     0x82  EP 2 IN
```

Configure printer:

``` python
# file config.py
ID_VENDOR = 0x0fe6
ID_PRODUCT = 0x811e
IN_EP = 0x82
OUT_EP = 0x02
```

## Run the application

Execute:

``` sh
$ python3 src/run.py
```

The application obtains the configuration from the server. The expected response is:

``` javascript
{
  "id": 3,
  "config": "http://192.168.1.101/printreceipt",
  "receiptHeader": "Relevant information\r\nAbout the parking lot",
  "receiptContract": "Usage contract."
}
```

Expected input in the /printreceipt endpoint:

``` javascript
// Check in
{
    "plate": "ABC123",
    "vehicle_type": "pickup",
    "check_in": "2018-03-27T20:11:42.9947971",
    "check_out": "0001-01-01T00:00:00",
    "helmets": 2,
    "done": 0,
    "fee": 0.0,
    "fee_detail": {
        "baseValue": 1000,
        "feeValue": 500,
        "helmetsBase": 500,
        "helmetsFee": 0
    }
}
```

```javascript
// Check out
{
    "plate": "ABC123",
    "vehicle_type": "pickup",
    "check_in": "2018-03-27T20:11:42.9947971",
    "check_out": "0001-01-01T00:00:00",
    "helmets": 2,
    "done": 1,
    "fee": 5000.0,
    "fee_detail": {
        "baseFee": 1000,
        "additionalHours": 3,
        "additionalFee": 3000,
        "helmetsTotal": 1000
    }
}
```
