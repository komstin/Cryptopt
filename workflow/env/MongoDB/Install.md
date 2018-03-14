Install MongoDB Community Edition on Ubuntu (3.6.3)  
https://docs.mongodb.com/master/tutorial/install-mongodb-on-ubuntu/ 

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5 
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list 
sudo apt-get update 
sudo apt-get install -y mongodb-org 

Start: sudo service mongod start 
Stop:  sudo service mongod stop 
Restart: sudo service mongod restart 
Shell: mongo --host 127.0.0.1:27017 

tuning: 
https://docs.mongodb.com/master/reference/ulimit/ 
