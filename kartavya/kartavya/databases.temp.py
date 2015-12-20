import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default='mysql://USERNAME:PASSWORD@localhost/DATABASENAME')
}