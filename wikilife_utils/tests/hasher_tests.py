# coding=utf-8

from wikilife_utils.hasher import Hasher
import unittest

class HasherTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_create_sha256(self):
        raw_str = "abc123"
        hash_str = Hasher.create_sha256(raw_str)
        print hash_str
        assert hash_str != None

    def test_create_pseudo_unique(self): 
        hash_str = Hasher.create_pseudo_unique(16)
        print hash_str
        assert hash_str != None
        assert len(hash_str) == 16
