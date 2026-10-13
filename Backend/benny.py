import httpx

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:3b"
SYSTEM_PROMPT = "You are Benny, a friendly private personal assistant. Keep answers short and clear."


def make_message(role: str, content: str) -> dict:
    return {"role": role, "content": content}


def build_messages(system_prompt: str, user_message: str) -> list:
    return [
        make_message("system", system_prompt),
        make_message("user", user_message),
    ]


def ask_benny(user_message: str) -> str:
    payload = {
        "model": MODEL,
        "messages": build_messages(SYSTEM_PROMPT, user_message),
        "stream": False,
    }

    response = httpx.post(OLLAMA_URL, json=payload, timeout=120)
    response.raise_for_status()

    data = response.json()
    return data["message"]["content"]


reply = ask_benny("Hi, who are you?")
print(reply)