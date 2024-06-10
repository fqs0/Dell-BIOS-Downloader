import xml.etree.ElementTree as ET
import urllib.request
import subprocess
import os

def download_catalog_file(catalog_file_path, output_catalog):
    urllib.request.urlretrieve(catalog_file_path, output_catalog)

download_catalog_file(catalog_file_path="https://downloads.dell.com/catalog/CatalogPC.cab", output_catalog="CatalogPC.cab")

def extract_cab_file_with_cabextract(cab_file_path, output_dir):
    subprocess.run(['cabextract', '-d', output_dir, cab_file_path])

extract_cab_file_with_cabextract(cab_file_path='./CatalogPC.cab', output_dir = './')

def parse_xml(file_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    results = []
    
    # List of models ID
    # Precision 3581 - 0A68
    # Precision 3571 - 0B04
    # Precision 3561 - 0C07
    # Latitude 5420 - 0B10
    # Latitude 5430 - 0A20
    system_ids_to_check = ['0A68', '0B04', '0C07', '0B10', '0A20']
    
    # Iterate over all 'SoftwareComponent' elements
    for component in root.findall(".//SoftwareComponent"):
        # Check for 'ComponentType' with value 'BIOS'
        component_type = component.find(".//ComponentType[@value='BIOS']")
        if component_type is not None:
            # Check for 'Model' with any of the specified system IDs
            model = component.find(".//Model")
            if model is not None and model.get('systemID') in system_ids_to_check:
                # Find the 'Display' element inside 'Name'
                display_element = component.find(".//Name/Display")
                # Get the 'path' attribute from the 'SoftwareComponent' element
                path = component.get("path")
                if display_element is not None and path is not None:
                    display_text = display_element.text
                    results.append((display_text, path))
    
    return results


def download_bios_files(parsed_results, output_directory):
    for display_text, path in parsed_results:
        # Construct the URL
        url = f"https://dl.dell.com/{path}"
        # Create the output file path
        output_file_path = os.path.join(output_directory, os.path.basename(path))
        # Download the file
        print(f"Downloading {url} to {output_file_path}...")
        urllib.request.urlretrieve(url, output_file_path)
        print(f"Downloaded {url}")

file_path = 'CatalogPC.xml'
output_directory = 'bios_files'

os.makedirs(output_directory, exist_ok=True)

parsed_results = parse_xml(file_path)

# Print the BIOS firmware details and paths
for display_text, path in parsed_results:
    print(f"FOUND! BIOS Firmware: {display_text}\nURL: https://dl.dell.com/{path}\n")

# Download the BIOS files
download_bios_files(parsed_results, output_directory)