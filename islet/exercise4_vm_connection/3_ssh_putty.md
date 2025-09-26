# Accessing a VM from Windows using PuTTY (based on DESTINE-Islet docs)

**Objective:** Convert your `.pem` key and connect to your OpenStack VM from Windows using PuTTY.  
**Estimated time:** ~10 minutes

**based on documentation** : https://destine-data-lake-docs.data.destination-earth.eu/en/latest/dedl-big-data-processing-services/Islet-service/access-from-windows/How-to-access-a-VM-from-Windows-PuTTY/How-to-access-a-VM-from-Windows-PuTTY.html

---

## Step 1: Install PuTTY and PuTTYgen
1. Download and install **PuTTY** and **PuTTYgen** (if not already installed).
2. Ensure both `putty.exe` and `puttygen.exe` are available in your Start menu or installation folder.

---

## Step 2: Convert the PEM key to PPK using PuTTYgen
1. Launch **PuTTYgen**.
2. In PuTTYgen:
   - Click **Load**.
   - In the file dialog, switch the file type filter to **All Files (\*)**.
   - Select your `.pem` file (e.g. `MyKey.pem`).
3. You should see “Successfully imported foreign key”.
4. Click **Save private key**.
   - Choose a file name (e.g. `MyKey.ppk`).
   - If warned about saving without a passphrase, accept if okay.

---

## Step 3: Gather connection details
- Note your VM’s **floating IP address**.
- Note the **username** for the VM (i.e. `eouser`)

---

## Step 4: Configure PuTTY session
1. Open **PuTTY**.
2. In the **Session** category:
   - Enter the **Host Name** field as:  
     ```
     eouser@<floating_ip>
     ```  
     (e.g. `eouser@203.0.113.45`)
3. (Optional) In **Saved Sessions**, enter a name (e.g. `MyOpenStackVM`) and click **Save**.

---

## Step 5: Load the private key in PuTTY
1. In the left pane, expand **Connection → SSH → Auth**.
2. Under **Private key file for authentication**, click **Browse…**.
3. Select your `.ppk` file (e.g. `MyKey.ppk`).
4. (Optional) You can also go to **Connection → Data** and set the **Auto-login username** to your VM username `eouser`.

---

## Step 6: Connect
1. Return to **Session** in the left pane.
2. Ensure your session name is selected (or the host is entered).
3. Click **Open**.
4. On first connection, PuTTY may show a **“Server’s host key is not cached in the registry”** warning:
   - Click **Accept** or **Yes** to store the host key.
5. You should now see a shell prompt, e.g.: eouser@your-vm:~$

