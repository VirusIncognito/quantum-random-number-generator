from qiskit import QuantumCircuit
from qiskit_aer import QasmSimulator

def generate_random_number(num_bits):
    '''
    The idea is to generate a random number using quantum superposition.
    We achieve this by taking input of the number of bits required for the random number.
    After that, we create a quantum circuit with the specified number of qubits, and then
    we apply Hadamard gates to each qubit to create a superposition of |0> and |1> states.
    Finally, we measure each of the qubits to collapse the superposition into a definite state,
    which gives us a random bitstring. This bitstring is then converted to its decimal equivalent
    to obtain the random number.
    
    An advantage of this method is that it leverages the inherent randomness of quantum mechanics,
    making it more unpredictable compared to classical pseudo-random number generators.

    Args:
        num_bits (int): Number of bits for the random number.

    Returns:
        tuple: A tuple containing the random bitstring and its decimal equivalent.

    Time Complexity:
        O(n), where n is the number of bits.
    Space Complexity:
        O(1), as we are using a fixed amount of space regardless of input size.
    '''
    bitstring = ''
    simulator = QasmSimulator()
    for _ in range(num_bits):
        qc = QuantumCircuit(1, 1)
        qc.h(0)
        qc.measure(0, 0)
        result = simulator.run(qc, shots=1).result()
        counts = result.get_counts()
        bit = list(counts.keys())[0]
        bitstring += bit
    random_number = int(bitstring, 2)
    return bitstring, random_number

if __name__ == "__main__":
    num_bits = 16  # You can change this value to generate random numbers of different bit lengths
    bitstring, random_number = generate_random_number(num_bits)
    print(f"Generated random bitstring: {bitstring}")
    print(f"Generated random number: {random_number}")
