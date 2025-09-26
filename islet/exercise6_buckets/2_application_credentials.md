# Exercise: Create an OpenStack Application Credential

## Objective
Learn how to create an **application credential** in OpenStack Horizon for use with the CLI or automated scripts. The credential will follow a standard naming convention and include all available roles.

## Project Documentation

- [How to generate or use application credentials via cli](https://destine-data-lake-docs.data.destination-earth.eu/en/latest/dedl-big-data-processing-services/Islet-service/cloud/How-to-generate-or-use-Application-Credentials-via-CLI/How-to-generate-or-use-Application-Credentials-via-CLI.html)


---

## What Are Application Credentials?
Application credentials are a secure way to authenticate with OpenStack without exposing your main user password. They generate an ID and secret pair that can be used by the CLI, SDKs, or scripts. 

- Use them for automation or when sharing access with services.  
- They can be revoked at any time without changing your main account.  
- Keep the file secure, as anyone with the credential can act on your behalf within the specified project.

---

## Steps

### Step 1: Log in to Horizon
1. Open the OpenStack Horizon web dashboard.
2. Log in with your account credentials.

---

### Step 2: Navigate to Application Credentials
1. Go to section Identity > Application Credentials

---

### Step 3: Create a New Application Credential
1. Click **Create Application Credential**.
2. Fill out the form:
   - **Name:** Use the naming convention `<first_name><family_name_initial>-bids-app-cred`  
     - Example: `jessb-bids-app-cred`
   - **Roles:** Select **all available roles** (Select first role, hold shift down, Select last role)
   - Leave other fields as default unless specific restrictions are required.
3. Click **Create Application Credential**.

---

### Step 4: Download the Credential File
1. A popup will appear showing the ID, Name and Secret (Note these, we will use them later)
2. (Optional) You can also download the associated openrc file by clicking `Download openrc file` 
2. Save this file in a secure location.
3. You will not be able to download it again—keep it safe.

---

## Notes
- Use application credentials instead of your main password for scripts or long-running jobs.
- If compromised, delete the credential in Horizon immediately.
- Keep credential files private—do not commit them to version control systems.