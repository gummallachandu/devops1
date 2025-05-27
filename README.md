# devops1
This application simulates an AI-augmented Software Development Life Cycle (SDLC) with human-in-the-loop (HITL) checkpoints using a Streamlit UI. The process is divided into distinct workflow stages, each representing a real-world SDLC milestone.

👥 User Roles
Business User
Uploads requirement documents and initiates the SDLC process.

Tech Reviewer (HITL)
Reviews the outcomes of each stage — user stories, architecture, code — and approves or rejects with feedback.

UI Layout
Main Panel (Center): Displays current workflow screen based on the user's role.

Right Panel: Tracks SDLC workflow progress with stage status indicators:

⏳ In Progress

🕓 Ready to Review

✅ Completed

❌ Rejected

Left Sidebar:

Role toggle

Chat assistant (mock query to AI agent)
