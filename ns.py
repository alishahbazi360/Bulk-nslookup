import csv
import subprocess
import time

input_file = 'input.csv'
output_file = 'output.csv'
dns_server = '192.168.1.1'

def nslookup(ip, dns_server):
    try:
        result = subprocess.run(
            ['nslookup', ip, dns_server],
            capture_output=True,
            text=True,
            timeout=2
        )
        output = result.stdout
        for line in output.splitlines():
            line = line.strip()
            if line.lower().startswith('name:'):
                return line.split(':', 1)[1].strip().strip('.')
            elif 'name =' in line.lower():
                return line.split('=', 1)[1].strip().strip('.')
            time.sleep(0.1)
        return ''
    except Exception as e:
        return f'Error: {e}'


# Read IPs from input CSV
with open(input_file, newline='') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Process each row
    for row in reader:
        ip = row[0].strip()
        hostname = nslookup(ip, dns_server)
        print("\n",ip,":",hostname)
        row.append(hostname)
        writer.writerow(row)

print("Done! Check 'output.csv' for results.")

