class SimulatedHttpRequest:
    def __init__(self, method="GET", url="/", headers=None, body=""):
        self.method = method
        self.url = url
        self.headers = headers if headers is not None else {}
        self.body = body

    def __repr__(self):
        return (f"Method: {self.method}, URL: {self.url}\n"
                f"Headers: {self.headers}\n"
                f"Body: {self.body}\n")

    def get_inspectable_content(self):
        """Combines relevant parts of the request for inspection."""
        content = self.url
        if self.body:
            content += " " + self.body
        # For a more advanced version, you could add headers too
        return content.lower() # Convert to lowercase for case-insensitive matching