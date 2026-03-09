def run_code(code):

    try:
        local_vars = {}
        exec(code, {}, local_vars)
        return local_vars

    except Exception as e:
        return str(e)