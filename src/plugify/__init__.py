"""
plugify.py
~~~~~~~~~~
Pythonic API Wrapper For https://plugify.cf

:copyright: 2021 RPS
:license: Apache-2.0
"""

__title__ = "plugify"
__author__ = "RPS"
__license__ = "Apache-2.0"
__copyright__ = "Copyright 2021 RPS"
__version__ = "0.0.1"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import logging
from typing import NamedTuple, Literal

# Official API
from .http import *
from .client import *
from .dispatch import *
from .group import *
from .members import *
from .gateway import *

# User API
# from .user_api import *

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(
    major=0, minor=0, micro=1, releaselevel="candidate", serial=0
)

logging.getLogger(__name__).addHandler(logging.NullHandler())