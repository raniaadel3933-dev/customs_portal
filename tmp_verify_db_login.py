import os

os.environ['DB_HOST'] = '127.0.0.1'
os.environ['DB_USER'] = 'missing_user'
os.environ['DB_PASSWORD'] = 'wrong_password'
os.environ['DB_NAME'] = 'missing_db'
os.environ['DB_PORT'] = '3306'
os.environ['FLASK_DEBUG'] = '0'

import app

client = app.app.test_client()
resp = client.get('/')
print('status=', resp.status_code)
print('login_present=', 'login' in resp.data.decode('utf-8', 'ignore').lower())
print('has_valid_db_config=', app.has_valid_db_config())
print('db_user=', app.db_config['user'])
