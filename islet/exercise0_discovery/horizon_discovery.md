# OpenStack Horizon: Logging Into OpenStack Horizon - Discover Interface

**Objective:** Learn how to connect to a databridge using your Destination Earth 'Desp Credentials'
**Estimated time:** 10 minutes

## Step 1: Log in to Horizon
1. Open your web browser.
2. Navigate to your OpenStack Horizon URL https://cloud.leonardo.data.destination-earth.eu/
3. Assure Authenticate using DEDL OpenID is selected
4. Assure Region DEDL-LEONARDO is selected
5. Click sign in
6. On the page 'Sign in to your account', assure identity provider 'DESP OpenID' is selected
7. Click the button 'Authenticate'
8. On the Desp Sign In page, Enter your DESP **username** and **password**.
9. You should now be authenticated into the Islet (OpenStack) Overview page
10. Assure you are connected to the BiDS25 Domain, BiDS25_1 project(tenant)

## Step 2: Discover the different sections

In particular
- Compute --> Instances
- Compute --> Images
- Compute --> Key Pairs
- Container Infra --> Clusters
- Network --> Network Topology
- Network --> Security Groups
- DNS --> Zones
- Object Store --> Containers
- API Access --> Find Object Store URL and confirm that it is this https://s3.leonardo.data.destination-earth.eu:443/swift/v1