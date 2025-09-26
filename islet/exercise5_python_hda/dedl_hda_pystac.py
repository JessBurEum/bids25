#!/usr/bin/env python3

# ==========================
# Imports
# ==========================
import os
import requests
from tqdm import tqdm

import destinelab as deauth
from pystac_client import Client
from dotenv import load_dotenv
import geopandas as gpd
from rich.console import Console
from rich.table import Table

# ==========================
# Load environment variables
# ==========================
load_dotenv()
DESP_USERNAME = os.getenv("DESP_USERNAME")
DESP_PASSWORD = os.getenv("DESP_PASSWORD")

# ==========================
# Authenticate with DEDL/DESP
# ==========================
auth = deauth.AuthHandler(DESP_USERNAME, DESP_PASSWORD)
access_token = auth.get_token()
console = Console()

if access_token:
    console.print("[green]DEDL/DESP Access Token Obtained Successfully[/green]")
else:
    console.print("[red]Failed to Obtain DEDL/DESP Access Token[/red]")
    raise SystemExit(1)

auth_headers = {"Authorization": f"Bearer {access_token}"}

# ==========================
# Connect to HDA STAC API
# ==========================
HDA_API_URL = "https://hda.data.destination-earth.eu/stac/v2"
# HDA_API_URL = "https://hda.central.data.destination-earth.eu/stac/v2"
hda_client = Client.open(HDA_API_URL, headers=auth_headers)

# ==========================
# Display HDA collections
# ==========================
hda_collections = hda_client.get_collections()

# Table 1: Collection IDs and Titles
table = Table(title="HDA Collections", expand=True)
table.add_column("ID", style="cyan", justify="right", no_wrap=True)
table.add_column("Title", style="violet", no_wrap=True)
for collection in hda_collections:
    table.add_row(collection.id, collection.title)
console.print(table)


# Table 2: Collection Titles and Providers

hda_collections = hda_client.get_collections()

table = Table(title="HDA collections | Providers", expand=True)
table.add_column("Title", style="cyan", justify="right", no_wrap=True)
table.add_column("Provider", style="violet", no_wrap=True)

for collection in hda_collections:
    collection_details = hda_client.get_collection(collection.id)
    provider = ",".join(str(x.name) for x in collection_details.providers)
    table.add_row(collection_details.title, provider)
console.print(table)


# ==========================
# Search for items in a collection
# ==========================
coll_name = "EO.ESA.DAT.SENTINEL-1.L1_GRD"
search = hda_client.search(
    max_items=10,
    collections=[coll_name],
    bbox=[-72.5, 40.5, -72, 41],
    datetime="2023-09-09T00:00:00Z/2023-09-20T23:59:59Z",
)
coll_items = search.item_collection()
console.print(
    f"For collection [bold]{coll_name}[/bold] we found {len(coll_items)} items"
)

# ==========================
# Convert items to GeoDataFrame
# ==========================
df = gpd.GeoDataFrame.from_features(coll_items.to_dict(), crs="epsg:4326")
print(df.head())

# ==========================
# Inspect STAC assets of an item
# ==========================
selected_item = coll_items[3]

table = Table(title="Assets in STAC Item")
table.add_column("Asset Key", style="cyan", no_wrap=True)
table.add_column("Description")
for key, asset in selected_item.assets.items():
    table.add_row(key, asset.title)
console.print(table)

# ==========================
# Download and save quicklook image
# ==========================
quicklook_url = selected_item.assets["quick-look.png"].href
with requests.get(quicklook_url, headers=auth_headers, stream=True) as response:
    response.raise_for_status()
    with open("quicklook.png", "wb") as f:
        for chunk in response.iter_content(chunk_size=1024 * 1024):  # 1 MB chunks
            if chunk:
                f.write(chunk)
console.print("[green]Quicklook image saved as quicklook.png[/green]")

# ==========================
# Get download link of asset
# ==========================
down_uri = selected_item.assets["downloadLink"].href
console.print(f"Download link of asset: [blue]{down_uri}[/blue]")

# ==========================
# Download large asset with progress bar
# ==========================
# filename = f"{selected_item.id}.{selected_item.assets['downloadLink'].media_type.split('/')[1]}"
# url = selected_item.assets["downloadLink"].href

# with requests.get(url, headers=auth_headers, stream=True) as response:
#     response.raise_for_status()
#     total_size = int(response.headers.get("Content-Length", 0))
#     chunk_size = 10 * 1024 * 1024  # 10 MB chunks

#     with open(filename, "wb") as f, tqdm(
#         total=total_size, unit="B", unit_scale=True, unit_divisor=1024, desc=filename
#     ) as pbar:
#         for chunk in response.iter_content(chunk_size=chunk_size):
#             if chunk:
#                 f.write(chunk)
#                 pbar.update(len(chunk))

# console.print(f"[green]Asset downloaded successfully as {filename}[/green]")
