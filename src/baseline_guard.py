class BaselineGuard:
    def __init__(self, baseline=10, threshold=5):
        self.baseline = baseline
        self.threshold = threshold

    def check(self, activity):
        change = activity - self.baseline

        # Sudden/unusual change
        if change > self.threshold:
            return "SUSPICIOUS - Baseline not updated"

        # Gradual legitimate change
        if change > 0:
            self.baseline = (self.baseline + activity) / 2
            return "LEGITIMATE - Baseline updated"

        return "NORMAL - No change"


if __name__ == "__main__":
    guard = BaselineGuard()

    activities = [10, 12, 14, 15, 30, 32]

    for activity in activities:
        result = guard.check(activity)
        print(
            f"Activity: {activity} | "
            f"Baseline: {guard.baseline:.2f} | "
            f"Result: {result}"
        )    
