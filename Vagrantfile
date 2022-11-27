# -*- mode: ruby -*-
# vi: set ft=ruby :
$script = <<-SCRIPT
ls
sudo python ./main.py
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  config.disksize.size = "50GB"
  config.vm.network "forwarded_port", guest: 8088, host: 8088
  config.vm.network "forwarded_port", guest: 5432, host: 5432
  config.vm.network "private_network", ip: "192.168.56.56"
  config.vm.provision :file, source: './id_rsa_slave.pub', destination: "~/.ssh/authorized_keys"
  config.ssh.private_key_path = ['./id_rsa_slave', '~/.vagrant.d/insecure_private_key']
  config.vm.provision :file, source: 'main.py', destination: "main.py"
  config.ssh.insert_key = false
  config.vm.provision "shell", inline: $script

  config.vm.provider "virtualbox" do |v|
    v.memory = 4096
    v.cpus = 2
    v.name = "teste-superset"
  end


end
