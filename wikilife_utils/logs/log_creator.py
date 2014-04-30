# coding=utf-8

from wikilife_utils.formatters.date_formatter import DateFormatter


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

        if not isinstance(start, str):
            start = DateFormatter.to_datetime(start)

        if end and not isinstance(end, str):
            end = DateFormatter.to_datetime(end)

        return {
            "id": 0,
            "userId": user_id,
            "start": start,
            "end": end,
            "text": text,
            "source": source,
            "nodes": nodes
        }
