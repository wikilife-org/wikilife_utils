# coding=utf-8

class LogCreator(object):
    """
    Raw logs
    """

    @staticmethod
    def create_log_node(node_id, metric_id, value):
        return {
            "nodeId": node_id,
            "metricId": metric_id,
            "value": value
        }

    @staticmethod
    def create_log(user_id, start, end, text, source, nodes):
        return {
            "id": 0,
            "userId": user_id,
            "start": start,
            "end": start,
            "text": text,
            "source": source,
            "nodes": nodes
        }
