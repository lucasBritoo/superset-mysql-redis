# superset-mysql-redis## ⚙ Ambiente de desenvolvimento

## 🔨 Funcionalidades do projeto

- `Funcionalidade 1`: ✔️ Criar um script Vagrant que suba uma máquina CentOS 7.x com 2 CPUs (2 cores de processador), 4 GB de memória RAM e 50gb de HD chamada “teste-zeppelin”;
- `Funcionalidade 2`: ✔️ O acesso a VM deve ser através de uma chave privada, não com senha;
- `Funcionalidade 3`: ✔️ Criar um programa em python que faça a instalação do Python3 e do Apache Superset na máquina;
- `Funcionalidade 4`: ✔️ Adicionar ao script Python a instalação do PostgreSQL;
- `Funcionalidade 5`: :heavy_multiplication_x: Integrar o PostgreSQL com o Superset <b>(Em desenvolvimento)</b>.
- `Funcionalidade 5`: 	:heavy_multiplication_x: Fazer instalação do Redis e integrar com o Superset <b>(Em desenvolvimento)</b>.

## ⚙ Ambiente de desenvolvimento

A máquina de desenvolvimento está com o sistema operacional Ubuntu Desktop 22.04.1 LTS. Neste ambiente há configurado o Vagrant e VirtualBox.

## 📌 Vagrant

O provider utilizado para desenvolvimento foi o VirtualBox. O box utilizado foi o sistema operacional default do 'centos/7'. Para conseguir manipular o tamanho do disco da VM foi necessário instalar um plugin no Vagrant. Veja o comando abaixo:

```
$ vagrant plugin install vagrant-disksize
```

É importante ressaltar que o IP da VM está configurado como fixo dentro do 'vagrantfile', para os testes de desenvolvimento local foi atribuído o seguinte IP: '192.168.56.56'. Devido a algumas limitações de hardware, a VM foi configurada com 2 'vcpus' e com 4096MB (4GB) de RAM .

## 🔒 SSH

Para a configuração do ssh é necessário gerar novas chaves. O nome da chave gerada é 'id_rsa_slave' e ela precisa estar no mesmo diretório do 'vagrantfile'. Os comandos abaixo vão gerar novas chaves ssh para nossa conexão:

```
$ ssh-keygen -t rsa -b 4096 -C "id_rsa_slave"
$ eval $(ssh-agent) 
$ ssh-add ./id_rsa_slave
```

Para se conectar é necessário copiar o arquivo 'config' para ~/.ssh/. Depois a conexão será estabelecida usando o arquivo config_ssh:

```
$ cp ./config ~/.ssh/
$ ssh teste-zeppelin
```
É essencial que as chaves estejam no mesmo diretório do 'Vagrantfile', pois a chave pública será inserida dentro da VM ao iniciar o processo.

Há um arquivo de configuração chamado 'ssh.config' que contém os parâmetros de conexão ssh (IP, user, port, key). Este arquivo já está configurado com as configurações estáticas para o ambiente de desenvolvimento.


## 🔀 Python

Toda a documentação que foi consultada durante o desenvolvimento está referenciada logo abaixo: 

- `Instalação Python3.6`: <br>
-   [externo] https://www.liquidweb.com/kb/how-to-install-python-3-on-centos-7/


## :floppy_disk: PostgreSQL

Toda a documentação que foi consultada durante o desenvolvimento está referenciada logo abaixo:

- `Instalação PostgreSQL 12`: <br>
-   [oficial] https://www.postgresql.org/download/linux/redhat/
-   [externo] https://gist.github.com/carymrobbins/39b75df64a1201407c80

Há dois arquivos que são copiados para '/var/lib/pgsql/12/data', são eles: 'pg_hba.conf' e 'postgresql.conf'. Estes arquivos contém a liberação para acessar a instância do postgre externo a VM. Assim foi possível testar a conexão utilizando o PGAdmin instalado na máquina host e acessar o PostgreSQL dentro da VM.

## :green_book: Superset

Toda a documentação que foi consultada durante o desenvolvimento está referenciada logo abaixo:

- `Instalação PostgreSQL 12`: <br>
-   [oficial] https://superset.apache.org/docs/installation/installing-superset-from-scratch/#python-virtual-environment
-   [externo] https://github.com/tylerFowler/docker-superset/blob/master/superset-init.sh

O Superset está sendo executado na porta 8088 externo, assim é possível se conectar no navegador pela url 'http://localhost:8088/'. 

