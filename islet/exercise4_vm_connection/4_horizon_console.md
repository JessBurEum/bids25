# Exercise: Connecting to Horizon Console and Switching Users

**Duration:** ~3 minutes  
**Objective:** Learn how to connect to a VM through the OpenStack Horizon console and switch to the real user.

## Project Documentation

[How to access the vm from openstack console](https://destine-data-lake-docs.data.destination-earth.eu/en/latest/dedl-big-data-processing-services/Islet-service/cloud/How-to-access-the-VM-from-OpenStack-console/How-to-access-the-VM-from-OpenStack-console.html)

---

## Steps

1. **Open the Horizon Console**
   - In Horizon, navigate to **Project > Compute > Instances**.
   - Select your VM and click the tab **Console** to open the Horizon web console.

2. **Login with the Initial User**
   - At the login prompt, enter:
     ```
     login: eoconsole
     password: console123
     ```
   - *(Note: Use the simple password `totototo` only for this exercise.)*

3. **Switch to the Real User**
   - Once logged in, switch to the intended user:
     ```bash
     sudo su - eouser
     ```
   - Enter the password for `eouser` when prompted.

---

## Notes

- The VMs are configured with **default keyboard layouts**. Depending on your own keyboard (e.g., AZERTY vs QWERTY), some characters (like `-`, `_`, `@`) may appear in unexpected positions.
- Even with a password you cannot login with just a password using ssh (passwordauthentication is set to no)
   - ssh eouser@<floating_ip> (will fail therefore)

---
