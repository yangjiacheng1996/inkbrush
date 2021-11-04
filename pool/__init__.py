#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path


class _Pool(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__


pool = _Pool()
project_root = Path(__file__).resolve().parent.parent
