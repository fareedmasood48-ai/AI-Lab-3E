class StatefulClassroomAgent:
    """Avoid sending repeated identical mode commands; no hardware is controlled."""
    def __init__(self):
        self.previous_mode = None

    def act(self, temp, occupied):
        if not occupied:
            target = "ECO"
        elif temp > 26:
            target = "COOL"
        elif temp < 20:
            target = "WARM"
        else:
            target = "IDLE"

        send_command = target != self.previous_mode
        previous_mode = self.previous_mode
        self.previous_mode = target
        return previous_mode, target, send_command


if __name__ == "__main__":
    agent = StatefulClassroomAgent()
    percepts = [(29, True), (29, True), (20, True), (26, True),
                (19, True), (29, False), (29, False), (24, True)]
    print("step | previous | percept | target | command")
    for step, percept in enumerate(percepts, 1):
        previous, target, send = agent.act(*percept)
        print(f"{step:>4} | {str(previous):>8} | {str(percept):>13} | "
              f"{target:>6} | {'SEND' if send else 'NO SEND'}")
