# Django Tasker System

### Installation

* Without Docker

```Bash
git clone git@gitlab.com:21labs/tasker/tasker.git
cd tasker
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd tasker
./manage.py migrate
./manage.py createsuperuser
```

Run server

`./manage.py runserver`

Visit website

[http://127.0.0.1:8000](http://127.0.0.1:8000)

Visit admin website

[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

### Application Scenario

* Details in scenario.txt
