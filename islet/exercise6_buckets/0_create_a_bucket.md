# Exercise: Create an Object Storage Bucket in OpenStack Horizon

## Objective
Create an object storage bucket in the OpenStack Horizon interface following the naming convention:  
`<first_name><last_name_initials>-bids-bucket1`  
Example: `jessb-bids-bucket1`

## Project Documentation

- [How to use object storage](https://destine-data-lake-docs.data.destination-earth.eu/en/latest/s3/How-to-use-Object-Storage.html#how-to-use-object-storage)

---

## Steps

## Step 1: Log in to Horizon
1. Open your web browser and log in to the OpenStack Horizon dashboard.  
2. Refer to `islet_exercise0` if you need guidance on logging in.

## 2. **Navigate to Object Store**
   - In the left-hand menu, click **Project → Object Store → Containers**.

## 3. **Create a New Bucket**
   - Click **+ Create Container**.
   - In the **Container Name** field, enter your bucket name using the convention:  
     `<first_name><last_name_initials>-bids-bucket1`  
     Example: `jessb-bids-bucket1`.

## 4. **Set Access Control**
   - Leave the container access as **Private** (default), unless otherwise instructed.
   - This ensures only authenticated users with the correct credentials can access it.

## 5. **Confirm Creation**
   - Click **Create**.
   - You should now see your bucket listed in the containers view.

---

## Verification
- Check that the bucket appears in the list.
- Ensure the name matches the required convention exactly.

**Goal:**  
You now have a correctly named private object storage bucket in OpenStack Horizon.

