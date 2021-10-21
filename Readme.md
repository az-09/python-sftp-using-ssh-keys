### Steps
```
$ lsb_release -a

Ubuntu 20.04 on WSL 

$ python3 -m venv venv

$ source venv/bin/activate

(venv) $ pip install python-dotenv

(venv) $ pip install wheel
  error: invalid command 'bdist_wheel'
  ----------------------------------------
  ERROR: Failed building wheel for pysftp

(venv) $ pip install pysftp

(venv) $ ssh-keygen -t rsa -b 4096 -C "demo for taeheechoi.com"
        Generating public/private rsa key pair.
        Enter file in which to save the key (/home/ubuntu/.ssh/id_rsa): # Enter
        Enter passphrase (empty for no passphrase): # Enter
        Enter same passphrase again: # Enter
        Your identification has been saved in /home/ubuntu/.ssh/id_rsa
        Your public key has been saved in /home/ubuntu/.ssh/id_rsa.pub
        The key fingerprint is:
        SHA256:1xO35pPIcmQtvxTCUmy3rwX6FnladZpbDUk3F5UG254 demo for taeheechoi.com
        The key's randomart image is:
        +---[RSA 4096]----+
        |             ...=|
        |           .  ++o|
        |            =o++o|
        |           = =+o+|
        |        S o O BE+|
        |         . = X===|
        |          . = *Bo|
        |           o o+= |
        |             .+  |
        +----[SHA256]-----+

(venv) $ ls ~/.ssh/id_*
/home/ubuntu/.ssh/id_rsa  /home/ubuntu/.ssh/id_rsa.pub

(venv) $ cp ~/.ssh/id_rsa .

(venv) $ sudo service ssh restart

(venv) $ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

(venv) $ sudo vi /etc/ssh/sshd_config
    Click Insert key
    Uncomment AuthorizedKeysFile
      AuthorizedKeysFile      .ssh/authorized_keys .ssh/authorized_keys2
    Click Esc :wq
(venv) $ sudo service ssh restart

(venv) $ mkdir ~/sftp

(venv) $ python demo.py
```