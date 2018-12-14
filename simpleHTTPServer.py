#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import argparse
import http.server
import socketserver


def get_host_ip():
    """Query the local IP address"""

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except:
        print("Currently there seems to be no internet connection.")
    finally:
        s.close()

    return ip


def get_port():
    """Get the port from user input (default: 8000)"""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", dest="port", type=int, default=8000,
        help="the port of HTTP server"
    )
    args = parser.parse_args()
    return args.port


def main(host, port):

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer((host, port), Handler) as httpd:
        print(
            "Serving HTTP on {0} port {1} (http://{0}:{1}/) ...".format(host, port)
        )
        httpd.serve_forever()
        


if __name__ == "__main__":
    main(get_host_ip(), get_port())
