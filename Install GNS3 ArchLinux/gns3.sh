left=" =======================================( "
right=" )========================================="
install_dynamips() {
  printf %b\\n "
$left Installing dynamips $right
"
sleep 2

sudo pacman -S libelf libpcap cmake --noconfirm --needed
yay -S dynamips --noconfirm --needed
}
install_vpcs() {
  # Installing VPCS
  printf %b\\n "
$left Installing VPCS $right
"
  sleep 2
  yay -S vpcs --noconfirm --needed
}

install_iouyap() {
  # Install IOUYAP
  printf %b\\n "
$left Installing IOUYAP $right
"
  sleep 2
  sudo pacman -S iniparser --noconfirm --needed
  yay -S iouyap --noconfirm --needed
}

install_iol_dependencies() {
  # Install IOL Dependencies
  printf %b\\n "
$left Installing IOL Dependencies$right
"
  sleep 2
  sudo pacman -S lib32-openssl lib32-gcc-libs --noconfirm --needed
  sudo ln -s /usr/lib32/libcrypto.so.1.0.0 /usr/lib32/libcrypto.so.4
  sudo sysctl net.unix.max_dgram_qlen=10000
  sudo tee -a /etc/sysctl.d/99-sysctl.conf >/dev/null <<EOL
# Prevent EXCESSCOLL error for IOL
net.unix.max_dgram_qlen=10000
EOL
}

install_ubridge() {
  # Install uBridge
  sleep 2
  printf %b\\n "
$left Installing uBridge$right
"
  yay -S ubridge --noconfirm --needed
  sudo pacman -S ebtables dnsmasq libvirt virt-manager --noconfirm --needed
}

install_qemu() {
  # Install QEMU
  printf %b\\n "
$left Installing QEMU$right
"
  sleep 2
  sudo pacman -S qemu --noconfirm --needed
}

install_docker() {
  # Install docker
  printf %b\\n "
$left Installing Docker$right
"
  sleep 2
  sudo pacman -S docker --noconfirm --needed
  sudo systemctl enable docker.service
  sudo systemctl start docker.service
  sudo gpasswd -a "$USER" docker
}

install_wireshark() {
  # Install Wireshark
  printf %b\\n "
$left Installing Wireshark$right
"
  sleep 2
  sudo pacman -S wireshark-qt --noconfirm --needed
  sudo gpasswd -a "$USER" wireshark
}
install_gns3() {
  printf %b\\n "
$left Installing GNS3 Dependencies $right
"
cd /tmp && git clone https://aur.archlinux.org/python-jsonschema26.git && cd python-jsonschema26 && makepkg -si --nocheck
yay -S python-aiohttp-cors-gns3 python-yarl-gns3 --noconfirm --needed
  printf %b\\n "
$left Installing GNS3 GUI $right
"
yay -S gns3-gui --noconfirm --needed
printf %b\\n "
$left Installing Server $right
"
yay -S gns3-server --noconfirm --needed
}
main() {
  install_dynamips
  install_vpcs
  install_iouyap
  install_iol_dependencies
  install_ubridge
  install_qemu
  install_docker
  install_wireshark
  install_gns3
  printf %b\\n "${IGreen}
Installation has been completed!

Please reboot your PC...${Color_Off}"
}


main