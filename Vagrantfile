# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
	config.vm.box = "ubuntu/xenial64"
	config.vm.network "forwarded_port", guest: 80, host: 8080
	config.vm.provision "shell", inline: <<-SHELL
		apt-get update && apt-get install -y bats	
		useradd -M candidate
		ln -s /vagrant /home/candidate
		bash -x /home/candidate/init.sh
	SHELL
end

