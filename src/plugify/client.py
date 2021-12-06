"""
Apache-2.0

Copyright 2021 RPS

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the LICENSE file for the specific language governing permissions and
limitations under the License.
"""
from __future__ import annotations

import asyncio
import logging
import signal
import sys
import traceback
from typing import (
    Any, 
    Callable, 
    Coroutine, 
    Dict, 
    Generator, 
    List, 
    Optional, 
    Sequence, 
    TYPE_CHECKING, 
    Tuple, 
    TypeVar, 
    Union
)

import aiohttp

class Client:
    pass


Coro = TypeVar('Coro', bound=Callable[..., Coroutine[Any, Any, Any]])