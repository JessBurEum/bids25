# Exercise: Install Python Virtual Environment Dependencies

## Objective
Use a bash script to create a Python virtual environment and install the following Python packages:
`python-openstackclient`, `pystac-client`, `pystac`, `destinelab`, `python-dotenv`, `geopandas`, `tqdm`.

This also triggers execution of the Python script `dedl_hda_pystac.py`.

**Estimated time:** 7 minutes

---

## Steps

### Step 1: Connect to Your VM
1. Open your preferred method to connect to your VM:
   - VSCode Remote SSH
   - Command Prompt / Terminal with SSH
   - PuTTY
2. Refer to `exercise4` if you need guidance on connecting.

---

### Step 2: cd to excercise5 foleder following git clone

Following previous git clone command you should find exercise5 in the following path.

1. Navigate to the folder:
   ```bash
   cd /home/eouser/projects/bids25/islet/exercise5_python_hda/
   ```

---

### Step 3: Transfer or Create Required Files
In the `exercise5` folder, ensure the following three files exist at the root level:

1. **.env** – Contains your DESP credentials.
2. **setup_python.sh** – Bash script to:
   - Create a Python virtual environment
   - Install the required dependencies
   - Launch `dedl_hda_pystac.py`
3. **dedl_hda_pystac.py** – Python script that:
   - Connects to Destination Earth Data Lake (HDA)
   - Discovers collections
   - Searches a collection
   - Downloads an asset of an Item

**Tip:** You can use VSCode, `nano`, or any text editor to create or transfer these files.

---

### Step 3a: Set Your DESP Credentials
1. Open the `.env` file:
   ```bash
   nano .env
   ```
   or use VSCode to edit.
2. Update it with your DESP credentials as instructed.
3. Save and close the file.

---

### Step 4: Make setup_python.sh Executable
1. Change the script permissions:
   ```bash
   chmod +x setup_python.sh
   ```

---

### Step 5: Run the Script
1. Execute the script:
   ```bash
   ./setup_python.sh
   ```
2. The script will:
   - Create a virtual environment named `venv` (or as defined in the script)
   - Install the required dependencies
   - Execute `dedl_hda_pystac.py`

3. After successful execution, you should see a file called `quicklook.png` downloaded from HDA.

---

### Optional Verification
- Activate the virtual environment manually to check installed packages:
   ```bash
   source venv/bin/activate
   pip list
   ```
- Deactivate after verification:
   ```bash
   deactivate
   ```

