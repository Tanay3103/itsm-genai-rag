from rag.decision_router import decide_next_action
from rag.knowledge_retriever import search_knowledge
from rag.ticket_lookup import parse_ticket_content, search_tickets
from rag.triage_engine import generate_followup_questions
from ui.chat import bot_message


def handle_triage(user_query, memory):
    if memory.support_state["mode"] == "CONFIRM":
        return
    tickets = search_tickets(memory.support_state["issue_summary"] or user_query)
    kb = search_knowledge(memory.support_state["issue_summary"] or user_query)

    action = decide_next_action(tickets, kb, memory.support_state)

    if action == "ASK_MORE_QUESTIONS":
        questions = generate_followup_questions(
            memory.support_state["issue_summary"], [d.page_content for d, _ in tickets + kb]
        )
        memory.support_state["questions"] = questions
        q = questions[0]
        memory.add_ai(q)
        bot_message(q, kind="question")

    elif action in ["TRY_EXISTING_FIX", "TRY_KB_FIX"]:
        doc = (tickets or kb)[0][0].page_content
        parsed = parse_ticket_content(doc)

        resolution = parsed.get("resolution", "Please try the suggested steps")

        response = (
            "Based on similar issues, here’s what usually helps:\n\n"
            f"- **Recommended fix:** {parsed.get('resolution')}\n\n"
            "Please try this and let me know if it resolves the issue."
        )

        memory.support_state["solutions_tried"].append(parsed.get("resolution"))
        memory.update_state(current_solution=resolution, mode="CONFIRM")

        memory.add_ai(response)
        bot_message(response, kind="solution")
