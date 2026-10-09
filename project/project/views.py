
from django.http import HttpResponse


def home(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Webserver</title>
    </head>
    <body>
        <h1>Simple Webserver</h1>
        <h2>Student Details</h2>
        <p>Name: Prasana S</p>
        <p>Register Number: 26017367</p>

        <h2>TCP/IP Protocol Suite</h2>
        <h3>Application Layer</h3>
        <p>HTTP, HTTPS, FTP, SMTP, DNS, DHCP</p>
        <h3>Transport Layer</h3>
        <p>TCP, UDP</p>
        <h3>Internet Layer</h3>
        <p>IP, ICMP</p>
        <h3>Network Access Layer</h3>
        <p>Ethernet, Wi-Fi</p>
    </body>
    </html>
    """
    return HttpResponse(html)