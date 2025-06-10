import re
from waf_rules import WAFRule, WAF_RULES 
from request_simulator import SimulatedHttpRequest

class WAFEngine:
    def __init__(self, rules=WAF_RULES):
        self.rules = rules

    def inspect_request(self, request: SimulatedHttpRequest):
        """
        Inspects a simulated HTTP request against all defined WAF rules.
        Returns a list of detected threats.
        """
        detected_threats = []
        inspect_content = request.get_inspectable_content()

        for rule in self.rules:
            # For simplicity, we currently inspect 'url_and_body'
            # In a real WAF, you'd check `target_part` and inspect specific parts
            if rule.target_part == "url_and_body":
                match = re.search(rule.pattern, inspect_content, re.IGNORECASE)
                if match:
                    detected_threats.append({
                        "rule_id": rule.id,
                        "rule_name": rule.name,
                        "matched_pattern": rule.pattern,
                        "matched_text": match.group(0), # The actual text that matched
                        "action": rule.action,
                        "request_url": request.url
                    })
            # Add more 'target_part' conditions here if you expand (e.g., 'headers')

        return detected_threats

    def add_rule(self, rule: WAFRule):
        self.rules.append(rule)
        print(f"Added new rule: {rule.name}")

    def remove_rule(self, rule_id):
        self.rules = [rule for rule in self.rules if rule.id != rule_id]
        print(f"Removed rule with ID: {rule_id}")

    def list_rules(self):
        print("\n--- Current WAF Rules ---")
        for rule in self.rules:
            print(f"ID: {rule.id} | Name: {rule.name} | Pattern: '{rule.pattern}' | Target: {rule.target_part} | Action: {rule.action}")
        print("-------------------------\n")