# Rotation Gates

Rotataion gates will rotate a qubit around the axes of the Bloch Sphere. The three gates Rx, Ry and Rz will rotate respectively around each axis.

Rz gate is similar to the S and T Phase Shift gates but allows you to set an arbitrary angle to shift the phase.

Each gate can be represented by a unitary matrix, by replacing the θ with the appropriate angle you want to rotate.

## Rx(θ) Gate

    |cos(θ/2), -i(sin(θ/2))|
    |-i(sin(θ/2)), cos(θ/2)|

## Ry(θ) Gate

    |cos(θ/2), -sin(θ/2)|
    |sin(θ/2), cos(θ/2)|

## Rz(θ) Gate

    |exp(-iθ/2), 0|
    |0, exp(iθ/2)|

While Rz is similar to S and T gates, Rz gates can also introduce amplitude changes along with phase changes, unlike S and T gates that only produce a phase change.
