# coding=utf-8

from wikilife_utils.parsers.json_parser import JSONParser, JSONParserException
import pika


class QueueConsumerException(Exception):
    pass


class QueueConsumer(object):
    """
    Queue client to read
    """
    _logger = None
    _host = None
    _port = None
    _name = None
    _connection = None
    _channel = None
    _callback = None

    def __init__(self, logger, queue_settings):
        self._logger = logger
        self._host = queue_settings["host"]
        self._port = queue_settings["port"]
        self._name = queue_settings["name"]

    def start(self, callback):
        """
        Start listening for messages from the Queue\
        callback: Function closure. Boolean foo(message)
        """

        self._callback = callback

        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=self._host, port=self._port))
            channel = connection.channel()
            channel.queue_declare(queue=self._name, durable=True)
            channel.basic_qos(prefetch_count=1)
            channel.basic_consume(self._internal_callback, queue=self._name)
            self._connection = connection
            self._channel = channel
            channel.start_consuming()

        except Exception, e:
            raise QueueConsumerException(e)

    def _internal_callback(self, ch, method, properties, body):
        try:
            data = JSONParser.to_collection(body)
            success = self._callback(data)

            if success:
                ch.basic_ack(delivery_tag=method.delivery_tag)

        except JSONParserException, e:
            self._logger.error(e)
            ch.basic_ack(delivery_tag=method.delivery_tag)

        except Exception, e:
            raise QueueConsumerException(e)
