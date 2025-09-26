# OpenStack Horizon: Connect to a VM Using SSH (Windows)

**Objective:** Connect to an existing VM with a floating IP using SSH from a Windows PC.  
**Estimated time:** 5 minutes

---

## Prerequisites
- The VM is already created and has a **floating IP** assigned.
- You have the **private key file** (`.pem`) downloaded when creating the key pair.
- Install an SSH client:
  - **Windows 10/11:** Built-in `ssh` command (via PowerShell or Command Prompt).
  - Or use [PuTTY](https://www.putty.org/) if preferred.

---

## Step 1: Locate Your Private Key
1. Find your `.pem` file (e.g., `jessb-bids-key.pem`).
2. Save it in a known folder, e.g., `C:\Users\<YourName>\.ssh\`.

---

## Step 2: Open Command Prompt
1. Press **Win + R**, type `cmd`, and press **Enter**.
2. Change to the folder where your key is stored:
   ```cmd
   cd C:\Users\<YourName>\.ssh


## Step 2: Open PowerShell (Alternative to Command Prompt)
1. Press **Win + R**, type `powershell`, and press **Enter**.
2. Navigate to the folder where your key is saved:
   ```powershell
   cd C:\Users\<YourName>\.ssh\


## Step 5: Connect via SSH
1. From your local terminal, connect to the VM using SSH:
   
   ssh -i MyKey.pem eouser@<floating_ip>

2. Replace MyKey.pem with your key file name.

3. Replace <floating_ip> with your VM’s floating IP address.

Note: The user by default is 'eouser'


## Step 6: Known hosts Check

1. You will likely see a message 'The authenticity of host... can't be established. Are you sure you want to continue connecting?
2. Type `yes` then enter
3. You should now be connected to the vm



## Step 6: Verify Connection

1. You should see something similar to below

   eouser@leonardo-jess-vm1:~$

```bash

C:\Users\jburford\.ssh>ssh -i jess-bids-key-private-leonardo eouser@217.71.197.133
The authenticity of host '217.71.197.133 (217.71.197.133)' can't be established.
ED25519 key fingerprint is SHA256:IeEVQeTeDQcJ9datvpl//pit2Cf7mZxewUQtU5WUrxU.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '217.71.197.133' (ED25519) to the list of known hosts.
Connection closed by 217.71.197.133 port 22

C:\Users\jburford\.ssh>ssh -i jess-bids-key-private-leonardo eouser@217.71.197.133
Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 5.15.0-135-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

eouser@leonardo-jess-vm1:~$

```
   
2. type `pwd` to check where you are in the filesystem.

   eouser@leonardo-jess-vm1:~$ pwd
   /home/eouser
   eouser@leonardo-jess-vm1:~$


