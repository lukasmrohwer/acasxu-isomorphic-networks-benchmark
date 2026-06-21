# creates a VNN-LIB 2.0 file (list of text lines) according to a fixed template:
# Arguments:
# - eps_in: allowed distance from original network's output
def vnnlib_template_2(eps_in):

    assert eps_in >= 0.0

    lines = []

    # intro comment
    lines.append("; Epsilion equivalence in simulated retrained networks:")
    lines.append("; a VNN-COMP benchmark with equivalent networks.")
    lines.append("; Author: Lukas Rohwer")
    lines.append("")

    # tell the verifier to use VNN-LIB 2.0
    lines.append("(vnnlib-version <2.0>)")
    lines.append("")

    # neural network declaration
    lines.append("(declare-network f")
    lines.append("    (declare-input X_f real [1, 1, 1, 5])")
    lines.append("    (declare-output Y_f real [1, 5])")
    lines.append(")")
    lines.append("(declare-network g")
    lines.append("    (isomorphic-to f)")
    lines.append("    (declare-input X_g real [1, 1, 1, 5])")
    lines.append("    (declare-output Y_g real [1, 5])")
    lines.append(")")
    lines.append("")

    # input constraints
    lines.append("; Input Constraints")
    lines.append("(assert (and (<= X_f[0,0,0,0] 0.679857769) (>= X_f[0,0,0,0] 0.6)))")
    lines.append("(assert (and (<= X_f[0,0,0,1] 0.5) (>= X_f[0,0,0,1] -0.5)))")
    lines.append("(assert (and (<= X_f[0,0,0,2] 0.5) (>= X_f[0,0,0,2] -0.5)))")
    lines.append("(assert (and (<= X_f[0,0,0,3] 0.5) (>= X_f[0,0,0,3] 0.45)))")
    lines.append("(assert (and (<= X_f[0,0,0,4] -0.45) (>= X_f[0,0,0,4] -0.5)))")
    lines.append("(assert (== X_f[0,0,0,0] X_g[0,0,0,0]))")
    lines.append("(assert (== X_f[0,0,0,1] X_g[0,0,0,1]))")
    lines.append("(assert (== X_f[0,0,0,2] X_g[0,0,0,2]))")
    lines.append("(assert (== X_f[0,0,0,3] X_g[0,0,0,3]))")
    lines.append("(assert (== X_f[0,0,0,4] X_g[0,0,0,4]))")
    lines.append("")

    # output constraints
    lines.append("; Output Constraints")
    lines.append("(assert (or")
    lines.append(f" (or (> Y_g[0,0] (+ Y_f[0,0] {eps_in})) (< Y_g[0,0] (- Y_f[0,0] {eps_in})))")
    lines.append(f" (or (> Y_g[0,1] (+ Y_f[0,1] {eps_in})) (< Y_g[0,1] (- Y_f[0,1] {eps_in})))")
    lines.append(f" (or (> Y_g[0,2] (+ Y_f[0,2] {eps_in})) (< Y_g[0,2] (- Y_f[0,2] {eps_in})))")
    lines.append(f" (or (> Y_g[0,3] (+ Y_f[0,3] {eps_in})) (< Y_g[0,3] (- Y_f[0,3] {eps_in})))")
    lines.append(f" (or (> Y_g[0,4] (+ Y_f[0,4] {eps_in})) (< Y_g[0,4] (- Y_f[0,4] {eps_in})))")
    lines.append("))")

    return lines