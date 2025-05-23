#!/bin/bash

groupeadd ftpgroup
useradd -g ftpgroup -d /dev/null -s /etc/ftpuser
pure-pw useradd offsec -u ftpuser -d /ftphome
pure-pw mkdb

cd /etc/pure-ftpd/auth/
ln -s ../conf/PureDB 60pdb
mkdir -p /ftphome
chown -R ftpuser:ftpgroup /ftphome/
systemctl restart pure-ftpd