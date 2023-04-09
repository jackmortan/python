# import requests
# from bs4 import BeautifulSoup
# import csv

# # make a GET request to the URL
# url = "https://www.tec.com"
# response = requests.get(url)

# # parse the HTML content
# soup = BeautifulSoup(response.content, "html.parser")

# # find all the links in the HTML
# links = [link.get("href") for link in soup.find_all("a")]

# # write the links to a CSV file
# with open("links.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Links"])
#     for link in links:
#         writer.writerow([link])

from scapy.all import *
import sqlite3

# Open a connection to the SQLite database
conn = sqlite3.connect('packets.db')
c = conn.cursor()

# Create the packets table if it does not exist
c.execute('''CREATE TABLE IF NOT EXISTS packets
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              src_ip TEXT,
              dst_ip TEXT,
              protocol TEXT,
              length INTEGER)''')

def packet_callback(packet,IP(dst='192.168.198.45')/ICMP()):
    if packet.haslayer('192.168.198.45'):
        src_ip = packet['192.168.198.45'].src
        dst_ip = packet['192.168.198.45'].dst
        protocol = packet['192.168.198.45'].proto
        length = len(packet)
        # Insert the packet data into the database
        c.execute("INSERT INTO packets (src_ip, dst_ip, protocol, length) VALUES (?, ?, ?, ?)",
                  (src_ip, dst_ip, protocol, length))
        conn.commit()

# Start sniffing network packets and call the packet_callback function for each packet
sniff(prn=packet_callback)

# Close the database connection
conn.close()
