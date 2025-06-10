from request_simulator import SimulatedHttpRequest
from waf_engine import WAFEngine
from waf_rules import WAFRule, WAF_RULES

def run_simulation(waf_engine, request_url, request_body=""):
    print(f"\n--- Simulating Request ---")
    print(f"URL: {request_url}")
    if request_body:
        print(f"Body: {request_body}")
    print("--------------------------")

    request = SimulatedHttpRequest(url=request_url, body=request_body)
    threats = waf_engine.inspect_request(request)

    if threats:
        print("\n!!! THREAT DETECTED !!!")
        for threat in threats:
            print(f"  - Rule ID: {threat['rule_id']} ({threat['rule_name']})")
            print(f"    Matched Pattern: '{threat['matched_pattern']}'")
            print(f"    Matched Text: '{threat['matched_text']}'")
            print(f"    Action: {threat['action']}")
        print("---------------------------\n")
    else:
        print("\n--- Request Clean ---")
        print("No threats detected by WAF rules.\n")

def main():
    waf = WAFEngine()

    while True:
        print("\nPyWAF-Sim Menu:")
        print("1. Simulate a GET request (URL only)")
        print("2. Simulate a POST request (URL + Body)")
        print("3. List current WAF rules")
        print("4. Add a custom WAF rule (basic)")
        print("5. Remove a WAF rule by ID")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            url = input("Enter URL (e.g., /search?q=test): ")
            run_simulation(waf, url)
        elif choice == '2':
            url = input("Enter URL: ")
            body = input("Enter Request Body: ")
            run_simulation(waf, url, body)
        elif choice == '3':
            waf.list_rules()
        elif choice == '4':
            try:
                rule_id = int(input("Enter new Rule ID (e.g., 2001): "))
                rule_name = input("Enter Rule Name: ")
                rule_pattern = input("Enter Regex Pattern: ")
                # For simplicity, always target 'url_and_body' for custom rules
                waf.add_rule(WAFRule(rule_id, rule_name, rule_pattern, "url_and_body"))
            except ValueError:
                print("Invalid Rule ID. Please enter a number.")
        elif choice == '5':
            try:
                rule_id_to_remove = int(input("Enter Rule ID to remove: "))
                waf.remove_rule(rule_id_to_remove)
            except ValueError:
                print("Invalid Rule ID. Please enter a number.")
        elif choice == '6':
            print("Exiting PyWAF-Sim. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()