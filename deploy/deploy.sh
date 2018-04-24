#Create instances and attach volumns. The Host file will be available in "host"
#The number of instances, size of volumns and other configurations are in "config.json"
#python create_instance.py

#Wait for booting of instances
#sleep 60

#ping check all instances (also add the keys)
#ANSIBLE_HOST_KEY_CHECKING=False ansible all -i hosts -m ping

#For all instances, mount volumn and install basic packages
#ansible-playbook -i hosts playbook/basic.yml

#For db instances, install couchdb cluster
#ansible-playbook -i hosts playbook/couchdb.yml

#For db instances, install and run harvester
ansible-playbook -i hosts playbook/harvester.yml