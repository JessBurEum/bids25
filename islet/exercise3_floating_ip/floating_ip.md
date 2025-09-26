# OpenStack Horizon: Assign a Floating IP Exercise

**Objective:** Learn how to assign a floating IP to a virtual machine (VM) for external access.  
**Estimated time:** 3 minutes

---

## Step 1: Log in to Horizon
1. See islet_exercise0

---

## Step 2: Navigate to Instances
1. In the left-hand menu, click **Compute → Instances**.
2. Find the VM you want to assign a floating IP to (Your vm created in islet_exercise2)

---

## Step 3: Assign Floating IP
1. In the **Actions** column for your VM, click the drop-down menu.
2. Select **Associate Floating IP**.
3. If no floating IPs are available:
   - Click **+ Allocate IP to Project**.
   - Leave Default Values (Pool = `external`).
   - Click **Allocate IP**.

---

## Step 4: Confirm Association
1. Select the newly allocated floating IP from the list.
2. Click **Associate**.
3. The floating IP will now appear in the **IP Address** column of your instance.

---

