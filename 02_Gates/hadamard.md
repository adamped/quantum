# Hadamard Gate

The hadamard's gate (H-gate) primary function is to place a qubit into a superposition. It places the qubit into an equal 50/50 probability between |0⟩ and |1⟩.

When represented mathematically to a basis state |0⟩ you get

    H |0⟩ = 1/√2 (|0⟩ + |1⟩).

To expand on why 1/√2 is used, lets look at the basis states as column vectors.

    |0⟩ = | 1 |
          | 0 |

    |1⟩ = | 0 |
          | 1 |


This is the Hadamard gate represented as a matrix

    H = 1/√2 * | 1  1 |
               | 1 -1 |

Now we do matrix multiplication, in this example with |0⟩

    H |0⟩ = (1/√2) * | 1  1 | * | 1 | 
                     | 1 -1 |   | 0 |            

          = (1/√2) * | 1*1 + 1*0 | 
                     | 1*1 - 1*0 |            

          = (1/√2) * | 1 |
                     | 1 |

The Hadamard gate is reverisble, meaning if you apply it twice to the same qubit you end up in the same state.

## Born Rule

The Born rule is the reason for 1/√2. In quantum mechanics we need a system to interpret a wave function of a quantum system into a definite result. The Born rule states that the probability of obtaining a particular measurement is equal to the square of the absolute value of the probability amplitude.

    Probability of outcome = amplitude²

Hence if the amplitude is 1/√2

    (1/√2)² = 1/2 = 50%

And this allows us to arrive at the 50% probability of collapsing into either |0⟩ or |1⟩.