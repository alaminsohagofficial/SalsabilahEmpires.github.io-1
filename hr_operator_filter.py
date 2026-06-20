# Salsabilah-Empire-OS - HR Module Sandbox (Pro Edition)
# Inspired by Global Industrial Benchmarks (ACI Motors/Yamaha)
from datetime import datetime

class SystemOperatorFilter:
    def __init__(self):
        # Global Standard Deadline Setup
        self.min_deadline = datetime.strptime("2026-05-30", "%Y-%m-%d")
        self.required_capabilities = [
            "Quarterly Strategic Planning",
            "Monthly P&L Statement Monitoring",
            "Cash Flow Evaluation",
            "Institutional Sales Expansion"
        ]

    def evaluate_candidate(self, capabilities, segment_budget_experience, application_date_str):
        # 1. Deadline Verification
        try:
            app_date = datetime.strptime(application_date_str, "%Y-%m-%d")
        except ValueError:
            return {"STATUS": "REJECTED", "REASON": "INVALID_DATE_FORMAT"}

        if app_date > self.min_deadline:
            return {"STATUS": "NON_COMPLIANT", "REASON": "DEADLINE_EXCEEDED"}

        # 2. Budget Experience and Capability Matching Check
        missing_caps = [cap for cap in self.required_capabilities if cap not in capabilities]
        total_caps = len(self.required_capabilities)
        matched_caps = total_caps - len(missing_caps)
        compliance_score = (matched_caps / total_caps) * 100

        # 3. Final Decision Engine
        if segment_budget_experience and compliance_score == 100:
            return {
                "STATUS": "COMPLIANT - PROCEED TO SOVEREIGN COMMAND",
                "SCORE": f"{compliance_score}%",
                "MISSING_CORE_CAPABILITIES": None
            }
        else:
            return {
                "STATUS": "NON_COMPLIANT - FILTER NOISE",
                "SCORE": f"{compliance_score}%",
                "MISSING_CORE_CAPABILITIES": missing_caps if missing_caps else "None (Budget Experience Missing)"
            }

# ==========================================
# OS Sandbox Execution Example
# ==========================================
operator_test = SystemOperatorFilter()

# Demo Candidate Dataset
candidate_caps = [
    "Quarterly Strategic Planning",
    "Monthly P&L Statement Monitoring",
    "Cash Flow Evaluation"
]

result = operator_test.evaluate_candidate(
    capabilities=candidate_caps,
    segment_budget_experience=True,
    application_date_str="2026-05-25"
)

print(result)
