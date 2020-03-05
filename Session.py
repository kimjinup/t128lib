#!/usr/bin/env python3

import urllib3
import json


class T128Error(Exception):
    pass


class Session:
    def __init__(self, host, username, password, port=443):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.authorization = None
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.http = urllib3.PoolManager(cert_reqs='CERT_NONE')
        self.host_url = 'https://' + self.host + ':' + str(self.port)
        self.headers = {'Content-Type': 'application/json', 'accept': 'application/JSON'}
        self.authorized_headers = self.headers

    def connect(self):
        api = '/api/v1/login'
        url = self.host_url + api
        data = {'username': self.username, 'password': self.password}
        encoded_data = json.dumps(data).encode('utf-8')
        response = self.http.request('POST', url, body=encoded_data, headers=self.headers)
        print(response.data)
        if response.status == 200:
            self.authorization = 'Bearer ' + json.loads(response.data.decode('utf-8'))['token']
            self.authorized_headers['Authorization'] = self.authorization
        else:
            raise T128Error('RESPONSE Code ' + str(response.status) + 'in the call ' + api )

    def commit(self):
        api = '/api/v1/config/commit'
        url = self.host_url + api
        response = self.http.request('post', url, headers=self.authorized_headers)
        return response.status

    def create_service(self, service_name):
        api = '/api/v1/config/candidate/authority/service'
        url = self.host_url + api
        data = {'name': service_name}
        encoded_data = json.dumps(data).encode('utf-8')
        response = self.http.request('post', url, body=encoded_data, headers=self.authorized_headers)
        return response.data

    def add_service_addresses(self, service_name, service_addresses):
        api = '/api/v1/config/candidate/authority/service/' + service_name
        url = self.host_url + api
        data = {'address': service_addresses}
        body = json.dumps(data).encode('utf-8')
        response = self.http.request('patch', url, body=body, headers=self.authorized_headers)
        return response.data

    def create_router(self, router_name):
        api = '/api/v1/config/candidate/authority/router'
        url = self.host_url + api
        data = {'name': router_name}
        body = json.dumps(data).encode('utf-8')
        response = self.http.request('post', url, body=body, headers=self.authorized_headers)
        if response.status != 201:
            raise T128Error('\nstatus: ' + str(response.status) + ' \ndata: ' + str(response.data.decode('utf-8')))
        return response.data

