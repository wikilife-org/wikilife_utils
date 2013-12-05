# coding=utf-8


class NodeValueValidatorException(Exception):
    pass


class NodeValueValidator(object):
    """
    Validates range, text and date value nodes
    """

    _meta_mgr = None

    def __init__(self, meta_manager):
        self._meta_mgr = meta_manager

    @staticmethod
    def is_range_value_node(node):
        return "properties" in node["fields"] and "value_type" in node["fields"]["properties"] and node["fields"]["properties"]["value_type"] == "range"

    @staticmethod
    def is_text_value_node(node):
        return "properties" in node["fields"] and "value_type" in node["fields"]["properties"] and node["fields"]["properties"]["value_type"] == "text"

    @staticmethod
    def is_date_value_node(node):
        return "properties" in node["fields"] and "value_type" in node["fields"]["properties"] and node["fields"]["properties"]["value_type"] == "datetime"

    def validate_text_node_value(self, value, value_node_id=None, value_node=None):
        """
        value: Number
        value_node_id: Integer
        """

        if not value_node:
            value_node = self._meta_mgr.get_node_by_id(value_node_id)

        if value_node == None:
            raise NodeValueValidatorException("Node not found %s" %value_node_id)

        options = value_node["fields"]["properties"]["options"]

        if not value in options:
            raise NodeValueValidatorException("Option not valid: %s %s" %(value, value_node))

    def validate_range_node_value(self, value, value_node_id=None, value_node=None):
        """
        value: Number
        value_node_id: Integer
        """
        if  not value_node:
            value_node = self._meta_mgr.get_node_by_id(value_node_id)

        if value_node == None:
            raise NodeValueValidatorException("Node not found %s" %value_node_id)

        min = float(value_node["fields"]["properties"]["min_value"])
        max = float(value_node["fields"]["properties"]["max_value"])

        if value < min or value > max:
            raise NodeValueValidatorException("Value out of range: %s %s" %(value, value_node))

    def validate_node_value(self, value, value_node_id):
        """
        value: Obj
        value_node_id: Integer
        """
        value_node = self._meta_mgr.get_node_by_id(value_node_id)

        if self.is_range_value_node(value_node):
            self.validate_range_node_value(float(value), value_node= value_node)

        elif self.is_text_value_node(value_node):
            self.validate_text_node_value(value, value_node= value_node)
