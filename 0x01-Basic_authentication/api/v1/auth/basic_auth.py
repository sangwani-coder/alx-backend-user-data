#!/usr/bin/env python3
""" Basic Auth"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ returns the decoded value of a Base64 str """
        try:
            utf_val = authorization_header.encode('utf-8')
            decode = base64.b64decode(utf_val).decode('utf-8')
            return decode
        except (AttributeError, ValueError) as a:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ extracts user password and email"""
        if decoded_base64_authorization_header is None or \
                type(decoded_base64_authorization_header) is not str:
            return None, None
        colon = ":"
        if colon not in decoded_base64_authorization_header:
            return None, None
        cred = decoded_base64_authorization_header.split(':')
        return cred[0], cred[1]
