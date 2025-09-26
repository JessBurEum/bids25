# Exercise: Download OpenStack RC File and Transfer to a VM

## Objective
Download an OpenStack RC file (application credentials) from the Horizon dashboard and securely transfer it to a remote VM for later use with the OpenStack CLI.

## Project Documentation

- [How to activate OpenStack cli access to the cloud](https://destine-data-lake-docs.data.destination-earth.eu/en/latest/openstackcli/How-to-activate-OpenStack-CLI-access-to-the-cloud.html)


### RC File (Application Credentials)

In OpenStack, an RC file (Application Credentials) is a small shell script that contains environment variables used to authenticate with the OpenStack APIs and CLI.

When you source the file in your shell, it sets variables such as:

OS_AUTH_URL – the identity service (Keystone) endpoint

OS_PROJECT_ID / OS_PROJECT_NAME – the project (tenant) you’re working in

OS_USERNAME / OS_PASSWORD or application credential ID and secret

OS_REGION_NAME – the OpenStack region

This way, the OpenStack client tools (like openstack, nova, glance) know who you are, what project you belong to, and where to send API requests.


```bash
# When we 'source' a file environment variables are set allowing you to interact with the openstack servers.

source BiDS25_1-openrc-app-credentials.sh
# Gives a list of virtual machine instances in the project(tenant)
openstack server list

```


---

## Steps

### Step 1: Download the RC File from Horizon
1. Log in to the OpenStack Horizon web dashboard.
2. Click on your username (top right corner).
3. Select **OpenStack RC File (Application Credentials)**.
4. The file will download to your local **Downloads** folder, for example:
   ```
   BiDS25_1-openrc-app-credentials.sh
   ```

---

### Step 2: Prepare Your SSH Key
1. Ensure you have the private key for your VM available on your local machine.
2. Restrict access to your private key:
   ```bash
   chmod 600 ~/.ssh/my_vm_key.pem
   ```

---

### Step 3: Transfer the File to the Remote VM
Use `scp` to securely copy the file to your VM.

**Linux/Mac Example:**
```bash
scp -i ~/.ssh/my_vm_key.pem ~/Downloads/BiDS25_1-openrc-app-credentials.sh eouser@<floating_ip>:/home/eouser/

```

**Windows Command Prompt or PowerShell Example:**
```powershell
scp -i C:\Users\<YourName>\.ssh\my_vm_key.pem C:\Users\<YourName>\Downloads\BiDS25_1-openrc-app-credentials.sh eouser@<floating_ip>:/home/eouser/
```

**Example with actual IP:**
```powershell
scp -i C:\Users\jburford\.ssh\jess-bids-key-private-leonardo BiDS25_1-openrc-app-credentials.sh eouser@217.71.197.133:/home/eouser/

```

---

### Step 4: Log in to the VM
1. Connect to your VM using SSH:
   ```bash
   ssh -i ~/.ssh/my_vm_key.pem eouser@<floating_ip>
   ```

2. Verify the file was transferred:
   ```bash
   ls -l ~/BiDS25_1-openrc-app-credentials.sh
   ```

3. Move the file into the exercise5 folder:

- The file BiDS25_1-openrc-app-credentials.sh will be used to connect to openstack

   ```bash
   mv ~/BiDS25_1-openrc-app-credentials.sh ~/projects/bids25/exercise5_python_hda/
   ```

---

### Step 5: Set Permissions (Recommended)
Restrict access to the RC file so only your user can read it:
```bash
chmod 600 ~/projects/bids25/islet/exercise5_python.hda/BiDS25_1-openrc-app-credentials.sh
```

---

## Notes
- Keep the RC file secure as it contains your OpenStack application credentials.
- Always use SSH keys with proper permissions when transferring sensitive files.
- You will later **source** this RC file in your VM to authenticate the OpenStack CLI.

