from lab2_model import StatefulClassroomAgent

def run_checks():
    agent = StatefulClassroomAgent()
    cases = [
        ((29, True), None, "COOL", True),   # initial command
        ((29, True), "COOL", "COOL", False),# repeated percept/mode
        ((20, True), "COOL", "IDLE", True), # exact lower boundary
        ((26, True), "IDLE", "IDLE", False),# exact upper boundary
        ((19, True), "IDLE", "WARM", True), # transition
        ((29, False), "WARM", "ECO", True), # empty-room priority
        ((29, False), "ECO", "ECO", False) # repeated empty-room mode
    ]
    for i, (percept, expected_previous, expected_target, expected_send) in enumerate(cases, 1):
        previous, target, send = agent.act(*percept)
        assert previous == expected_previous, (i, previous, expected_previous)
        assert target == expected_target, (i, target, expected_target)
        assert send == expected_send, (i, send, expected_send)
        print(f"PASS {i}: prev={previous}, percept={percept}, target={target}, "
              f"command={'SEND' if send else 'NO SEND'}")
    print("All checks passed.")

if __name__ == "__main__":
    run_checks()
