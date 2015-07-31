Arris TM502G Status Chart
====
Crude scraper/server/client combo for collecting/displaying Arris TM502G cable modem data over time using DRF and jQuery/Google Visualization.

*Installation*
- Clone to location such as "/arris-modem-status-chart/"
- Nginx config
    
    location / {
        root /arris-modem-status-chart/frontend/public;
    }
    
    location /modemstatus {
        proxy_pass http://127.0.0.1:8080/modemstatus;
    }

- `virtualenv env`, `source env/bin/activate`, `pip install -r requirements.txt`, `./manage.py migrate`
- `source env/bin/activate`, `./manage.py runserver 0.0.0.0:8080` or systemd/supervisor/gunicorn/whatever
- Change backend/scraper/scraper.py 'citystate' value to nearby location.
- Install the scraper cron job (test it first, ya dingus!)
>`* * * * * /arris-modem-status-chart/backend/env/bin/python /arris-modem-status-chart/backend/scraper/scraper.py`

