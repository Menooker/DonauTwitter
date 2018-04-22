sudo apt-get -y install vim
echo -e "cqmygysdss\ncqmygysdss" | sudo passwd ubuntu
sudo mkdir /extra
sudo mkfs.ext4 /dev/vdc

echo -e "sudo mount /dev/vdc /extra -t auto\nsudo chown ubuntu /extra" > mount.sh
chmod 777 mount.sh
./mount.sh

echo "/dev/vdc        /extra  auto    defaults        0       2" | sudo tee --append /etc/fstab > /dev/null