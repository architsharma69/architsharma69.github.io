---
title: SimplifyNext Hackathon
role: Team Lead
period: 2026 July
summary: An Agentic AI hackathon, where my team designed a solution meant to tackle social welfare-related issues.
tags: [Python, Multi-Agent Systems, LLM Orchestration, FastAPI]
image: assets/simplify.png   # optional; delete this line for a card with no thumbnail
---

## Competition Description
The SimplifyNext Hackathon is a competition where participants solve real-world business challenges using cutting-edge AI, automation, and intelligent-agent technologies. Teams are required to design innovative solutions to genuine industry problems.

My group looked to address issues faced by startup founders. Founders want to focus on their ideas, not on mastering business admin — HR, finance, logistics, filling out forms, writing grant and loan applications, and navigating a different tech-savvy platform for each one. BRO is our hackathon entry: an assistant that takes on that peripheral work so founders don't have to.

The hackathon had elements of enterprising for social good. It has increased my motivation for entrepreneurship. 

## What we delivered
- An **Orchestrator** agent that classifies every incoming message as `clarify` (asks a follow-up), `direct` (answers small talk itself) or `delegate` (routes rephrased sub-questions to specialists, then synthesizes their responses — surfacing conflicts rather than silently picking a side).
- An **HR Manager** agent that places and reassigns tasks against a team roster, gated by a hard Python safety check rather than LLM judgment alone, and logs wellbeing events.
- A three-specialist **Document generation** team: a Statutory Compliance Specialist (Singapore ACRA incorporation filings), an Internal Financial Synthesizer (reviews a 3-year forecast computed deterministically in Python, not by the LLM), and a Grant & Capital Strategist (compiles Startup SG Founder / EDG grant packages).
- Two independent front ends — a Streamlit dashboard and a Telegram bot — both thin clients of the same FastAPI backend, with session state kept server-side so conversation history follows the user across either UI.

## What I did
- Led the team and owned the overall multi-agent architecture, including how the Orchestrator delegates to and synthesizes results from the HR and Document generation branches.
- Handled deployment and infrastructure for the project, including troubleshooting AWS account access issues during the competition window.
- Coordinated integration between the FastAPI backend and the two front ends (Streamlit + Telegram).
