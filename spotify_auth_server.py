# Author : Nathaniel Thoma


# Libraries
import http.server   # provides classes for building simple HTTP servers
import socketserver  # provides the TCPServer class for creating socket-based servers
import urllib.parse  # provides functions for parsing URLs and query strings


# Classes

class SpotifyAuthHandler(http.server.SimpleHTTPRequestHandler):  # define a custom HTTP request handler class
    def do_GET(self):                                            # override do_GET method to handle GET requests
        query = urllib.parse.urlparse(self.path).query           # parse the query string from the requested URL
        params = urllib.parse.parse_qs(query)                    # parse the query parameters from the query string

        if 'code' in params:  # Check if the 'code' parameter is present in the query parameters
            code = params['code'][0]                     # Extract the value of the 'code' parameter
            self.server.auth_code = code                 # Store the received authorization code in the server instance
            self.send_response(200, 'OK')  # Send an HTTP response with a success status code (200)
            self.send_header('Content-type', 'text/html')                    # Set the content type header
            self.end_headers()                                                             # End the HTTP headers
            self.wfile.write(b'Authorization code received. You can close this tab now.')  # message


# Functions
def run_auth_server():
    PORT = 8888                   # define the port number on which the server will listen
    Handler = SpotifyAuthHandler  # define the handler class to use for incoming requests

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Listening for authorization code on port {PORT}")  # indicates that the server is waiting for code
        httpd.auth_code = None                                     # Initialize the auth_code to None
        httpd.handle_request()                                     # Handle an incoming request
        return httpd.auth_code                                     # Return the auth_code captured from the request


# Main
if __name__ == "__main__":
    auth_code = run_auth_server()
    print("Authorization code:", auth_code)
