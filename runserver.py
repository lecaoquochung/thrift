#!/usr/bin/env python

import os
import BaseHTTPServer
import CGIHTTPServer

class Handler(CGIHTTPServer.CGIHTTPRequestHandler):
cgi_directories = ['/']
print "Starting server on port 4747..."
BaseHTTPServer.HTTPServer(('', 4747), Handler).serve_forever()
