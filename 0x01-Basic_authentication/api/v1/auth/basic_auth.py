#!/usr/bin/env python3
""" Basic Auth"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ inherit Auth"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ extracts Base64"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        space = ' '
        if space in authorization_header:
            auth = authorization_header.split()
            if auth[0] != "Basic":
                return None
            return auth[1]
