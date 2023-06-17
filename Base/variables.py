import os

PROJECT_NAME='DJANGO-MAX'

# static configs 

GITHUB_LINK=''

CLOUD_NAME=''

CLOUD_APIKEY=''

CLOUD_SECRET= os.environ.get('SECRET_KEY')


#database config
DB_NAME=os.environ.get('DB_NAME')
DB_USER=os.environ.get('DB_USER')
DB_PASSWORD=os.environ.get('DB_PASSWORD')
DB_PORT=os.environ.get('PORT')
DB_HOST=os.environ.get('DB_HOST')

#allauth config
DEV_SITE=1
PROD_SITE=1

#email config
EMAIL_USER=''
EMAIL_PASSWORD=os.environ.get('EMAIL_PASSWORD','gksznagmjpkzikfg')