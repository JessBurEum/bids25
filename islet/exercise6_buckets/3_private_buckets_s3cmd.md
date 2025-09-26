# Exercise: Configure `s3cmd` on an OpenStack VM

**Objective:** Learn how to configure and use `s3cmd` to access private object storage from an OpenStack VM.  
**Estimated time:** ~15 minutes

---

## Step 1: Navigate to the Exercise6 Folder

Move into the project folder:

```bash
cd /home/eouser/projects/bids25/islet/exercise6_buckets
```

Copy the file `quicklook.png` from exercise5 here:

```bash
cp /home/eouser/projects/bids25/islet/exercise5_python_hda/quicklook.png .
```

---

## Step 2: Check Installation of `s3cmd`

Check if `s3cmd` is installed and view the version:

```bash
s3cmd --version
```

If not installed, install it:

```bash
sudo apt update && sudo apt install s3cmd -y
```

---

## Step 3: Obtain Your Credentials

You will need the following from the previous step `3_ec2_credentials`:

- **Access Key**
- **Secret Key**
- **S3 Endpoint URL**: `https://s3.leonardo.data.destination-earth.eu`

Keep these handy for configuration.

---

## Step 4: Configure `s3cmd`

Run the configuration wizard:

```bash
s3cmd --configure
```

When prompted, provide the following:

```text
Access Key: (your EC2 Access Key)
Secret Key: (your EC2 Secret Key)
Default Region: DEDL-LEONARDO
S3 Endpoint: s3.leonardo.data.destination-earth.eu
DNS-style bucket+hostname:port template: s3.leonardo.data.destination-earth.eu
Encryption password: (leave blank)
Path to GPG program: /usr/bin/gpg
Use HTTPS protocol: yes
HTTP Proxy server name: (leave blank if none)
HTTP Proxy server port: 0
```

- Test access with supplied credentials `[Y/n] y`. You should see a success message.
- Save the configuration `[y/N] y`.  
  This creates the file: `~/.s3cfg`.

---

## Step 5: Test the Configuration

List available buckets:

```bash
s3cmd ls
```

You should see output similar to:

```text
2025-09-23 18:00  s3://2d8f35f3-6928-4126-8cd6-f298477cf855-etcd-backup
2025-09-24 09:00  s3://be8171a4-2aad-441d-887d-2e9a26fc9602-etcd-backup
2025-09-24 12:52  s3://bids25_resources
2025-09-26 20:13  s3://jessb-bids-bucket1
```

If you get a **name resolution error**, double-check:

- Endpoint spelling
- The endpoint should not include https
  - s3.leonardo.data.destination-earth.eu

---

## Step 6: Upload a File to a Private Bucket

Upload `quicklook.png` to your private bucket:

```bash
s3cmd put quicklook.png s3://jessb-bids-bucket1/
```

Check that the upload succeeded by listing the files:

```bash
s3cmd ls s3://jessb-bids-bucket1/
```

You should see `quicklook.png` in the output.

---

## Step 7: Download a File from a Bucket

To test downloading:

```bash
s3cmd get s3://jessb-bids-bucket1/quicklook.png quicklook_downloaded.png
```

Verify the file exists locally:

```bash
ls -l quicklook_downloaded.png
```

---

## Step 8: Remove a File from the Bucket (Optional)

If you want to clean up:

```bash
s3cmd del s3://jessb-bids-bucket1/quicklook.png
```

---

## Step 9: Summary

- `s3cmd` is installed and configured
- Credentials are stored in `~/.s3cfg`
- You can **list buckets**, **upload**, **download**, and **delete** files


