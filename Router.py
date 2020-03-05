#!/usr/bin/env python3


class NetworkInterface:
    def __init__(self):
        self.address = None
        self.dhcp = False
        pass


class EthernetInterface:
    def __init__(self, name, pci_address):
        self.pci_address = pci_address


class PPPoEInterface:
    def __init__(self, user_name, password, authentication_protocol):
        self.user_name = user_name
        self.password = password
        self.authentication_protocol = authentication_protocol


class LTEInterface:
    def __init__(self,apn_name, user_name, password, authentication_protocol):
        self.apn_name = apn_name
        self.user_name = user_name
        self.password = password
        self.authentication_protocol = authentication_protocol


class Node:
    def __init__(self, name, role, asset_id):
        self.name = name
        self.role = role
        self.asset_id = asset_id


class Router:
    def __init__(self, name):
        self.name = name
        self.application_id = True
        self.node = None
