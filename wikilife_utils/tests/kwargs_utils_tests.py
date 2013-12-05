# coding=utf-8

import unittest
from wikilife_utils.kwargs_utils import KwargsUtils


class KwargsUtilsTests(unittest.TestCase):

    def test_get_arg_matrix_3_args(self):
    
        test_kwargs = {"a": ["a1", "a2", "a3"], "b": ["b1"], "c": ["c1", "c2"]}
        
        expected = [
         {'a': 'a1', 'b': 'b1', 'c': 'c1'}, 
         {'a': 'a2', 'b': 'b1', 'c': 'c2'}, 
         {'a': 'a3', 'b': 'b1', 'c': 'c1'}, 
         {'a': 'a1', 'b': 'b1', 'c': 'c2'}, 
         {'a': 'a2', 'b': 'b1', 'c': 'c1'}, 
         {'a': 'a3', 'b': 'b1', 'c': 'c2'}
        ]

        result = KwargsUtils.get_arg_matrix(test_kwargs)
        
        print test_kwargs 
        print result 
        
        self.assertItemsEqual(result, expected)

    def test_get_arg_matrix_4_args(self):
    
        test_kwargs = {"a": ["a1", "a2"], "b": ["b1", "b2"], "c": ["c1"], "d": ["d1"]}
        
        expected = [
         {'a': 'a1', 'b': 'b1', 'c': 'c1', 'd': 'd1'}, 
         {'a': 'a2', 'b': 'b1', 'c': 'c1', 'd': 'd1'}, 
         {'a': 'a1', 'b': 'b2', 'c': 'c1', 'd': 'd1'}, 
         {'a': 'a2', 'b': 'b2', 'c': 'c1', 'd': 'd1'} 
        ]

        result = KwargsUtils.get_arg_matrix(test_kwargs)
        
        print test_kwargs 
        print result 
        
        self.assertItemsEqual(result, expected)

    def test_get_arg_matrix_large(self):
    
        test_kwargs = {'tylenolacetaminophenpills': ['.*'], 'mood': ['.*'], 'weight': ['.*'], 'advilibupills': ['.*'], 'gender': ['Female', 'Male'], 'age': ['31\\-35', '36\\-40'], 'bmi': ['.*'], 'height': ['.*'], 'running': ['.*'], 'sleep': ['.*'], 'location': ['.*'], 'livingwith': ['.*'], 'smoking': ['.*'], 'sex': ['.*'], 'headache': ['.*']}
        
        expected = [
         {'gender': 'Female', 'age': '31\\-35', 'tylenolacetaminophenpills': '.*', 'mood': '.*', 'weight': '.*', 'advilibupills': '.*', 'bmi': '.*', 'height': '.*', 'running': '.*', 'sleep': '.*', 'location': '.*', 'livingwith': '.*', 'smoking': '.*', 'sex': '.*', 'headache': '.*'},
         {'gender': 'Female', 'age': '36\\-40', 'tylenolacetaminophenpills': '.*', 'mood': '.*', 'weight': '.*', 'advilibupills': '.*', 'bmi': '.*', 'height': '.*', 'running': '.*', 'sleep': '.*', 'location': '.*', 'livingwith': '.*', 'smoking': '.*', 'sex': '.*', 'headache': '.*'},
         {'gender': 'Male', 'age': '31\\-35', 'tylenolacetaminophenpills': '.*', 'mood': '.*', 'weight': '.*', 'advilibupills': '.*', 'bmi': '.*', 'height': '.*', 'running': '.*', 'sleep': '.*', 'location': '.*', 'livingwith': '.*', 'smoking': '.*', 'sex': '.*', 'headache': '.*'},
         {'gender': 'Male', 'age': '36\\-40', 'tylenolacetaminophenpills': '.*', 'mood': '.*', 'weight': '.*', 'advilibupills': '.*', 'bmi': '.*', 'height': '.*', 'running': '.*', 'sleep': '.*', 'location': '.*', 'livingwith': '.*', 'smoking': '.*', 'sex': '.*', 'headache': '.*'}
        ]

        result = KwargsUtils.get_arg_matrix(test_kwargs)
        
        print "##############" 
        print test_kwargs 
        print "--------------" 
        print result 
        print "--------------" 
        print expected 
        print "##############" 
        
        self.assertItemsEqual(result, expected)
