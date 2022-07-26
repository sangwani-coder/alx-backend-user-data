#!/usr/bin/env python3
""" API authentication """
from flask import request
from typing import List, TypeVar


class Auth():
    """ auth system template"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ public method
            Return: False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ public method
            Return - None
        """
        return None

    def current_user(self, request=None) -> TypeVar('user'):
        """ public method
        Return - None
        """
        return None
