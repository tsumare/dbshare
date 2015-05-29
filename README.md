# dbshare.py

## Setup
dbshare.py depends on the dropbox python API.  To install this on Ubuntu 14.04,
run the following commands:

```sh
sudo aptitude install python-pip
sudo -i pip install dropbox
```

You are now ready to run dbshare.py.  It is recommended that you add it to your
PATH.

On first startup it will prompt for a Dropbox API app key and app secret, and
will ask you to link it to your Dropbox account.

```
$ dbshare ~/Dropbox/file.jpg
Enter app key: xxxxxxxxxxxxxxx
Enter app secret: xxxxxxxxxxxxxxx
Please authorize the application at https://www.dropbox.com/1/oauth2/authorize?response_type=code&client_id=xxxxxxxxxxxxxxx
Enter the token you are given: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Updating ~/.dbshare.conf...
https://www.dropbox.com/s/xxxxxxxxxxxxxxx/file.jpg?dl=0
```
