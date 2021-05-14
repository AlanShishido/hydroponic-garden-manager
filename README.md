# Hydroponic System Project

### Demo

[Live Demo](https://django-vue-template-demo.herokuapp.com/)

![System image](/assets-readme/hydroponics-techniques-and-systems.jpg "Hydroponic System")

### Backlog

| TODO                 |  Content                                   |
|----------------------|--------------------------------------------|
| `/Buy Font 12V/3000mA`   |                         |
| `/Buy Jack P4 pin`       |                         |
| `/Buy Jack P4 pin`       |                         |
|                          |                         |


## Instalation Step

`Developed Python 3.8.5 version`

### Raspberry Setup after installing Raspbian OS
    
```
sudo apt update
sudo apt-get update
sudo apt upgrade
```
### Postgres

```
sudo apt install postgresql libpq-dev postgresql-client postgresql-client-common -y
```

### Update to Python 3.8.7
Prerequisites
```
sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev tar wget vim
```
Download Python
```
wget https://www.python.org/ftp/python/3.8.7/Python-3.8.7.tgz
```
Install Python 3.8.7
```
sudo tar zxf Python-3.8.7.tgz
cd Python-3.8.7
sudo ./configure --enable-optimizations
sudo make -j 4
sudo make altinstall
python3.8 -V
```
Make Python 3.8 as the default version
```
echo "alias python=/usr/local/bin/python3.8" >> ~/.bashrc
source ~/.bashrc
python -V
```
Clean up
```
sudo rm -rf Python-3.8.7.tgz
sudo rm -rf Python-3.8.7
```



### Pip command
```
pip3 install -r requirements.txt
```

### Docker install

1. Install Docker
```
curl -sSL https://get.docker.com | sh
```
2. Add permission to Pi User to run Docker Commands
```
sudo usermod -aG docker pi
```
`Reboot here or run the next commands with a sudo`

3. Test Docker installation
```
docker run hello-world
```
4. IMPORTANT! Install proper dependencies
```
sudo apt-get install -y libffi-dev libssl-dev
sudo apt-get install -y python3 python3-pip
sudo apt-get remove python-configparser
```
5. Install Docker Compose
```
sudo pip3 -v install docker-compose 
```