# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# picasso is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Pytest fixtures and plugins for the UI application."""

from __future__ import absolute_import, print_function

import pytest
from invenio_app.factory import create_app as create_ui_api


@pytest.fixture(scope='module')
def create_app():
    """Create test app."""
    return create_ui_api
