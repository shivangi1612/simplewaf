import streamlit as st
from request_simulator import SimulatedHttpRequest
from waf_engine import WAFEngine
from waf_rules import WAFRule, WAF_RULES # Make sure WAFRule is imported here too!

# Initialize the WAF Engine (can be done once)
# Using st.session_state to persist the WAF engine and rules
if 'waf_engine' not in st.session_state:
    st.session_state.waf_engine = WAFEngine()

st.set_page_config(
    page_title="SimpleWAF: Web Application Firewall Simulator",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ SimpleWAF: Web Application Firewall Simulator")
st.markdown("---")

st.subheader("Simulate an HTTP Request")

request_type = st.radio(
    "Choose Request Type:",
    ("GET", "POST"),
    horizontal=True
)

url_input = st.text_input("Enter URL (e.g., /search?q=test):", value="/")

body_input = ""
if request_type == "POST":
    body_input = st.text_area("Enter Request Body (for POST requests):", height=100)

if st.button("🚀 Run Simulation"):
    with st.spinner("🔎 Inspecting request..."):
        request = SimulatedHttpRequest(method=request_type, url=url_input, body=body_input)
        threats = st.session_state.waf_engine.inspect_request(request)

        st.markdown("### 📊 Simulation Results")
        if threats:
            st.error("🚨 THREAT DETECTED! 🚨")
            for threat in threats:
                st.json(threat) # Display threat details as JSON for clarity
            st.markdown("---")
            st.warning("⚠️ Note: In a real WAF, this request would typically be blocked or flagged.")
        else:
            st.success("✅ Request Clean! No immediate threats detected.")
            st.write("This request passed all active WAF rules.")

st.markdown("---")

st.subheader("⚙️ WAF Rule Management")

rule_action = st.radio(
    "Choose Rule Action:",
    ("View Rules", "Add New Rule", "Remove Rule"),
    horizontal=True
)

if rule_action == "View Rules":
    st.markdown("#### Current WAF Rules")
    if not st.session_state.waf_engine.rules:
        st.info("No rules currently loaded.")
    else:
        # Create a list of dictionaries for easier display
        rules_data = []
        for rule in st.session_state.waf_engine.rules:
            rules_data.append({
                "ID": rule.id,
                "Name": rule.name,
                "Pattern": rule.pattern,
                "Target": rule.target_part,
                "Action": rule.action
            })
        st.dataframe(rules_data, height=300) # Display rules in a nice table

elif rule_action == "Add New Rule":
    st.markdown("#### 🛠️ Add a Custom WAF Rule")
    with st.form("add_rule_form"):
        new_rule_id = st.number_input("Rule ID (e.g., 2001):", min_value=1, value=len(WAF_RULES) + 1)
        new_rule_name = st.text_input("Rule Name (e.g., 'Custom Malicious IP Block'):")
        new_rule_pattern = st.text_input("Regex Pattern (e.g., 'bad_ip_address'):")
        # For simplicity, target_part is fixed for custom rules in this UI
        # new_rule_target = st.selectbox("Target Part:", ("url_and_body", "url", "body", "headers"))
        new_rule_action = st.selectbox("Action:", ("block", "log", "alert"))

        submitted = st.form_submit_button("💾 Add Rule")
        if submitted:
            if new_rule_id and new_rule_name and new_rule_pattern:
                try:
                    new_rule = WAFRule(new_rule_id, new_rule_name, new_rule_pattern, "url_and_body", new_rule_action)
                    st.session_state.waf_engine.add_rule(new_rule)
                    st.success(f"Rule '{new_rule_name}' (ID: {new_rule_id}) added successfully!")
                except Exception as e:
                    st.error(f"Error adding rule: {e}")
            else:
                st.warning("Please fill in all fields to add a rule.")

elif rule_action == "Remove Rule":
    st.markdown("#### ❌ Remove a WAF Rule")
    with st.form("remove_rule_form"):
        rule_ids = [rule.id for rule in st.session_state.waf_engine.rules]
        if not rule_ids:
            st.info("No rules to remove.")
            remove_id = None
        else:
            remove_id = st.selectbox("Select Rule ID to remove:", rule_ids)

        submitted_remove = st.form_submit_button("🗑️ Remove Rule")
        if submitted_remove and remove_id:
            try:
                st.session_state.waf_engine.remove_rule(remove_id)
                st.success(f"Rule ID {remove_id} removed successfully!")
            except Exception as e:
                st.error(f"Error removing rule: {e}")