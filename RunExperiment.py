import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000

os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        webbrowser.open(f"http://localhost:{PORT}/experiment.html")
        httpd.serve_forever()

except KeyboardInterrupt:
    print("\nServer interrupted. Closing...")
    httpd.shutdown()
    sys.exit(0)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)