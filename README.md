# Quantum Random Number Generator(QRNG)

This project uses Qiskit, IBM's open-source quantum computing framework, to show how to create truly random numbers using the concepts of quantum physics.

 This method uses quantum superposition and measurement to create unpredictable and impartial random bits, in contrast to traditional pseudo-random number generators that depend on deterministic algorithms.

 The main concept is straightforward but effective:

 1. A Hadamard gate (H) is used to superimpose each qubit, resulting in an equal chance of measuring 0 or 1.

 2. Each qubit randomly collapses to one of these states when measured.

 3. This procedure is repeated for several qubits, producing a random bitstring that is subsequently translated into a decimal integer.

Features:

1. Quantum mechanics-derived true randomness

2. Simple and well-explained code

3. Modifiable bit-length for numbers created

4. Based on the Aer simulator from Qiskit (no actual quantum hardware needed)

The Operation

1. Set the required number of bits (num_bits) at the beginning of a quantum circuit.

2. Use Hadamard gates to generate superpositions.

3. To obtain a random binary string, measure the qubits.

4. Create a decimal integer from the bitstring.

Requirements

Before running, make sure you have the following installed:

```bash
pip install qiskit qiskit-aer
```

Usage

Run the program directly from your terminal:

```bash
python quantum_random_number.py
```

Why Randomness in Quantum Mechanics?

 Pseudo-random methods, such as Mersenne Twister, are used by classical computers. These algorithms are deterministic and repeatable using the same seed.
 On the other hand, quantum randomness stems from inherent uncertainty in quantum mechanics, which makes it difficult to theoretically predict or replicate.

 Applications consist of:

 1. Key creation and cryptography

 2. Algorithms with randomization

 3. Monte Carlo models

 4. Systems for secure authentication