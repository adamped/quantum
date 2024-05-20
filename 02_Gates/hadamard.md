# Hadamard Gate

The hadamard's gate (H-gate) primary function is to place a qubit into a superposition. It places the qubit into an equal 50/50 probability between |0⟩ and |1⟩.

When represented mathematically to a basis state |0⟩ you get

    H |0⟩ = 1/√2 (|0⟩ + |1⟩).

To expand on why 1/√2 is used lets look at the basis states as column vectors.

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

          
