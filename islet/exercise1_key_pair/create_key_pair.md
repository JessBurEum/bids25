# OpenStack Horizon: Create a Key Pair Exercise

**Objective:** Learn how to create a key pair to securely access OpenStack instances via SSH.  
**Estimated time:** 5 minutes

---

## Step 1: Log in to Horizon
1. Open your web browser and log in to the OpenStack Horizon dashboard.  
2. Refer to `islet_exercise0` if you need guidance on logging in.

---

## Step 2: Navigate to Key Pairs
1. In the left-hand menu, go to **Compute → Key Pairs**.  
2. Click the **Create Key Pair** button.

---

## Step 3: Create the Key Pair
1. **Name:** Enter a descriptive name for your key pair, e.g., `[first_name_last_initial]-bids-key`.  
   - Example: `jessb-bids-key`  
2. **Key Type:** Select **SSH Key**.  
3. Click **Create Key Pair**.

---

## Step 4: Download and Save Private Key
1. Your private key (`.pem` file) will automatically download.  
2. **Important:** Save it securely; this is the only time you can download it.  
3. Move the file to your SSH directory or a temporary folder for the exercise:  

   - **Windows:** `C:\Users\<YourName>\.ssh\`  
   - **Linux/Mac:** `~/.ssh/`  

4. (Optional) Set proper file permissions on Linux/Mac:  
   ```bash
   chmod 600 ~/.ssh/<your-key>.pem
   ```

---

## Step 5: Verify Key Pair in Horizon
1. Go back to **Compute → Key Pairs**.  
2. Ensure your new key pair is listed.  
3. You can now assign this key to any instance when launching VMs.

---

## Step 6: See exercise 2 – vm creation
1. Launch a VM and assign your new key pair to it.  
2. Once the instance is active and has a floating IP, connect via SSH:  
   ```bash
   ssh -i ~/.ssh/<your-key>.pem eouser@<floating_ip>
   ```
3. You should now have secure SSH access to your instance.

---

**Tips / Notes:**  
- Keep your private key secret. Sharing it compromises security.  
- If using Windows, you may need an SSH client like **PuTTY** (convert `.pem` to `.ppk`) to connect.  
- If SSH access fails, check your security group rules to ensure port 22 is open.

