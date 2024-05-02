from twocaptcha import TwoCaptcha

from .solve_recaptcha import build_make_solve_recaptcha

make_solve_recaptcha = build_make_solve_recaptcha(TwoCaptcha)
