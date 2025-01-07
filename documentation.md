# **Bettips App Documentation**

## **Project Overview**
Bettips is a Django-based web application designed to provide users with various betting tips and game predictions. The app includes multiple endpoints to fetch game data, such as all games, yesterday's games, and games from the previous two days. The project is deployed using Nginx and Gunicorn on an Ubuntu server.

---

## **Technology Stack**
- **Backend Framework:** Django
- **Web Server:** Nginx
- **Application Server:** Gunicorn
- **Database:** PostgreSQL (or SQLite for development)
- **Environment:** Ubuntu Server

---

## **Project Structure**
```plaintext
bettipsbackend-master/
├── api/
│   ├── __init__.py
│   ├── urls.py
│   ├── views.py
│   └── models.py
├── bettips/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── static/
```

---

## **Endpoints**
The API provides the following endpoints:

### **Base URL**
```plaintext
http://<your-server-ip>/
```

### **1. Home Endpoint**
**URL:** `/`
- **Method:** GET
- **Description:** Displays a welcome message or the home page.

### **2. All Games Endpoint**
**URL:** `/all_games`
- **Method:** GET
- **Description:** Returns a list of all available games.

### **3. Yesterday's Games Endpoint**
**URL:** `/yesterday_games`
- **Method:** GET
- **Description:** Returns a list of games that were played yesterday.

### **4. Previous Two Days' Games Endpoint**
**URL:** `/previous_two_days_games`
- **Method:** GET
- **Description:** Returns a list of games that were played in the last two days.

---

## **API Configuration**

### **Project URL Configuration (bettips/urls.py)**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls'))
]
```

### **API URL Configuration (api/urls.py)**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all_games', views.all_games, name='all_games'),
    path('yesterday_games', views.yesterday_games, name='yesterday_games'),
    path('previous_two_days_games', views.previous_two_days_games, name='previous_two_days_games'),
]
```

---

## **Views (api/views.py)**
```python
from django.http import JsonResponse

# Home view
def home(request):
    return JsonResponse({"message": "Welcome to Bettips API!"})

# All games view
def all_games(request):
    games = ["Game 1", "Game 2", "Game 3"]
    return JsonResponse({"all_games": games})

# Yesterday's games view
def yesterday_games(request):
    games = ["Yesterday's Game 1", "Yesterday's Game 2"]
    return JsonResponse({"yesterday_games": games})

# Previous two days' games view
def previous_two_days_games(request):
    games = ["Day -2 Game 1", "Day -1 Game 2"]
    return JsonResponse({"previous_two_days_games": games})
```

---

## **Deployment Setup**

### **1. Gunicorn Configuration**
Ensure Gunicorn is installed and properly configured to serve your Django app:

```bash
pip install gunicorn
```

Run Gunicorn to serve your project:

```bash
gunicorn --workers 3 --bind unix:/run/gunicorn.sock bettips.wsgi:application
```

### **2. Nginx Configuration**
Create an Nginx configuration file:

```plaintext
/etc/nginx/sites-available/bettips
```

Sample Nginx configuration:
```nginx
server {
    listen 80;
    server_name <your-server-ip>;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        alias /home/ubuntu/bettips/static/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```

Enable the Nginx configuration:
```bash
sudo ln -s /etc/nginx/sites-available/bettips /etc/nginx/sites-enabled
```

Restart Nginx:
```bash
sudo systemctl restart nginx
```

---

## **Static Files**
Ensure static files are collected and properly served by Nginx:

```bash
python manage.py collectstatic
sudo chown -R www-data:www-data /home/ubuntu/bettips/static/
sudo chmod -R 755 /home/ubuntu/bettips/static/
```

---

## **Systemd Service for Gunicorn**
Create a systemd service file for Gunicorn:

```plaintext
/etc/systemd/system/gunicorn.service
```

Sample Gunicorn service configuration:
```ini
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/home/ubuntu/bettipsbackend-master
ExecStart=/home/ubuntu/venv/bin/gunicorn --workers 3 --bind unix:/run/gunicorn.sock bettips.wsgi:application

[Install]
WantedBy=multi-user.target
```

Reload systemd, start Gunicorn, and enable it to start on boot:

```bash
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

---

## **Common Issues and Fixes**

### **1. 404 Not Found for Static Files**
- Ensure Nginx is correctly pointing to the static file directory.
- Ensure the static files have the correct permissions.

### **2. 502 Bad Gateway**
- Check if Gunicorn is running:
  ```bash
  sudo systemctl status gunicorn
  ```
- Check the Nginx error log:
  ```bash
  sudo tail -f /var/log/nginx/error.log
  ```

---

## **Accessing the API**
To access the endpoints:

```plaintext
http://<your-server-ip>/all_games
http://<your-server-ip>/yesterday_games
http://<your-server-ip>/previous_two_days_games
```

