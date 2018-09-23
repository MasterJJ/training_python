#!/usr/bin/env python3
# -*- coding: utf-* -*-

import os

from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('tempfile.1')
    os.remove('tempfile.2')
    os.remove('tempfile.3')

