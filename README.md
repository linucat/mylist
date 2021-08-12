# Setup Raspberry Pi

##  SSH to server

```python
# Create:
ssh-keygen -b 4096

# Copy:
ssh-copy-id your_username@192.0.2.0

# Connect:
ssh your_username@192.0.2.0

>>> Enter passphrase for key '/root/.ssh/id_rsa':   "DO NOT SAVE PASS PHRASE" 

```

## SSH to raspi

- Create ssh file in boot folder: ``touch ssh``
- Connect to same network
- SSH to pi ``ssh pi@raspberrypi.local``
- Username: pi, Password: raspberry

## Change root password

```bash
sudo passwd root
sudo passwd username ### for username 

```

## Change wifi

```bash
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

network={
ssid="wifssidnumberone"
Priority=35
psk="secretpassword"
}
network={
ssid="numbertwoSSID"
priority=70
psk="pswdsecret"
}

```


## Auto send IP on reboot

```bash
 sudo nano /etc/rc.local

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
  sudo /usr/bin/python3 /home/pi/Mygit/tools/send_ip.py
fi

exit 0

```

## Github

```python
git config --global user.name MY_USER_NAME

git config --global user.email MY_USER_EMAIL


git config --global credential.helper store

>> save to home/.gitconfig
>> save to home/.git-credentials
```

## Python venv

```python
apt-get install python3-venv
```

## Working Dir

```bash
cd ~

mkdir Mygit

cd Mygit/

git clone ...
```

## Create venv folder

```bash
cd /home/pi/Mygit/

python3 -m venv venv

source ./venv/bin/activate

pip install -r /home/pi/Mygit/tools/requirements.txt

```

## chmod +x

```bash
chmod +x _dailyslotbonus.sh
chmod +x _coinmasterspin.sh
chmod +x _send_temp.sh

```

## Crontab

```bash
crontab -e