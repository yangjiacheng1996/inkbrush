#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import importlib
import importlib.util
import logging

class Grammar:
    def get_func_varnames(self, func):
        func_vars = func.__code__.co_varnames
        print(func_vars)
        return func_vars

    @staticmethod
    def import_module_from_spec(self,module_spec):
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        return module

    def check_module_exist_and_import(self,import_path:str):
        module_spec = importlib.util.find_spec(import_path)
        if module_spec is not None:
            module_object = self.import_module_from_spec(module_spec)
            logging.info("import module success: %s" % import_path)
            return module_object
        else:
            logging.info("Cannot find module : %s"%import_path)
            return None



