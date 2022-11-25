import os

try:
    #doc https://www.python.org/downloads/release/python-360/
    #externo https://realpython.com/installing-python/#how-to-build-python-from-source-code
    os.system("sudo yum update -y")
    os.system("sudo yum upgrade -y")
    os.system("sudo yum install wget -y")
    os.system("sudo yum install xz")
    os.system("sudo yum -y groupinstall 'Development Tools' -y")
    os.system("sudo yum -y install gcc openssl-devel bzip2-devel libffi-devel -y")
    os.system("wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tar.xz")
    os.system("tar -xf Python-3.6.0.tar.xz")
    os.system("cd Python-3.6.0")
    os.system("./configure --enable-optimizations --with-ensurepip=install")
    os.system("make -j 1")
    os.system("sudo make altinstall")
    os.system("python3.6 --version")
except:
    print("-> OCORREU UM ERRO AO INSTALAR O PYTHON 3.6")

try:
    #doc https://apache-superset.readthedocs.io/en/latest/installation.html
    #externo https://superset.apache.org/docs/installation/installing-superset-from-scratch/
    os.systen("sudo yum install gcc gcc-c++ libffi-devel python-devel python-pip python-wheel openssl-devel cyrus-sasl-devel openldap-devel -y")
    os.system("pip3 install --upgrade pip")
    os.system("pip install virtualenv")
    os.system("python3.6 -m venv venv")
    os.system(". venv/bin/activate")
    os.system("pip install apache-superset")
    os.system("superset db upgrade")
    os.system("export FLASK_APP=superset")
    os.system("superset fab create-admin")
    os.system("superset load_examples")
    os.system("superset init")
    os.system("superset run -p 8088 --with-threads --reload --debugger")
except:
    print("-> OCORREU UM ERRO AO INSTALAR O APACHE-SUPERSET")

try:
    #doc https://dev.mysql.com/doc/refman/8.0/en/linux-installation-yum-repo.html
    os.system("wget https://dev.mysql.com/downloads/file/?id=513590")
    os.system("sudo yum install mysql80-community-release-el7-7.noarch.rpm")
    os.system("sudo yum repolist enabled | grep "mysql.*-community.*"")
    os.system("yum repolist all | grep mysql")
    os.system("sudo yum-config-manager --enable mysql80-community")
    os.system("yum repolist enabled | grep mysql")
    os.system("sudo yum module disable mysql")
    os.system("sudo yum install mysql-community-server")
    os.system("systemctl start mysqld")
    os.system("systemctl status mysqld")
    os.system("mysql -uroot -p")
    os.system("ALTER USER 'root'@'localhost' IDENTIFIED BY 'Mynewpass4!';")
except:
    print("-> OCORREU UM ERRO AO INSTALAR O MYSQL")



