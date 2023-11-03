def build_make_default_controller(CustomError, inspect):
    def make_default_controller(uc_func, status_code=200):
        async def default_controller(*args, **kwargs):
            try:
                result = await uc_func(*args, **kwargs) \
                    if inspect.iscoroutinefunction(uc_func) \
                    else uc_func(*args, **kwargs)
                if result is None:
                    return { 'statusCode': status_code }
                return {
                    'statusCode': status_code,
                    'body': result
                }
            except Exception as e:
                return {
                    'statusCode': e.error_code if isinstance(e, CustomError) else 500,
                    'error': str(e)
                }

        return default_controller

    return make_default_controller
