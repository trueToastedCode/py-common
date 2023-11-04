import asyncio
from awaits.awaitable import awaitable
import inspect

from .race_functions import make_race_functions

race_functions = make_race_functions(asyncio, awaitable, inspect)
