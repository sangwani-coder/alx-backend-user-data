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
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if path[-1] != "/":
            path = path + "/"
            if path not in excluded_paths:
                return True
            else:
                return False
        return False

    def authorization_header(self, request=None) -> str:
        """ public method
            Return - None
        """
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('user'):
        """ public method
        Return - None
        """
        return None
