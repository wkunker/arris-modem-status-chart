#!/usr/bin/python

import lxml.html
import requests
import re
import json

##################################################
# User config
##################################################
# citystate is used to find weather information at
#   which can be compared against the modem status.
# citystate takes the format 'City,st'
citystate = 'Louisville,ky'

# modemaddr is the address of the modem displaying 
#   power/freq/mod/other data.
modemaddr = 'http://192.168.100.1/phy.html'

##################################################
##################################################
##################################################

page = requests.get(modemaddr)
tree = lxml.html.fromstring(page.text)

def xpath(xpath_str):
    return tree.xpath(xpath_str)[0].rstrip()

status_data = {
    "rf_parameters": {
        "downstream": {
            'frequency': xpath('/html/body/table[4]/tr[2]/td[3]/text()'),
            'power': xpath('/html/body/table[4]/tr[2]/td[4]/text()'),
            'signal_to_noise_ratio': xpath('/html/body/table[4]/tr[3]/td[3]/text()'),
            'modulation': xpath('/html/body/table[4]/tr[4]/td[3]/text()')
        },
        "upstream": {
            'frequency': xpath('/html/body/table[4]/tr[6]/td[3]/text()'),
            'power': xpath('/html/body/table[4]/tr[6]/td[4]/text()'),
            'channel_type': xpath('/html/body/table[4]/tr[7]/td[3]/text()'),
            'symbol_rate': xpath('/html/body/table[4]/tr[9]/td[3]/text()'),
            'modulation': xpath('/html/body/table[4]/tr[11]/td[3]/text()')
        }
    },
    "status": {
        "system_uptime": xpath('/html/body/table[6]/tr[1]/td[2]/text()'),
        "computers_detected": xpath('/html/body/table[6]/tr[2]/td[2]/text()'),
        "cm_status": xpath('/html/body/table[6]/tr[3]/td[2]/text()'),
        "time_and_date": xpath('/html/body/table[6]/tr[4]/td[2]/text()')
    }
}

page = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + citystate + '&units=imperial')

r = requests.post('http://127.0.0.1:8080/modemstatus/', data={'status_data': json.dumps(status_data), 'weather_data': json.dumps(page.json())})

print r.content

