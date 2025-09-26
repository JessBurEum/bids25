# Exercise: Set Your Python Virtual Environment in VS Code

## Objective
Configure VS Code to use your `venv` virtual environment as the workspace Python interpreter.

---

## Steps

### Step 1: Open the Project Folder
1. Open VS Code.
2. Go to `File → Open Folder...` and select the folder containing your project and virtual environment.
   - Example: `/home/eouser/projects/bids25`

---

### Step 2: Install Python Extension (if not already installed)
1. Go to the Extensions view (`Ctrl+Shift+X` / `Cmd+Shift+X`).
2. Search for **Python** and install the official Microsoft extension.
3. Reload VS Code if prompted.

---

### Step 3: Open the Command Palette
1. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac).
2. Type `Python: Select Interpreter` and select it.
3. Enter interpreter path...
4. Find...
5. select venv/bin/python

The path should be like this
```bash
/home/eouser/projects/bids25/islet/exercise5_python_hda/venv/bin/python
```

---

### Step 4: Select Your Virtual Environment
1. Look for your virtual environment in the list, e.g., `./venv/bin/python`.
2. If it’s not listed:
   - Choose `Enter interpreter path → Find...`
   - Navigate to your `venv` folder, e.g., `venv/bin/python3.12`, and select it.

---

### Step 5: Verify the Interpreter
1. Open a terminal in VS Code (`Ctrl+``).
2. Check that the virtual environment is active:
   ```bash
   (venv) $ python --version
   (venv) $ which python
   ```
3. Both commands should point to the virtual environment, not the system Python.

---

### Step 6: Optional – Configure Workspace Settings
1. Ensure `.vscode/settings.json` exists in your project folder.
2. Verify it contains:
   ```json
   {
     "python.defaultInterpreterPath": "venv/bin/python"
   }
   ```
3. This ensures that every new terminal and script in this workspace automatically uses the `venv` interpreter.

---

### Step 7: Run a Test
1. In the VS Code terminal, run:
   ```bash
   openstack --help
   ```
2. The command should work and use the packages installed in your virtual environment.

---

**Goal:**  
After completing this exercise, all Python scripts and terminals in this workspace should automatically use `venv`, ensuring your dependencies are isolated from the system Python.