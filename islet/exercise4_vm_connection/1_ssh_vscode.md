# Connect to a VM using VS Code Remote Explorer (SSH)

**Objective:** Use Visual Studio Code’s Remote Explorer extension to connect to a VM over SSH.  
**Estimated time:** ~10 minutes

---

## Step 1: Install Requirements
1. Install [Visual Studio Code](https://code.visualstudio.com/).
2. In VS Code, open the **Extensions Marketplace** and install:
   - **Remote - SSH**
   - **Remote Explorer**
3. Ensure you have:
   - An SSH private key (`.pem`).
   - Your VM’s floating IP address.
   - The correct default username (i.e. `eouser`).

---

## Step 2: Locate the SSH Config File
- On **Windows**: `C:\Users\<YourName>\.ssh\config`  
- On **Linux/Mac**: `~/.ssh/config`  

If the file does not exist, create it.

---

## Step 3: Edit the SSH Config File
1. Open the `config` file in an editor (you can use VS Code itself).
2. Add a configuration entry like this:

   ```ssh
   Host my-vm
       HostName <floating_ip>
       User eouser
       IdentityFile C:/Users/<YourName>/.ssh/MyKey.pem
   ```

## Step 4: Open Remote Explorer

1. In VS Code, click the Remote Explorer icon in the left Activity Bar.
2. From the dropdown, select SSH Targets.
3. You should see the new host entry (e.g., my-vm).
4. Right-click on the host and choose Connect to Host in New Window.

## Step 5: First Connection

1. The new VS Code window will attempt to connect.
2. If prompted with a host key verification dialog, click Continue.
3. VS Code will install the VS Code server on your VM automatically.


## Step 6: Verify Connection

1. Once connected, open a terminal in VS Code
2. Confirm the prompt shows your VM user, for example:

eouser@my-vm:~$

You can now browse, edit files, and run commands directly inside VS Code.

