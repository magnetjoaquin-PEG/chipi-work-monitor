class DocumentIntelligenceService:

    @staticmethod
    def analyze(content: str):

        actions = []
        risks = []

        text = content.lower()

        action_keywords = [
            "actualizar",
            "implementar",
            "revisar",
            "corregir",
            "completar",
            "desarrollar"
        ]

        risk_keywords = [
            "riesgo",
            "hallazgo",
            "incumplimiento",
            "desvío",
            "observación"
        ]

        for keyword in action_keywords:

            if keyword in text:

                actions.append({
                    "title": content[:100]
                })

                break

        for keyword in risk_keywords:

            if keyword in text:

                risks.append({
                    "title": content[:100]
                })

                break

        return {
            "actions_detected": actions,
            "risks_detected": risks
        }