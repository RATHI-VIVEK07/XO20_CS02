import random
from datetime import datetime, timedelta

IDENTITIES = [
    "service_A",
    "service_B",
    "service_C"
]

ACTIONS = [
    "READ",
    "WRITE",
    "CALL"
]

RESOURCES = [
    "database",
    "payment_api",
    "analytics_api"
]


def generate_event(identity):
    event = {
        "identity": identity,
        "action": random.choice(ACTIONS),
        "resource": random.choice(RESOURCES),
        "timestamp": datetime.now().isoformat()
    }

    return event


if __name__=="__main__":
    print("Synthetic Identity Activity")

    for _ in range(10):
        identity = random.choice(IDENTITIES)
        event = generate_event(identity)
        print(event)

