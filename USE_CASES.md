
# ITSM GenAI Copilot – Use Cases

## UC1: Similar Ticket Search (Known Issue)
User reports an issue. System finds high-similarity historical ticket and provides:
- Root cause
- Resolution steps
- Confidence score

## UC2: Knowledge-Based Resolution
If no ticket is found, system searches internal knowledge (PDF):
- Provides best-known guidance
- Medium confidence score

## UC3: New Issue Investigation
If not found in tickets or knowledge:
- Bot asks follow-up questions
- Attempts AI-based troubleshooting

## UC4: Auto Ticket Creation
If unresolved:
- Jira / ServiceNow ticket created
- Full context included
- Ticket auto-ingested into vector DB

## UC5: Continuous Learning
Newly created or resolved tickets are embedded and stored so future occurrences
are automatically detected and resolved.

## UC6: Intent-Aware Routing
System classifies intent (known issue, how-to, investigation, status)
and responds appropriately.
