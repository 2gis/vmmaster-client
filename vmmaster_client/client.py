# coding: utf-8
import requests
import json


class BadCommandStatus(Exception):
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return "Bad executed command status in response content:\n %s" % str(self.content)


class BadStatusCode(Exception):
    def __init__(self, response):
        self.response = response

    def __str__(self):
        return "Status code is not 200 in:\n code: %s\nheaders: %s\n\ncontent: %s" % (
            self.response.status_code, self.response.headers, self.response.content)


class vmmaster(object):
    _commands = {
        "run_script": ("POST", "/runScript"),
        "label": ("POST", "/vmmasterLabel")
    }

    def __init__(self, driver):
        self._driver = driver
        self.command_executor_url = driver.command_executor._url
        self.session_id = driver.session_id

    def _process_response(self, response):
        if response.status_code != 200:
            raise BadStatusCode(response)
        data = json.loads(response.content)
        if data.get('status', 1) > 0:
            raise BadCommandStatus(data)
        return data

    def _make_request(self, command, data):
        method, url = self._commands.get(command, None)
        if command is None:
            raise Exception("no such command: %s" % command)
        address = "%s/session/%s%s" % (self.command_executor_url, self.session_id, url)
        return self._process_response(requests.request(method, address, data=data))

    def run_script(self, script, command=None):
        data = {
            "script": script
        }
        if command:
            data.update({"command": command})
        return self._make_request("run_script", json.dumps(data))

    def label(self, label):
        data = {
            "label": label
        }
        return self._make_request("label", json.dumps(data))
