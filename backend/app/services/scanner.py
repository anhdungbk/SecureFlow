"""Multi-agent demo: Orchestrator -> Scanner -> Analyzer -> Remediator -> Tester (human reviews)."""
import re

RULES = {  # id: (regex, severity, explanation, fix)
    "sql-injection": (r'execute\(\s*f?["\'].*(\{|%s|\+)', "high",
                      "User input is concatenated into a SQL query.",
                      lambda l: re.sub(r'execute\(f"(.*?)\'?\{(\w+)\}\'?(.*?)"\)', r'execute("\1?\3", (\2,))', l)),
    "hardcoded-secret": (r'(password|secret|api_key)\s*=\s*["\'][^"\']+["\']', "critical",
                         "Credential committed in source code.",
                         lambda l: re.sub(r'=\s*["\'][^"\']+["\']', '= os.environ["SECRET"]', l)),
    "eval-usage": (r'\beval\(', "high", "eval() can execute arbitrary code.",
                   lambda l: l.replace("eval(", "ast.literal_eval(")),
}


def scan(src):
    return [{"line": n, "rule": r, "code": l.strip()}
            for n, l in enumerate(src.splitlines(), 1)
            for r, (rx, *_) in RULES.items() if re.search(rx, l)]


def analyze(findings):  # an LLM call would go here; rule metadata stands in for it
    return [{**f, "severity": RULES[f["rule"]][1], "why": RULES[f["rule"]][2]} for f in findings]


def remediate(src, findings):
    lines = src.splitlines()
    for f in findings:
        lines[f["line"] - 1] = RULES[f["rule"]][3](lines[f["line"] - 1])
    return "\n".join(lines)


def run_pipeline(src):
    findings = analyze(scan(src))
    patched = remediate(src, findings)
    return {"findings": findings, "patched": patched, "regression_passed": not scan(patched)}
