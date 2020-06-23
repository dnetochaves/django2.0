# Introdução ao Framework Django

#### Django é um framework para desenvolvimento rápido para web, escrito em Python, que utiliza o padrão model-template-view (MTV). Foi criado originalmente como sistema para gerenciar um site jornalístico na cidade de Lawrence, no Kansas. Tornou-se um projeto de código aberto e foi publicado sob a licença BSD em 2005. O nome Django foi inspirado no músico de jazz Django 


##### Instalando pytgon
	sudo apt-get install python3

##### Instalando Virtualenv
#### pip é um sistema de gerenciamento de pacotes padrão de facto usado para instalar e gerenciar pacotes de software escritos em Python.

    Instalando virtualenv: sudo apt-get install python-virtualenv / sudo apt-get install python3.7-venv
	
    Criação da virtualenv: virtualenv venv -p python3 

    ativar virtualenv: source venv/bin/activate 

    Instalação do Django: pip install django

    Criando projeto django: django-admin startproject nome_do_projeto .

    Subindo o servidor de produção: python manage.py runserver

    Rodando as migrações: python manage.py makemigrations / python manage.py migrate

    Criando uma App: djangp-admin startapp nomeapp

    Criando super usuário: pytgon manage.py createsuperuser
