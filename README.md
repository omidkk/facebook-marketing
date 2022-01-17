To run this project it is needed to install:

Python 3.8

Run the commend to install the requirments:

```
pip install -r requirments.py
```

It is necessary to create, and configure the **.env** file.

```
FLASK_APP=start.py
FLASK_ENV=production
ACCESS_TOKEN=<>
AD_ACCOUNT_ID=<>
APP_SECRET=<>
APP_ID=<>
PAGE_ID=<>
```

To run the flask app:
```
python start.py
```
---------
To run with docker:
```
docker build -t ounass .
docker run --env-file .env -d -p 5000:5000 ounass
```