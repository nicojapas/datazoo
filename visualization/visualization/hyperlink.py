#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Nicolás Japas.
# Distributed under the terms of the Modified BSD License.

"""
TODO: Add module docstring
"""

from ipywidgets import DOMWidget, ValueWidget, register
from traitlets import Unicode, Bool, validate, TraitError

from ._frontend import module_name, module_version
from IPython.core.display import display, HTML

class HyperlinkWidget(DOMWidget):
    """TODO: Add docstring here
    """
    _model_name = Unicode('HyperlinkModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('HyperlinkView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    value = Unicode('DataZoo website!').tag(sync=True)
