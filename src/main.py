from.baseline_guard import BaselineGuard
from.trust_engine import TrustEngine

guard = BaselineGuard()
trust = TrustEngine()

activities = [10, 12, 14, 15, 30, 32]

for activity in activities:
    result = guard.check(activity)
    score, risk = trust.evaluate(result)

    print(
        f"Activity: {activity} | "
        f"Result: {result} | "
        f"Trust Score: {score} | "
        f"Risk: {risk}"
    )
    