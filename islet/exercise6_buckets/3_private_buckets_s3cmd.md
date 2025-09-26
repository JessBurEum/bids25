# Exercise: Configure `s3cmd` on an OpenStack VM

**Objective:** Learn how to configure and use `s3cmd` to access private object storage from an OpenStack VM.  
**Estimated time:** ~10 minutes

---



### Step 1: Navigate to the Exercise6 Folder
Move into the project folder or create it:
```bash
#mkdir /home/eouser/projects/exercise6
cd /home/eouser/projects/exercise6
```

Copy the file quicklook.png from exercise5 here

```bash
cp /home/eouser/projects/exercise5/quicklook.png .
```

---


## Step 1: Check installation of `s3cmd`

On your VM, check the version of `s3cmd`:
```bash
s3cmd --version
```

If not installed on your VM, install `s3cmd`:
```bash
# Should be installed already
# sudo apt update && sudo apt install s3cmd -y
```

## Step 2: Obtain Your Credentials from the previous step 3_ec2_credentials

You will need:

- Access Key
- Secret Key
- S3 endpoint URL https://s3.leonardo.data.destination-earth.eu:443/swift/v1


## Step 3: Configure s3cmd

Run the configuration wizard:
```bash
s3cmd --configure
```

When prompted, provide the following values:

```bash
New settings:
 Access Key: (→ your EC2 Access Key)
 Secret Key: (→ your EC2 Secret Key)
 Default Region: DEDL-LEONARDO
 S3 Endpoint: s3.leonardo.data.destination-earth.eu
 DNS-style bucket+hostname:port template for accessing a bucket: s3.leonardo.data.destination-earth.eu
 Encryption password: (→ leave blank)
 Path to GPG program: /usr/bin/gpg
 Use HTTPS protocol: yes
 HTTP Proxy server name:
 HTTP Proxy server port: 0

 Test access with supplied credentials? [Y/n] y
 Please wait, attempting to list all buckets...
 Success. Your access key and secret key worked fine :-)

 Now verifying that encryption works...
 Not configured. Never mind.

 Save settings? [y/N] y
 
```

- This creates a config file: ~/.s3cfg


## Step 4: Test the Configuration

List available buckets:
```bash
s3cmd ls
```

You should see output like:
```bash
2025-09-24 12:00  s3://my-bucket
```