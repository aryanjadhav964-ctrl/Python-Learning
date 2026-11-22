# Nested LLM API Response Extractor (Real-World AI Payload)
# When you send a prompt to an LLM API (like Gemini), it returns a deeply nested JSON structure converted into a Python dictionary.
api_response = {
    "model": "gemini-2.5-flash",
    "usage": {"prompt_tokens": 42, "completion_tokens": 18},
    "candidates": [
        {
            "index": 0,
            "content": {
                "role": "model",
                "parts": [
                    {"text": "Morning Hatha Yoga starts at 6:30 AM IST."}
                ]
            },
            "finish_reason": "STOP"
        }
    ]
}

# Your Task:

# Extract the exact AI reply text ("Morning Hatha Yoga starts at 6:30 AM IST.") into a variable named ai_reply.

# Calculate total_tokens by adding prompt_tokens and completion_tokens from the "usage" dictionary.

# Build a clean log dictionary named chat_log containing only "reply", "tokens_used", and "status" (mapped from "finish_reason").

# Print chat_log.

api_reply = api_response["candidates"][0]["content"]["parts"][0]
print(api_reply)

total_tokens = api_response["usage"]["prompt_tokens"] + api_response["usage"]["completion_tokens"]
print(total_tokens)

## building the clean chat-log dictionary 
chat_log = {
    "reply" : api_reply,
    "token_used": total_tokens,
    "stauts" : api_response["candidates"][0]["finish_reason"]
}
print(chat_log)