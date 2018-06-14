from mitmproxy import http

# url: (file, contentType, status)
mapping = {
}

def request(flow: http.HTTPFlow) -> None:
    for url, (file, contentType, status) in mapping.items():
        if flow.request.pretty_url == url:
            with open(file, "r") as handler:
                flow.response = http.HTTPResponse.make(
                    status,
                    handler.read(),
                    {"Content-Type": contentType}
                )
