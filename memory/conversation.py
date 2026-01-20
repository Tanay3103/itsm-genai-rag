import json
import os
from datetime import datetime


class ConversationMemory:
    def __init__(self, session_id: str):
        self.support_state = None
        self.session_id = session_id
        self.file_path = f".memory/{session_id}.json"
        self.messages = []
        self.reset()

        self._load()

    def reset(self):
        self.support_state = {
            "mode": "NEW",
            "issue_summary": None,
            "questions": [],
            "answers": {},
            "solutions_tried": [],
            "current_solution": None,
            "last_updated": datetime.utcnow().isoformat(),
        }

    def add_user(self, text: str):
        self.messages.append({"role": "user", "content": text, "ts": datetime.utcnow().isoformat()})
        self._save()

    def add_ai(self, text: str):
        self.messages.append(
            {"role": "assistant", "content": text, "ts": datetime.utcnow().isoformat()}
        )
        self._save()

    def get(self):
        return self.messages

    # -------------------------
    # Persistence
    # -------------------------
    def _save(self):
        os.makedirs(".memory", exist_ok=True)
        with open(self.file_path, "w") as f:
            json.dump(
                {
                    "messages": self.messages,
                    "support_state": self.support_state,
                },
                f,
                indent=2,
            )

    def _load(self):
        if not os.path.exists(self.file_path):
            return

        with open(self.file_path, "r") as f:
            data = json.load(f)

        self.messages = data.get("messages", [])
        self.support_state = data.get("support_state", self.support_state)

    def update_state(self, **kwargs):
        self.support_state.update(kwargs)
        self._save()
