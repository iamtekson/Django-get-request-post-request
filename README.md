# About this repo
This repo contain the simple get request and post request on the Django. I use postgres database for this project.

### Get Request with django
add following code in views.py file:
```
def index(request):
    form = Form.objects.all()

    context = {
        'form': form
    }
    return render(request, 'index.html', context)
```
add your url as `path('form', views.form, name = 'form'),`
### Post Request with django
```
def submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']


        info = Form(name=name, email=email, password=password)
        info.save()

        return render(request, 'submit.html')
```
add your url as `path('submit', views.submit, name = 'submit'),`

### Start with this project
* Create the virtual enviroment
 `pip install venv`
* Install requirement.txt file
`pip install -r requirement.txt`
* Migrate database
```
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
```
* Create superuser
`python manage.py createsuperuser`
* Run your project
`python manage.py runserver`
Your project is running in localhost://8000
* Add data
You can add the data through the form or you can add the data through admin dashboard.

