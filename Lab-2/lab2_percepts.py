class ClassroomAgent:
    """Simple reflex agent for the simulated classroom environment."""
    def act(self, temp, occupied):
        if not occupied:
            return "ECO"
        if temp > 26:
            return "COOL"
        if temp < 20:
            return "WARM"
        return "IDLE"


if __name__ == "__main__":
    agent = ClassroomAgent()
    for percept in [(29, True), (24, True), (29, False)]:
        print(percept, agent.act(*percept))
