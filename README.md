Knackered-Binaries
==============
Knackered binaries is a collection of "malicious" code, ranging from bash backdoors, to python IRC botnets.

## bash_backdoor
This script runs, flushes iptables rules, sets default policies to accept, and overwrites the traceroute binary with the netcat binary.

It then finally looks to see if the "traceroute" process is running, if it is not, then it starts it as a listener on port 33434.

## passwd_backdoor
See the README in the folder.

## php_webshell
Simple PHP Webshell that just has a textbox, you can type any linux command in, and it will run it as root, and return the output to the screen.

## python_backdoor
Backdoor with very similar basic functionality of netcat. It runs on port 1080, and allows a remote user to connect, they are presented with a prompt
it allows them to run Linux/Windows commands, depending on what operating system it is being run on, then the output of the command is sent back to the user.

## python_irc_botnet
python script that runs and connects to a pre-defined IRC channel, and just listens for a certain syntax of a command, then runs it, and returns the output back to the pre-defined owner.
