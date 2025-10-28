# Quantum Random Number Generator

This project uses Qiskit, IBM's open-source quantum computing framework, to show how to create truly random numbers using the concepts of quantum physics.

 This method uses quantum superposition and measurement to create unpredictable and impartial random bits, in contrast to traditional pseudo-random number generators that depend on deterministic algorithms.

 The main concept is straightforward but effective:

 1. A Hadamard gate (H) is used to superimpose each qubit, resulting in an equal chance of measuring 0 or 1.

 2. Each qubit randomly collapses to one of these states when measured.

 3. This procedure is repeated for several qubits, producing a random bitstring that is subsequently translated into a decimal integer.

