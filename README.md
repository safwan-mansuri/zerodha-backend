# Zerodha-Backend Service

This service adds the data from coming from schedular and stores it in the redis database (i.e list), it is also responsible to fetch the data from the redis.

### endpoints

1. ` POST https://zerodha-backend-stock.herokuapp.com/stock_details/today_data`
2. ` GET https://zerodha-backend-stock.herokuapp.com/stock_details/`

### Run locally

1. `clone the repo`
2. `create python3 virtualenv`
3.  RUN `pip install -r requirements.txt`
4.  RUN `python manage.py migrate`
5.  RUN `python manage.py runserver

### using Docker

1. docker-compose build
2. docker-compose up.
