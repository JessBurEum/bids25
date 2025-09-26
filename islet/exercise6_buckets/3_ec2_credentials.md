# Exercise: Create EC2 Credentials with OpenStack CLI

## Objective
Use the OpenStack CLI to create **EC2-style credentials** (`access` and `secret`) for your user.

---

## Steps

### Step 1: Navigate to the Exercise5 Folder
Move into the project folder:
```bash
cd /home/eouser/projects/bids25/islet/exercise5_python_hda
```

---

### Step 2: Activate Your Virtual Environment
Activate the previously created Python virtual environment where the OpenStack client was installed:
```bash
source venv/bin/activate
```

If you haven’t installed the OpenStack client yet, install it first:
```bash
# Note this is already install in execise5
#pip install python-openstackclient
```

---

### Step 3: Authenticate with OpenStack
1. Source your OpenStack RC file to set the necessary environment variables:
   ```bash
   source BiDS25_1-openrc-app-credentials.sh
   ```
2. Enter the **Application Credential ID** and **Secret** when prompted.

*(See `2_application_credentials.md` for instructions on creating application credentials if you don’t have them yet.)*

---

### Step 4: Create EC2 Credentials
Run the following command to create new EC2-style credentials:
```bash
openstack ec2 credentials create -c access -c secret
```
This will output the `access` and `secret` values.

**Important:** Copy and store these values securely, as they are used to authenticate EC2 API–compatible tools.

---

### Step 5: Verify Creation
List all your EC2 credentials to confirm they were created:
```bash
openstack ec2 credentials list
```
You should see your newly created credentials in the list.

---

## Notes
- EC2 credentials are mainly used for compatibility with tools that expect AWS-style authentication.
- We will use them in a following step with the tool s3cmd which will allow us to work with a private bucket (requiring these EC2 credentials)
- Keep the `access` and `secret` keys secure. Treat them like passwords.
- If compromised, revoke them immediately using:
  ```bash
  openstack ec2 credentials delete <credential_id>
  ```