from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html>
<head>
<title>TCP/IP Protocol Suite</title>
<style>
    body { font-family: Arial, sans-serif; background: #f4f6f8; margin: 0; padding: 20px; }
    h1 { text-align: center; color: #1a3c6e; }
    h3 { text-align: center; color: #444; }
    table { border-collapse: collapse; width: 80%; margin: 20px auto; background: white; }
    th, td { border: 1px solid #999; padding: 10px 14px; text-align: left; }
    th { background: #1a3c6e; color: white; }
    tr:nth-child(even) { background: #eef2f7; }
</style>
</head>
<body>
    <h1>List of Protocols in the TCP/IP Protocol Suite</h1>
    <h3>Name: Krishna Prasath &nbsp;|&nbsp; Register No: 26017238</h3>
    <table>
        <tr><th>Layer</th><th>Protocols</th></tr>
        <tr><td>Application Layer</td><td>HTTP, HTTPS, FTP, SMTP, POP3, IMAP, DNS, DHCP, Telnet, SSH, SNMP, TFTP</td></tr>
        <tr><td>Transport Layer</td><td>TCP, UDP, SCTP</td></tr>
        <tr><td>Internet (Network) Layer</td><td>IP (IPv4, IPv6), ICMP, IGMP, ARP, RARP, IPsec</td></tr>
        <tr><td>Network Access (Link) Layer</td><td>Ethernet, Wi-Fi (802.11), PPP, Frame Relay, ATM</td></tr>
    </table>
</body>
</html>
"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)
print("My webserver is running...")
httpd.serve_forever()