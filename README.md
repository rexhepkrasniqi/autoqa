# AutoQA


## Set up the project


<br>

Dependencies: 
- python
- playwright [https://playwright.dev/python/docs/intro] 


<br>

Setting up:

<br>
<br>

Create virtual environment: 

` python3 -m virtualenv venv ` 

` source venv/bin/activate ` 

<br>

Install dependencies:

` pip install -r requirements.txt `

` playwright install `

<br>

Move to the main directory:

` cd autoqa `

<br>

Create and run migrations:

` python manage.py makemigrations app `

` python manage.py migrate app `

` python manage.py loaddata data.json ` :   this helps you out with data for testing www.kutia.net home page

<br>

Create superuser:

` manage.py createsuperuser `

<br>

Run the project:

` python manage.py runserver 0:8000 `


---

<br>

You can run tests on tasks list view, using select action at the top.

<br>

<br>

### Enjoy :)

