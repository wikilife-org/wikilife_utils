# coding=utf-8
import itertools

class KwargsUtils(object):
        
    @staticmethod
    def get_arg_matrix(arg_map):
        """
        Tranform

        {"a": [1, 2, 3], "b": [1], "c": [1, 2]}

        to

        [
            {"a": 1, "b": 1, "c": 1},
            {"a": 2, "b": 1, "c": 2},
            {"a": 3, "b": 1, "c": 1},
            {"a": 1, "b": 1, "c": 2},
            {"a": 2, "b": 1, "c": 1},
            {"a": 3, "b": 1, "c": 2}
        ]
        
        :param args_map: Arguments with list of values 
        :type args_map: dict
        
        :rtype: list
        """

        product = [x for x in apply(itertools.product, arg_map.values())]
        return [dict(zip(arg_map.keys(), p)) for p in product]
