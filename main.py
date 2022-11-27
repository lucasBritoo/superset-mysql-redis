import os

os.chdir("/home/vagrant")
os.system("sudo yum update -y")
os.system("sudo yum install -y python3")

os.system("sudo yum install gcc gcc-c++ libffi-devel python3-devel python3-pip python3-wheel openssl-devel cyrus-sasl-devel openldap-devel -y")
os.system("sudo pip3 install --upgrade pip")
os.system("sudo yum update")

os.system("sudo yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm")
os.system("sudo yum install -y postgresql12-server")
os.system("sudo /usr/pgsql-12/bin/postgresql-12-setup initdb")
os.system("sudo systemctl enable postgresql-12")
os.system("sudo systemctl start postgresql-12")
os.system("export PATH=/usr/pgsql-12/bin/pg_config:$PATH")
#/var/lib/pgsql/12/data


os.system("pip3 install psycopg2")
os.system("pip3 install itsdangerous==1.1.0")
os.system("pip3 install sqlalchemy==1.3.24")
os.system("pip3 install flask-appbuilder==3.1.1")
os.system("pip3 install werkzeug==0.16.1")
os.system("pip3 install flask-WTF==0.14.2")
os.system("pip3 install wtforms==2.3.3 ")
os.system("pip3 install dataclasses")
os.system("pip3 install pillow")

os.system("pip3 install apache-superset")
os.system("export FLASK_APP=superset")
os.system("/usr/local/bin/superset fab create-admin --username admin --firstname admin_admin --lastname admin-teste --email admin@gmail.com --password admin123")
os.system("/usr/local/bin/superset load_examples")
os.system("/usr/local/bin/superset db upgrade")
os.system("/usr/local/bin/superset init")
os.system("/usr/local/bin/gunicorn -w 2 --timeout 2000 -b 0.0.0.0:8088 'superset.app:create_app()' --daemon")



