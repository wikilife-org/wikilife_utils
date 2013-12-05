# coding=utf-8

from wikilife_utils.parsers.json_parser import JSONParser
import pika


class QueuePublisherException(Exception):
    pass


class QueuePublisher(object):
    """
    Queue client to write
    """
    _host = None
    _port = None
    _name = None
    _connection = None
    _channel = None
    _push_properties = None

    def __init__(self, queue_settings):
        self._host = queue_settings["host"]
        self._port = queue_settings["port"]
        self._name = queue_settings["name"]

    def open_conn(self):
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self._host, port=self._port))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=self._name, durable=True)
        self._push_properties = pika.BasicProperties(delivery_mode=2,)  # make message persistent

    def close_conn(self):
        self._channel.queue_purge(None, 0, self._name)
        self._connection.close()
        self._connection = None
        self._channel = None
        self._push_properties = None

    def publish(self, message):
        """
        message: Python serializable object
        Raises: QueuePublisherException, AMQP/Pika related exceptions
        """

        if self._channel == None:
            raise QueuePublisherException("connection is closed")

        if message == None:
            raise QueuePublisherException("message cannot be None")

        serialized_message = JSONParser.to_json(message)
        self._channel.basic_publish(exchange='', routing_key=self._name, body=serialized_message, properties=self._push_properties)
