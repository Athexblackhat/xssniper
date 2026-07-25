#!/usr/bin/env python
# -*- coding: utf-8 -*-"
# vim: set expandtab tabstop=4 shiftwidth=4:

class xssniperReporter(object):
    """
    Base class for objects wanting to receive report information from xssniper.
    It implements all callbacks so you will be safe ;)
    """
    def start_attack(self):
        pass
    def end_attack(self):
        pass
    def mosquito_crashed(self, dest_url, reason="unknown"):
        pass
    def report_state(self, state):
        pass
    def add_link(self, orig_url, dest_url):
        pass
    def report_error(self, error_msg):
        pass
    def start_token_check(self, dest_url):
        pass
    def start_crawl(self, dest_url):
        pass
    def post(self, msg):
        pass
    def token_arrived(self, token):
        pass
    def add_checked(self, dest_url):
        pass
    def add_success(self, dest_url):
        pass
    def add_failure(self, dest_url):
        pass
