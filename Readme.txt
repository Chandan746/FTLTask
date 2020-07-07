This application is to add the activity periods to user by the custom management command and get all activity periods of user in JSON
install python-3.8.3

Steps:
    You cn create env by command (python -m venv "env name")
    activate the env
1. pip install -r requirements.txt
2. python manage.py makemigrations
3. python mange.py migrate
4. python mange.py createsuperuser
5. python mange.py runserver
6. Signup User
7. Add activity management command line:
    7.1 In new bash activate the env if there
    7.2 cd to project folder
    7.3 python manage.py activity 1 Feb-3-2020-1:33-PM Feb-3-2020-3:54-PM
    7.4 python manage.py activity 2 Feb-4-2020-1:33-AM Feb-4-2020-3:54-AM
        activity is command 
        2 is userID 
        Feb-3-2020-1:33-PM is start date 
        Feb-3-2020-3:54-PM is end date
        Note*
        Please follow the order of date and time in same order ("%b-%d-%Y-%I:%M-%p")
        add multiple data 
8. click on getjson to get the output "http://127.0.0.1:8000/getjson/"
