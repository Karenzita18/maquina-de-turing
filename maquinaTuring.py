class TuringMachine:
    def __init__(self):
        self.transitions = {}
        self.current_state = "q0"

    def add_transition(self, current_state, read_symbol, new_state, write_symbol, direction):
        self.transitions[(current_state, read_symbol)] = (new_state, write_symbol, direction)

    def execute(self, input_word):
        tape = list(input_word)
        head_position = 0

        while True:
            current_symbol = tape[head_position]

            if (self.current_state, current_symbol) not in self.transitions:
                break

            new_state, write_symbol, direction = self.transitions[(self.current_state, current_symbol)]
            self.current_state = new_state
            tape[head_position] = write_symbol

            if direction == Direction.RIGHT:
                head_position += 1
                if head_position == len(tape):
                    tape.append('B')
            elif direction == Direction.LEFT:
                head_position -= 1
                if head_position < 0:
                    tape.insert(0, 'B')
                    head_position = 0

        return self.current_state == "q2" 


class Direction:
    LEFT = 'Left'
    RIGHT = 'Right'
    STAY = 'Stay'


if __name__ == "__main__":
    tm = TuringMachine()

    tm.add_transition("q0", '0', "q1", '1', Direction.RIGHT)
    tm.add_transition("q0", '1', "q1", 'B', Direction.RIGHT)
    tm.add_transition("q1", '1', "q0", '0', Direction.LEFT)
    tm.add_transition("q1", 'B', "q2", 'B', Direction.STAY)

    input_word = "0B"

    accepted = tm.execute(input_word)

    if accepted:
        print("Palavra aceita pela Máquina de Turing!")
    else:
        print("Palavra rejeitada pela Máquina de Turing!")