import inspect

from ..custom_error.index import CustomError

from .default_controller import build_make_default_controller

make_default_controller = build_make_default_controller(CustomError, inspect)
