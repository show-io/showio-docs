import csv
import re
import sys

def extract_info(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        
    title_match = re.search(r'^#\s+(.*)', content)
    title = title_match.group(1).strip() if title_match else None
    
    address_match = re.search(r'```\s*\n\s*(/\S+)', content)
    address = address_match.group(1).strip() if address_match else None
    
    return title, address

if __name__ == "__main__":
    files = sys.argv[1:]
    
    with open('osc_commands.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['title', 'address'])
        
        for file in files:
            title, address = extract_info(file)
            if title and address:
                writer.writerow([title, address])
            # also check for just a title and no address
            elif title:
                writer.writerow([title, ''])
