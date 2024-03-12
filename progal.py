from http.server import HTTPServer, BaseHTTPRequestHandler 
content = """ 
<html>
<head>
<title>Software Companies
</title>
</head>
<body bgcolor="orange">
<h1 align="center">Top 5 Revenue generating Companies</h1>
<table align="center" border="15" bordercolor="white" cellspacing="3" cellpadding="19" height="240" width="180">
<tr>
<th>Rank</th>
<th>Company</th>
<th>Sales</th>
<th>Nationality</th>
</tr>
<tr>
<td>1</td>
<td>Microsoft</td>
<td>57.9</td>
<td>USA</td>
</tr>
<tr>
<td>2</td>
<td>Oracle</td>
<td>21.0</td>
<td>USA</td>
</tr>
<tr>
<td>3</td>
<td>SAP</td>
<td>16.1</td>
<td>Germany</td>
</tr>
<tr>
<td>4</td>
<td>Computer Associates</td>
<td>4.2</td>
<td>USA</td>
</tr>
<tr>
<td>5</td>
<td>Adobe</td>
<td>3.4</td>
<td>USA</td>
</tr>
</table>
</body>
</html> """ 
class myhandler(BaseHTTPRequestHandler):    
    def do_GET(self):        
        print("request received")      
        self.send_response(200)        
        self.send_header('content-type', 'text/html; charset=utf-8')        
        self.end_headers()        
        self.wfile.write(content.encode()) 
server_address = ('',8000) 
httpd = HTTPServer(server_address,myhandler) 
print("my webserver is running...") 
httpd.serve_forever()