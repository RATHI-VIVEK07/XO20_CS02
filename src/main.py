from src.event_generator import generate_event, IDENTITIES
from src.baseline_guard import BaselineGuard
from src.trust_engine import TrustEngine

guard = BaselineGuard()
trust = TrustEngine()

print("=== Adaptive Behavioural Trust Engine ===")

for identity in IDENTITIES:
    print(f"\nIdentity: {identity}")

    for _ in range(5):
        event = generate_event(identity)

        # Convert event into an activity value
        activity = {
            "READ": 10,
            "CALL": 14,
            "WRITE": 15
        }[event["action"]]

        result = guard.check(activity)
        score, risk = trust.evaluate(result)

        print(
            f"Action: {event['action']} | "
            f"Resource: {event['resource']} | "
            f"Result: {result} | "
            f"Trust: {score} | "
            f"Risk: {risk}"
        )
    