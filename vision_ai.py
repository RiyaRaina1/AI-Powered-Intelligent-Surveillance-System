from typing import Any


class VisionAI:
    def summarize(self, people: int, known_faces: int, unknown_faces: int, objects: list[str], threat_score: int) -> dict[str, Any]:
        object_list = ", ".join(sorted(set(objects))) if objects else "none"
        risk_label = "low"
        if threat_score >= 75:
            risk_label = "high"
        elif threat_score >= 45:
            risk_label = "medium"

        return {
            "summary": (
                f"Detected {people} people, {known_faces} known visitor(s), "
                f"{unknown_faces} unknown visitor(s), and objects: {object_list}."
            ),
            "risk_level": risk_label,
            "threat_score": threat_score,
            "recommendation": (
                "Review suspicious unknown visitors and ensure critical areas are secured."
                if threat_score >= 45
                else "Normal activity detected. Continue monitoring."
            ),
        }
