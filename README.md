# devops1
This application simulates an AI-augmented Software Development Life Cycle (SDLC) with human-in-the-loop (HITL) checkpoints using a Streamlit UI. The process is divided into distinct workflow stages, each representing a real-world SDLC milestone.

Autogen vs. CrewAI – Final Decision Rationale
After evaluating both frameworks, we are in agreement to proceed with Autogen based on the following key considerations:

Linear Flow Execution

Autogen handles linear workflows efficiently (validated by Eshwar).

While CrewAI is designed around linear task orchestration, Autogen’s conversational flow has proven to be equally effective.

Iterative Flows Support

Autogen successfully supports iterative workflows (also tested by Eshwar).

CrewAI offers a dedicated Flow structure for iterative tasks, but Autogen’s flexibility achieves similar results without structural constraints.

Human-in-the-Loop (HITL) Integration

Autogen’s UserProxyAgent enables seamless HITL involvement.

CrewAI presents some challenges in implementing dynamic human intervention.

LangChain Integration

Integration effort with LangChain is comparable in both frameworks.

CrewAI has its own native toolkit for certain functionalities, but both can integrate with LangChain tools like Jira, Git, etc., with similar effort.

📝 To-Do Tasks
Figma Integration
Integrate with Figma API to generate wireframes based on system or user requirements.

System Architecture Diagram Generation
Use Claude or Draw.io API to auto-generate architecture diagrams from textual descriptions.

LangChain + Autogen Integration
Connect Autogen agents with LangChain-powered tools for:

Jira story creation

Git operations

Other DevOps/PM tools

HITL Implementation & UI Finalization
Implement Human-in-the-Loop via UserProxyAgent in Autogen, with Streamlit as the UI layer. Finalize the UI framework for the POC/demo.
