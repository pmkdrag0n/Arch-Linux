sudo brctl addbr br0
sudo brctl addif br0 enp3s0 #my interface is enp3s0 change it
sudo ip tuntap add dev tap0 mode tap 
sudo brctl addif br0 tap0
sudo ip link set up dev tap0
sudo dhclient -v br0

