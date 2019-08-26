class CorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        res = self.get_response(request)
        #res["Access-Control-Allow-Origin"] = "*"
        # res["Access-Control-Allow-Methods"] = "GET,OPTIONS,POST"
        # res["Access-Control-Allow-Headers"] = "content-type"
        return res