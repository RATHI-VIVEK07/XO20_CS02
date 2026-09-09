class TrustEngine:

    def __init__(self):
        self.trust_scores = {}

    def evaluate(self, identity, result):
        if identity not in self.trust_scores:
            self.trust_scores[identity] = 100

        score = self.trust_scores[identity]

        if result.startswith("NORMAL"):
            score = min(100, score + 2)

        elif result.startswith("LEGITIMATE"):
            score = min(100, score + 1)

        elif result.startswith("SUSPICIOUS"):
            score = max(0, score - 20)

        self.trust_scores[identity] = score

        if score >= 80:
            risk = "LOW"
        elif score >= 50:
            risk = "MEDIUM"
        else:
            risk = "HIGH"

        return score, risk
