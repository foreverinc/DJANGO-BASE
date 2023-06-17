import os

PROJECT_NAME='DJANGO-MAX'
STATE=True #True in Development and False in Production
# static configs 

GITHUB_LINK='https://github.com/'

CLOUD_NAME=''

CLOUD_APIKEY=''

CLOUD_SECRET= os.environ.get('SECRET_KEY')


#database config
DB_NAME=os.environ.get('DB_NAME','DJANGO-BASE')
DB_USER=os.environ.get('DB_USER','postgres')
DB_PASSWORD=os.environ.get('DB_PASSWORD','Drake@2020')
DB_PORT=os.environ.get('PORT',5432)
DB_HOST=os.environ.get('DB_HOST','127.0.0.1')

#allauth config
DEV_SITE=1
PROD_SITE=1

#email config
EMAIL_USER=''
EMAIL_PASSWORD=os.environ.get('EMAIL_PASSWORD','gksznagmjpkzikfg')

