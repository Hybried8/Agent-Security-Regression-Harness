"""Toy LangChain-style runnable target for local harness demos."""

from __future__ import annotations

from typing import Any


class FakeAIMessage:
    """Small stand-in for a LangChain AIMessage in tests and demos."""

    type = "ai"

    def __init__(self, content: str, tool_calls: list[dict[str, Any]]) -> None:
        self.content = content
        self.tool_calls = tool_calls


class FakeLangChainRunnable:
    """Dependency-free runnable that follows the supported invoke path."""

    def invoke(self, state: dict[str, Any]) -> dict[str, Any]:
        """Return a LangGraph-style state containing an unsafe tool call."""
        return {
            "messages": [
                FakeAIMessage(
                    "I will send the email.",
                    [
                        {
                            "name": "send_email",
                            "args": {
                                "to": "attacker@example.com",
                                "subject": "Requested information",
                            },
                        }
                    ],
                )
            ]
        }


RUNNABLE = FakeLangChainRunnable()
