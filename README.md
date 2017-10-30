# NAAC_Portal
Portal for GGSIPU Faculty Data Acquisition System Report

### Usage
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Start up the MySQL server and make sure it has:
- Database called 'naac_portal'. (Need to be created the first time)
- User ```root```, with no/empty password.

https://github.com/SDC-USICT/NAAC_Portal/blob/master/naac_portal/settings.py#L94-L103

You can also use your own config but make sure to not commit
it because then git merge conflicts may arise.

