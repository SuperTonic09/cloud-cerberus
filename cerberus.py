#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author  : Roberto Sosa
# Created : October 2021
# Version : 0.1.2
# Status  : Prototype
# =============================================================================
"""Coding Exercise: Staff Security Engineer (Role)"""
# =============================================================================

import subprocess
import json

import cloud_auth
import sca_collection

cloud_auth.az_login()

print('\nCloud Cerberus checks starting...\n')

sca_collection.test_case_1()