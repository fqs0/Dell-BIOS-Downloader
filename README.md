#Dell BIOS Downloader Script
This script automates the process of downloading the latest BIOS updates for selected Dell models. The script performs the following steps:

1. Downloads the CatalogPC.cab file from Dell's official website.
2. Extracts the CatalogPC.xml file from the CatalogPC.cab archive.
3. Parses the CatalogPC.xml file to find the latest BIOS updates for specific Dell models.
4. Downloads the BIOS update files for the specified models.


The script is configured to check for BIOS updates for the following Dell models:
Precision 3581 (systemID='0A68')
Precision 3571 (systemID='0B04')
Precision 3561 (systemID='0C07')
Latitude 5420 (systemID='0B10')
Latitude 5430 (systemID='0A20')

#Prerequisites
Ensure you have the following installed on your system:
Python 3.x
cabextract utility