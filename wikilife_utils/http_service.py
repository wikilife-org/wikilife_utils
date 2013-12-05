# coding=utf-8

import json
import urllib2
import requests

JSON = "json"
XML = "xml"
TEXT = "text"


class ResponseParser(object):

    def parse(self, response, fmt):
        if fmt == TEXT:
            return response
        elif fmt == JSON:
            return self.parse_json(response)
        elif fmt == XML:
            return self.parse_xml(response)
        else:
            raise Exception("unknown format: {}".format(fmt))

    def parse_json(self, response):
        response = json.loads(response)
        return response

    def parse_xml(self, response):
        raise Exception("XML parser not implemented")


class HTTPService(object):

    _parser = ResponseParser()

    def request_get(self, url, params=None, parse_format=JSON):
        """
        url: String
        params: Dict<String, String>
        parse_format: String. See constants
        """
        if params:
            url = self._get_url_with_qs(url, params)

        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        response = response.read()
        response = self._parser.parse(response, parse_format)
        return response

    def request_post(self, url, params=None, body="", headers={'Content-Type': 'application/json'}, parse_format=JSON):
        """
        url: String
        params: Dict<String, String>
        body: String
        headers: Dict<String, String>
        parse_format: String. See constants
        """
        if params:
            url = self._get_url_with_qs(url, params)

        #TODO elegantize
        if headers != None:
            response = requests.post(url, body,  headers=headers)
        else:
            response = requests.post(url, body)

        
        response = self._parser.parse(response.content, parse_format)
        return response

    def _get_url_with_qs(self, url, params):
        qs = ""
        for key in params:
            value = str(params[key])
            value = urllib2.quote(value)
            qs = "%s=%s&" % (key, value)

        return "%s?%s" % (url, qs)
