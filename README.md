The Python project get a bulk list of IP addresses in a CSV file (one ip per row) 
and do a "nslookup" command for each and give a CSV file output and write the data next to each ip in result csv file.

The code will try to find the **PTR** record of each IP in the DNS server. Usually when there is an **A** DNS record, there should be a PTR record for that.
For example, if the DNS server has a record like:
DNS A record:  **www.ABC.com** **172.20.20.20**
so the DNS server answer the request of :
**PTR** record= **20.20.20.172.in-addr.arpa**
with: **A** record= **172.20.20.20** **john-PC**

**Usage**: 
first create a csv file that only contain one column and each row only must contain one IP address without any subnet mask in any form. The file name must be "input.csv" and it should be available where the python code runs.


**example CSV file content**: ( if the input.csv is opened by a text editor, this is how it must look like)
172.20.5.11
172.20.5.12
172.20.5.17
172.20.5.46

**Note** that the default DNS server in this code has set to **192.168.1.1** ,so **change** it with your real dns server.

> python ns.py


and the **output** would written a file named: "output.csv"

Also make sure you have the require libraries installed before running the code:
> pip install csv
