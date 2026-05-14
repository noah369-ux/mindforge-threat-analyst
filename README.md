# MindForge Threat Analyst

A practical, open-source Threat Analyst Model developed through a full year of iterative, hands-on detection engineering.

## Core Pipeline
**Mindset → Behavioral Artifacts → Technical Signatures → Detection Engineering**

```mermaid
flowchart TD
    A[Mindset
Psychological Framework & Analyst Thinking] --> B[Behavioral Artifacts
Observable Actions & Patterns]
    B --> C[Technical Signatures
Concrete IOCs & Indicators]
    C --> D[Detection Engineering
Production Rules & Alerts]
    
    A -->|Desktop| E[Process Behavior
Persistence
Lateral Movement]
    A -->|Mobile| F[Permission Abuse
Runtime Behavior
Data Exfil]
    
    style A fill:#1e3a8a,stroke:#fff,color:#fff
```