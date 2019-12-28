#!/bin/bash

is_root_user() {
  # Function to check that the effective user id of the user running
  # the script is indeed that of the root user (0)

	if [[ $EUID != 0 ]]; then
		return 1
  	fi
	return 0
}

if ! is_root_user; then
	echo "ERROR: You must be the root user. Exiting..." 2>&1
	echo  2>&1
	exit 1
fi

cat << __EOFL__ > /etc/systemd/system/i2c.service
[Unit]
Description=Read values of CO2 

[Service]
ExecStart= /bin/bash -c /home/pi/Desktop/i2c-launch.sh

[Install]
WantedBy=multi-user.target
After=network-online.target
__EOFL__

systemctl daemon-reload
systemctl start i2c.service

echo '*/1 * * * * /bin/bash /home/pi/Desktop/aqn-ceri/dht/launch-dht.sh && python /home/pi/Desktop/aqn-ceri/recup.py' >> /var/spool/cron/crontabs/pi
