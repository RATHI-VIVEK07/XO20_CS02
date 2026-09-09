class TrustEngine:

    def _init_(self):
        self.trust_score = 100

    def evaluate(self, result):
        if result.startswith("NORMAL"):
            self.trust_score = min(100, self.trust_score + 2)

        elif result.startswith("LEGITIMATE"):
            self.trust_score = min(100, self.trust_score + 1)

        elif result.startswith("SUSPICIOUS"):
            self.trust_score = max(0, self.trust_score - 20)

        if self.trust_score >= 80:
            risk = "LOW"
        elif self.trust_score >= 50:
            risk = "MEDIUM"
        else:
            risk = "HIGH"

        return self.trust_score, risk