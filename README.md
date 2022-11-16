# Metsenat

### create virtual environment
```
python -m venv env or python3 -m venv env
```

### activate virtual environment
linux 
```bash
source env/bin/activate
```

windows
```bash
env\Scripts\activate
```

### install packages
```bash
pip install -r requirements.txt
```

### execute models
```bash
python manage.py migrate 
```

### run project
```bash
python manage.py runserver
```


# API Links:

admin
``` bash
* api/v1/common/login/ - LOGIN API FOR ADMIN (POST)
```

sponsor
```bash
* api/v1/common/register/ - REGISTER SPONSOR (POST)
* api/v1/common/sponsors/ - SPONSOR LIST (POST)
* api/v1/common/sponsors/detail/1/ - DETAIL SPONSOR (GET)
* api/v1/common/sponsors/detail/1/ - UPDATE SPONSOR (PUT)
* api/v1/common/sponsors/detail/1/ - DELETE SPONSOR (DELETE)
```

university
```bash
* /api/v1/common/university/create/ - UNIVERSITY LIST (GET)
* /api/v1/common/university/create/ - UNIVERSITY CREATE (POST)
```

student
```bash
* api/v1/common/students/ - STUDENTS LIST (GET)
* api/v1/common/student/1/ - DETAIL STUDENT (GET)
* api/v1/common/student/update/1/ - UPDATE SPONSOR (PUT)
* api/v1/common/student/1/ - DELETE STUDENT (DELETE)
```

sponsorship
```bash
* api/v1/common/sponsorship/create -  SPONSORSHIP CREATE (POST)
* api/v1/common/sponsorship/update/1/ - SPONSORSHIP DETAIL (GET)
* api/v1/common/sponsorship/update/1/ - SPONSORSHIP UPDATE  (PUT)
* api/v1/common/sponsorship/update/1/ - SPONSORSHIP DELETE (DELETE)
```


dashboard
```bash
* api/v1/common/dashboard/- DASHBOARD (GET)
* api/v1/common/dashboard/sponsor/ - DASHBOARD SPONSOR LIST (GET)
* api/v1/common/dashboard/students - DASHBOARD SPONSOR LIST (GET)
```