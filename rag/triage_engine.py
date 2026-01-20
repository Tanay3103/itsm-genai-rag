from config.config import OPENAI_MODEL

try:
    from langchain_core.messages import HumanMessage
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(model=OPENAI_MODEL, temperature=0)
except Exception:
    llm = None


def generate_followup_questions(issue_summary, known_context):
    if not llm:
        return ["Could you please share more details so I can help you better?"]

    prompt = f"""
You are an experienced IT L1/L2 support engineer.

User issue:
{issue_summary}

Known past context (may be empty):
{known_context}

Ask 2–3 concise, relevant follow-up questions
needed to diagnose the issue.
"""
    try:
        response = llm.invoke([HumanMessage(content=prompt)]).content
        return [q.strip("- ").strip() for q in response.split("\n") if q.strip()]
    except Exception:
        return ["Could you provide more details about the issue?"]
