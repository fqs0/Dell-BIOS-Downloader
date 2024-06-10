# Dell BIOS Downloader Script
This script automates the process of downloading the latest BIOS updates for selected Dell models. The script performs the following steps:

1. Downloads the CatalogPC.cab file from Dell's official website.
2. Extracts the CatalogPC.xml file from the CatalogPC.cab archive.
3. Parses the CatalogPC.xml file to find the latest BIOS updates for specific Dell models.
4. Downloads the BIOS update files for the specified models.


## The script is configured to check for BIOS updates for the following Dell models:
- Precision 3581 (`systemID='0A68'`)
- Precision 3571 (`systemID='0B04'`)
- Precision 3561 (`systemID='0C07'`)
- Latitude 5420 (`systemID='0B10'`)
- Latitude 5430 (`systemID='0A20'`)


## Prerequisites
Ensure you have the following installed on your system:
Python 3.x
cabextract utility


## Example Output
```yaml
FOUND! BIOS Firmware: Dell Precision 3581 System BIOS,1.12.0,1.12.0
URL: https://dl.dell.com/FOLDER11360381M/1/Precision_3581_1.12.0.exe

FOUND! BIOS Firmware: Dell Latitude 5420 System BIOS,1.36.2,1.36.2
URL: https://dl.dell.com/FOLDER11443268M/1/Latitude_5420_1.36.2.exe

FOUND! BIOS Firmware: Dell Precision 3561 and Latitude 5521 System BIOS,1.29.0,1.29.0
URL: https://dl.dell.com/FOLDER11236632M/1/Precision_3561_Latitude_5521_1.29.0.exe

FOUND! BIOS Firmware: Dell Precision 3571 and Latitude 5531 System BIOS,1.22.0,1.22.0
URL: https://dl.dell.com/FOLDER11365596M/1/Precision_3571_Latitude_5531_1.22.0.exe

FOUND! BIOS Firmware: Dell Latitude 5430 System BIOS,1.17.1,1.17.1
URL: https://dl.dell.com/FOLDER10684887M/1/Latitude_5430_1.17.1.exe
```