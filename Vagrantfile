Vagrant.configure('2') do |config|
  config.vm.box = 'centos/7'
  
  config.vm.synced_folder '.', '/vagrant', disabled: true

  config.vm.provider :libvirt do |libvirt|
    libvirt.driver = 'kvm'
    libvirt.cpus = 2
    libvirt.memory = '2048'
  end

  config.vm.define 'vault' do |node|
    node.vm.provision 'ansible' do |ansible|
      ansible.compatibility_mode = '2.0'
      ansible.playbook = "provisioning/main.yml"
    end
  end

end
