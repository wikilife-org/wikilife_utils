# coding=utf-8

import os
import base64
import hashlib


class Hasher(object):

    @staticmethod
    def create_sha256(raw_str):
        hasher = hashlib.sha256()
        hasher.update(str(raw_str))
        return hasher.hexdigest()

    @staticmethod
    def create_pseudo_unique(hash_length):
        puhash = base64.b64encode(os.urandom(hash_length))[:hash_length]
        puhash = puhash.replace("+", "-")
        puhash = puhash.replace("/", "_")
        puhash = puhash.replace("=", ".")
        return puhash
