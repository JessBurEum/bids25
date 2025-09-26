# OpenStack Horizon: Quick VM Creation Exercise

**Objective:** Learn how to create a virtual machine (VM) using the OpenStack Horizon web interface.  
**Estimated time:** 10 minutes

---

## Step 1: Log in to Horizon
1. See islet_exercise0

---

## Step 2: Navigate to Instances
1. In the left-hand menu, click **Compute → Instances**.
2. Click the **Launch Instance** button.

---

## Step 3: Configure Instance Details
1. **Instance Name:** Enter a name for your VM, e.g. `leonardo-[YOUR_NAME]-vm1` example `leonardo-jess-vm1`
2. **Description:** (Optional) Leave empty
3. **Availability Zone:** (Optional) Leave `nova` default
4. **Count:** (Optional) Leave Count `1` default
5. Click **Next** to proceed to the **Source** tab.

---

## Step 4: Choose an Image
0. Leave Default Values
1. Select the image **DEDL-Ubuntu 22.04 LTS** (up arrow to right)
2. Observe that the image is in the Allocated section
3. Click **Next**.

---

## Step 5: Choose Flavor
1. Select the **flavor** `eo2a.xlarge` for your VM (CPU, RAM, disk size) using 'up arrow to right'
   - `eo2a.large` → 4 vCPU, 14.9 GB RAM, 64 GB Total disk.
2. Click **Next**.

---

## Step 6: Configure Networking
1. Select a **network** for your instance (use `EUMETSAT_1`)
2. Click **Next**.

---

# Step 7: Network Ports
Click 'Next'

---

## Step 8: Security Groups
1. Choose a **security group** to apply (use, `allow_ping_ssh_rdp`).
4. Click **Next**.

---

## Step 9: Key Pair
1. Select an existing **key pair** (The keypair you created in previous exercise) 
2. At this point we have enough information to launch your instance
3. Click **Launch Instance**.

---

## Step 9: Verify Your Instance
1. You will be redirected to the **Instances** page.
2. Wait until the instance status shows **Active**.
3. Confirm the Power state is `Running`.



