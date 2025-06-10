class WAFRule:
    def __init__(self, id, name, pattern, target_part, action="block"):
        self.id = id
        self.name = name
        self.pattern = pattern
        self.target_part = target_part
        self.action = action

    def __repr__(self):
        return f"Rule(ID:{self.id}, Name:'{self.name}', Target:'{self.target_part}', Action:'{self.action}')"

# A list of example rules
WAF_RULES = [
    WAFRule(1001, "SQL Injection - Basic OR 1=1",
            r"('|%27)\s*OR\s*(\d+)=(\d+)", "url_and_body"),
    WAFRule(1002, "SQL Injection - Basic Union Select",
            r"union\s+select", "url_and_body"),
    WAFRule(1003, "XSS - Script Tag",
            r"<script\b[^>]*>(.*?)</script>", "url_and_body"),
    WAFRule(1004, "XSS - Img onerror",
            r"<img\s+src\s*=\s*['\"]?[^'\"]*\s+onerror\s*=\s*['\"]?[^'\"]*['\"]?", "url_and_body"),
    WAFRule(1005, "Path Traversal - Double Dot Slash",
            r"\.\./|\.\.\\", "url_and_body"),
    WAFRule(1006, "Path Traversal - Encoded Double Dot Slash",
            r"%2e%2e%2f|%2e%2e%5c", "url_and_body"),
    WAFRule(1007, "Command Injection - Semicolon",
            r";\s*(cat|ls|pwd|whoami)", "url_and_body"),
    WAFRule(1008, "Command Injection - Pipe",
            r"\|\s*(cat|ls|pwd|whoami)", "url_and_body"),
    WAFRule(1009, "XSS - Basic Alert",
            r"alert\(", "url_and_body"),
    WAFRule(1010, "SQLi - Common Comments",
            r"(--|\/\*|\#)", "url_and_body")
]