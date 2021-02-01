from mitmproxy import ctx
from mitmproxy import http


class ABC:
    def __init__(self):
        self.num = 0

    def request(self, flow: http.HTTPFlow) -> None:
        if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
            # print(flow.request.pretty_url)

            with open(r"./tmp.json", 'r', encoding="utf-8") as f:
                # print(f.read())
                flow.response = http.HTTPResponse.make(
                    200,  # (optional) status code
                    f.read(),  # (optional) content
                    {"Content-Type": "application/json"}  # (optional) headers
                )


addons = [
    ABC()
]
