memory = {
    100: 12,
    104: 8,
    108: 0
}

registers = {
    'R1': 0,
    'R2': 0,
    'R3': 0
}

def print_state(instruction):
    print(f"Executing: {instruction}")
    print(f"  Registers -> R1: {registers['R1']}, R2: {registers['R2']}, R3: {registers['R3']}")
    print(f"  Memory[108] -> {memory[108]}")
    print("-" * 40)

print("Initial State:")
print_state("None")
print("Starting Execution...\n")

instruction_a = "LOAD R1, 100"
registers['R1'] = memory[100]
print_state(instruction_a)

instruction_b = "LOAD R2, 104"
registers['R2'] = memory[104]
print_state(instruction_b)

instruction_c = "ADD R3, R1, R2"
registers['R3'] = registers['R1'] + registers['R2']
print_state(instruction_c)

instruction_d = "STORE R3, 108"
memory[108] = registers['R3']
print_state(instruction_d)

print("Execution Complete.")
print("\nFinal Results:")
print(f"Contents of R1: {registers['R1']}")
print(f"Contents of R2: {registers['R2']}")
print(f"Contents of R3: {registers['R3']}")
print(f"Final contents of memory location 108: {memory[108]}")
