"""
Authentification OAuth 2.0 pour l'API Tidal avec PKCE. 
Alternative robuste au système d'authentification Device Code.
"""
import json
import logging
import secrets
import time
import webbrowser
import hashlib
import base64
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlencode, urlparse, parse_qs
import requests
from threading import Thread
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CallbackHandler(BaseHTTPRequestHandler):
    """Gestionnaire pour le serveur de callback OAuth."""
    
    auth_code = None
    error = None
    
    def do_GET(self):
        """Gère la requête GET du callback."""
        try:
            query = urlparse(self.path).query
            params = parse_qs(query)
            
            if 'code' in params:
                CallbackHandler.auth_code = params['code'][0]
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile. write(b"""
                    <html>
                        <head><title>Authentication Success</title></head>
                        <body style="font-family: Arial; text-align: center; padding: 50px;">
                            <h1>Authentication Successful!</h1>
                            <p>You can close this window and return to the application.</p>
                        </body>
                    </html>
                """)
            elif 'error' in params:
                CallbackHandler.error = params['error'][0]
                self.send_response(400)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f"""
                    <html>
                        <head><title>Authentication
