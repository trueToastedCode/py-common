def build_make_solve_recaptcha(TwoCaptcha):
    def make_solve_recaptcha(api_key):
        two_captcha = TwoCaptcha(api_key)
        def solve_recaptcha(site_key, netloc):
            return two_captcha.solve_captcha(site_key, netloc)
        return solve_recaptcha
    return make_solve_recaptcha
