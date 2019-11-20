# Install

```
$ sudo apt install python3-fuse sshfs
$ # Example: connect to mainframe using sshfs and expose home directory with EBCDIC handling
$ mkdir -p sshfs-z sshfs-z-ebcdic
$ sshfs user@mainframe.corp.com: sshfs-z
$ python3 ebcdicfs.py ~/sshfs-z ~/sshfs-z-ebcdic
$ vim ~/.bashrc
```
