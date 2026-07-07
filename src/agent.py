class WaterIntakeAgent:
    def __init__(self):
        self.history = []

    def analyze_intake(self, intake_ml):
        if intake_ml < 1000:
            return "Your hydration is low. Drink more water immediately."
        elif intake_ml < 2000:
            return "Your hydration is moderate. Drink some more water."
        else:
            return "Your hydration level is good. Keep it up."

if __name__ == "__main__":
    agent = WaterIntakeAgent()
    feedback = agent.analyze_intake(1500)
    print("Hydration Analysis:", feedback)