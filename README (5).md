# Adaptive Behavioural Trust for Non-Human Identities

## PS02 --- Cybersecurity Hackathon

### Project Title

**Adaptive Behavioural Trust Engine for Non-Human Identities (NHI)**

### Tagline

> **Don't trust the identity. Trust its behaviour.**

------------------------------------------------------------------------

## 1. Problem Statement

Modern software systems depend on many **Non-Human Identities (NHIs)**
such as service accounts, application identities, workload identities,
API credentials, automation accounts, bots, and AI agents.

These identities continuously access databases, APIs, repositories,
storage services, and other resources.

The main security challenge is that:

-   Legitimate software or workload changes can cause an NHI to change
    its behaviour.
-   A compromised NHI can continue using valid credentials.
-   Attackers can introduce small changes gradually to avoid detection.
-   Blindly accepting new behaviour can allow malicious activity to
    become part of the trusted baseline.

Therefore, the system must continuously learn individual NHI behaviour
while distinguishing **legitimate workload evolution from potentially
compromised behaviour**.

------------------------------------------------------------------------

## 2. Proposed Solution

We propose a **real-time adaptive behavioural trust system** that
creates and maintains a separate behavioural profile for every NHI.

The system continuously monitors activity, compares current behaviour
with the identity's historical profile, calculates a dynamic trust/risk
score, and classifies the identity into one of four states:

-   🟢 **NORMAL**
-   🟡 **DRIFTING**
-   🟠 **SUSPICIOUS**
-   🔴 **HIGH-RISK**

The system also contains a **protected adaptation mechanism**. New
behaviour is not automatically added to the trusted baseline. Only
sufficiently trusted and consistent changes are allowed to influence
future learning.

------------------------------------------------------------------------

## 3. Key Idea

``` text
Activity Stream
      ↓
Individual Behaviour Profile
      ↓
Behaviour Analysis
      ↓
Risk / Trust Calculation
      ↓
NORMAL / DRIFTING / SUSPICIOUS / HIGH-RISK
      ↓
Adaptive Response
      ↓
Allow / Monitor / Restrict / Block
      ↓
Protected Baseline Update
```

------------------------------------------------------------------------

## 4. Core Features

### 4.1 Individual Behavioural Profiles

Each NHI has its own profile instead of using one global definition of
normal behaviour.

Example:

``` text
Identity: PaymentBot

Typical request rate: 100–150/hour
Typical resource: Payment Database
Typical time: Business hours
Typical source: Known application environment
```

------------------------------------------------------------------------

### 4.2 Continuous Monitoring

The system processes a continuous stream of simulated/sandboxed activity
instead of depending only on a completed offline dataset.

Monitored behavioural features can include:

-   Request frequency
-   Access time
-   Resource accessed
-   Action type
-   Data volume
-   Source/environment
-   Event sequences
-   Frequency changes over time

------------------------------------------------------------------------

### 4.3 Four Operational States

  -----------------------------------------------------------------------
  State                   Meaning                 Example Response
  ----------------------- ----------------------- -----------------------
  NORMAL                  Behaviour matches the   Allow
                          established profile     

  DRIFTING                Behaviour changed but   Monitor and evaluate
                          may represent           
                          legitimate evolution    

  SUSPICIOUS              Behaviour has           Restrict / monitor
                          meaningful risk         
                          indicators              

  HIGH-RISK               Strong evidence of      Block and alert
                          compromise              
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 5. Adaptive Trust Model

The trust score changes according to current behaviour.

Example:

``` text
Known resource              → Positive evidence
Expected timing             → Positive evidence
Stable request pattern      → Positive evidence

Unknown resource            → Negative evidence
Unusual timing              → Negative evidence
Sudden request spike        → Strong negative evidence
Sensitive resource access   → Strong negative evidence
Suspicious sequence         → Strong negative evidence
```

A possible prototype interpretation:

``` text
80–100  → NORMAL
50–79   → DRIFTING
20–49   → SUSPICIOUS
0–19    → HIGH-RISK
```

The exact thresholds can be tuned during evaluation.

------------------------------------------------------------------------

## 6. Protected Adaptation

Adaptation is a major part of the solution.

A new behaviour should **not automatically become the new normal**.

### Learning Gate

``` text
New Behaviour
      ↓
Evaluate Evidence
      ↓
Is the change sufficiently trusted?
      ↓
   ┌──┴──┐
  YES    NO
   ↓      ↓
Adapt   Do not
Profile  learn yet
   ↓      ↓
Update  Continue
Baseline Monitoring
```

This prevents suspicious activity from immediately contaminating the
trusted profile.

------------------------------------------------------------------------

## 7. Baseline-Poisoning Protection

The system is designed to handle an attacker who gradually changes
behaviour.

Example:

``` text
Normal → Small deviation → Small deviation
       → Larger deviation → Suspicious activity
```

A naive adaptive system may learn these changes and eventually consider
malicious behaviour normal.

Our system instead uses:

-   Confidence/evidence checks
-   Risk-aware learning
-   Delayed adaptation
-   Suspicious-change exclusion
-   Continuous monitoring

Therefore, **suspicious behaviour is not blindly incorporated into the
baseline**.

------------------------------------------------------------------------

## 8. Legitimate Drift Handling

Not every behavioural change is an attack.

For example, an organization may introduce:

-   A new service dependency
-   A new API
-   Increased workload
-   A new resource
-   A software architecture change

The system should detect the change as **DRIFTING**, monitor it, and
allow sufficiently trusted and consistent changes to influence the
future profile.

This avoids treating every new behaviour as malicious.

------------------------------------------------------------------------

## 9. Multiple NHI Support

The system maintains independent behavioural context for multiple
identities operating concurrently.

Example:

``` text
PaymentBot
BackupService
AI-Agent
IoT-Service
API-Service
```

Each identity has its own:

-   Behaviour profile
-   Trust score
-   Current state
-   History
-   Adaptation decisions

------------------------------------------------------------------------

## 10. Live Demonstration Scenarios

### Scenario A --- Stable Behaviour

``` text
PaymentBot
↓
Expected resource
↓
Expected request rate
↓
Expected timing
↓
NORMAL
↓
Access Allowed
```

### Scenario B --- Legitimate Workload Evolution

``` text
PaymentBot
↓
New service dependency
↓
Behaviour changes
↓
Evidence collected
↓
DRIFTING
↓
Trusted change confirmed
↓
Profile gradually adapted
```

### Scenario C --- Sudden Suspicious Behaviour

``` text
PaymentBot
↓
Unknown source
↓
Request spike
↓
Sensitive resource
↓
Unusual timing
↓
SUSPICIOUS / HIGH-RISK
↓
Access Restricted / Blocked
```

### Scenario D --- Gradual Baseline-Poisoning Attempt

``` text
Small change
      ↓
Small change
      ↓
Small change
      ↓
Risk accumulates
      ↓
Learning Gate rejects suspicious change
      ↓
Baseline remains protected
```

------------------------------------------------------------------------

## 11. Human-Readable Explanations

The system should explain important decisions.

Example:

``` text
Identity: PaymentBot
State: HIGH-RISK
Trust Score: 18

Reasons:
- Request frequency increased significantly
- Access occurred outside the normal time window
- New sensitive resource was accessed
- Behaviour differs from the established profile

Adaptation Decision:
Baseline NOT updated because risk evidence is insufficient for trusted learning.

Action:
ACCESS RESTRICTED
```

This makes the system easier for security teams and hackathon judges to
understand.

------------------------------------------------------------------------

## 12. Proposed Architecture

``` text
              ┌─────────────────────┐
              │ Simulated NHI Events│
              └──────────┬──────────┘
                         ↓
              ┌─────────────────────┐
              │ Streaming Monitor   │
              └──────────┬──────────┘
                         ↓
              ┌─────────────────────┐
              │ Identity Profiles   │
              └──────────┬──────────┘
                         ↓
              ┌─────────────────────┐
              │ Behaviour Analyzer  │
              └──────────┬──────────┘
                         ↓
              ┌─────────────────────┐
              │ Trust / Risk Engine │
              └──────────┬──────────┘
                         ↓
       ┌─────────────────┼─────────────────┐
       ↓                 ↓                 ↓
    State Engine     Learning Gate     Explanation
       ↓                 ↓
       └──────────┬──────┘
                  ↓
          Adaptive Response
                  ↓
       Allow / Monitor / Restrict / Block
                  ↓
          Protected Baseline
```

------------------------------------------------------------------------

## 13. Technology Stack

### Frontend

-   HTML
-   CSS
-   JavaScript

### Backend

-   Python
-   Flask

### Data Storage

-   SQLite / CSV for prototype data

### Behaviour Analysis

-   Statistical anomaly detection
-   Rule-based risk scoring
-   Optional lightweight machine learning

### Visualization

-   Dashboard
-   Trust score
-   Behaviour trends
-   Alerts
-   Event stream

The solution is designed to run on a normal development machine without
enterprise SIEM/EDR infrastructure.

------------------------------------------------------------------------

## 14. Why This Approach?

Traditional identity-based access asks:

> **"Is this identity valid?"**

Our approach additionally asks:

> **"Is this identity behaving normally right now?"**

This enables continuous, context-aware trust rather than permanent trust
based only on valid credentials.

------------------------------------------------------------------------

## 15. Evaluation

The system should be evaluated using more than detection accuracy.

Key metrics:

-   False-positive rate
-   Detection responsiveness
-   Legitimate-drift handling
-   Adaptation behaviour
-   Baseline-poisoning resistance
-   Processing latency
-   Resource usage

We will test:

1.  Stable behaviour
2.  Legitimate workload evolution
3.  Sudden suspicious behaviour
4.  Gradual suspicious behaviour
5.  Adaptive baseline-poisoning attempts
6.  Multiple concurrent identities

------------------------------------------------------------------------

## 16. Security Model

### Protected Assets

-   NHI behavioural profiles
-   Trust decisions
-   Access decisions
-   Simulated resources

### Threats

-   Compromised valid credentials
-   Sudden anomalous activity
-   Slow behavioural manipulation
-   Baseline poisoning
-   Suspicious resource access

### Security Goal

Detect meaningful behavioural changes while avoiding both:

-   **Overreaction to legitimate changes**
-   **Over-adaptation to malicious changes**

------------------------------------------------------------------------

## 17. Expected Outcome

The final prototype will provide a continuously running behavioural
trust layer that:

-   Maintains individual NHI profiles
-   Monitors behaviour continuously
-   Detects sudden and gradual deviations
-   Distinguishes drift from suspicious behaviour
-   Protects the baseline from poisoning
-   Adapts trusted profiles incrementally
-   Provides explainable decisions
-   Supports multiple identities
-   Runs on ordinary development hardware

------------------------------------------------------------------------

## 18. Project USP

> ### **Adaptive Trust, Not Static Trust**
>
> We don't permanently trust an NHI just because its credentials are
> valid. We continuously evaluate **behaviour**, protect the learning
> baseline, and adapt trust as the workload evolves.

------------------------------------------------------------------------

## 19. Team

**Team Size:** 3 Members

-   Member 1 --- Behavioural Trust & Backend
-   Member 2 --- Dashboard & Frontend
-   Member 3 --- Integration, Evaluation & Presentation

------------------------------------------------------------------------

## 20. One-Line Pitch

> **"Our system continuously learns what normal behaviour looks like for
> every non-human identity, detects both sudden and gradual deviations,
> protects the baseline from poisoning, and dynamically adapts trust
> before compromised behaviour becomes the new normal."**
