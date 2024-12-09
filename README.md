### Installation
1. Git Clone
2. make environment
```python -m venv ./env  ```
3. install pop
4. create my.cnf to configure db information outsite of the project or change location in https://github.com/tomcaz/ch-webapp/blob/main/mysite/settings.py#L83
5. content
    ```
   [client]
   database = phra-db
   user = <username>
   password = <password>
   default-character-set = utf8
   ```
6. activate env ```env\Script\activate```
7. install Django ```python -m pip install Django ``` 
8. install mysqlclient ```pip install mysqlclient ```
9. Database is using mysql.  Table can be load via db.script sql file

### Running Application
```python manage.py runserver```