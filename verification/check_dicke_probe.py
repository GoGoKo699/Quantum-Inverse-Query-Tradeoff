#!/usr/bin/env python3
"""Check finite-dimensional Dicke-probe likelihoods and moment identities.

Run from the repository root:
    python verification/check_dicke_probe.py

Requires the versions pinned in requirements.txt. Successful completion writes
one JSON object to standard output and creates no files. These numerical checks
support selected algebraic identities; they do not prove the query theorem.
"""

import itertools
import json
import math
import platform

import numpy as np
import scipy
from scipy.linalg import expm


SEED = 20261022


def haar_unitary(d, rng):
    """Sample a complex Haar unitary using the QR phase convention."""
    q, r = np.linalg.qr(rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d)))
    diagonal = np.diag(r)
    return q * (diagonal / np.abs(diagonal))


def dicke_vector(blank, excitation, copies, weight):
    """Explicitly form the symmetric tensor state for small instances."""
    vector = np.zeros(len(blank) ** copies, dtype=complex)
    for occupied in itertools.combinations(range(copies), weight):
        occupied = set(occupied)
        term = np.array([1.0 + 0j])
        for position in range(copies):
            term = np.kron(term, excitation if position in occupied else blank)
        vector += term
    return vector / math.sqrt(math.comb(copies, weight))


def apply_tensor_power(unitary, vector, copies):
    d = unitary.shape[0]
    tensor = vector.reshape((d,) * copies)
    for axis in range(copies):
        tensor = np.moveaxis(np.tensordot(unitary, tensor, axes=(1, axis)), 0, axis)
    return tensor.reshape(-1)


def return_amplitude(forward, inverse, p):
    """The finite return-amplitude sum, including its continuous endpoints."""
    total = 0.0
    for k in range(min(inverse, forward - inverse) + 1):
        total += (
            (-1) ** k
            * math.comb(inverse, k)
            * math.comb(forward - inverse, k)
            * p ** k
            * (1 - p) ** ((forward - 2 * k) / 2)
        )
    return total


def count_amplitudes(forward, inverse, amplitude):
    """All beta_t coefficients of the normalized two-mode polynomial."""
    c = math.sqrt(max(0.0, 1 - abs(amplitude) ** 2))
    result = np.zeros(forward + 1, dtype=complex)
    for target_count in range(forward + 1):
        coefficient = 0.0j
        for u in range(max(0, target_count - inverse),
                       min(target_count, forward - inverse) + 1):
            coefficient += (
                math.comb(forward - inverse, u)
                * math.comb(inverse, target_count - u)
                * c ** (forward - inverse + target_count - 2 * u)
                * amplitude ** u
                * (-amplitude.conjugate()) ** (inverse - target_count + u)
            )
        result[target_count] = coefficient * math.sqrt(
            math.comb(forward, inverse) / math.comb(forward, target_count)
        )
    return result


def random_unitary_checks():
    rng = np.random.default_rng(SEED)
    maximum_norm_error = 0.0
    maximum_probability_error = 0.0
    maximum_count_distribution_error = 0.0
    maximum_likelihood_norm_error = 0.0
    count = 0
    for d in (3, 4):
        blank = np.eye(d, dtype=complex)[:, 0]
        target = np.eye(d, dtype=complex)[:, 1]
        for forward in range(2, 6):
            for trial in range(10):
                inverse = 1 + trial % min(2, forward - 1)
                unitary = haar_unitary(d, rng)
                amplitude = target.conj() @ unitary @ blank
                p = abs(amplitude) ** 2
                xi = (
                    unitary.conj().T @ target - amplitude.conjugate() * blank
                ) / math.sqrt(1 - p)
                vector = dicke_vector(blank, xi, forward, inverse)
                output = apply_tensor_power(unitary, vector, forward)
                digits = np.indices((d,) * forward).reshape(forward, -1)
                target_counts = np.count_nonzero(digits == 1, axis=0)
                probabilities = np.bincount(
                    target_counts, weights=np.abs(output) ** 2,
                    minlength=forward + 1,
                )
                predicted_probabilities = np.abs(
                    count_amplitudes(forward, inverse, amplitude)
                ) ** 2
                prediction = return_amplitude(forward, inverse, p) ** 2
                maximum_norm_error = max(
                    maximum_norm_error, abs(np.vdot(output, output).real - 1)
                )
                maximum_probability_error = max(
                    maximum_probability_error,
                    abs(float(probabilities[inverse]) - prediction),
                )
                maximum_count_distribution_error = max(
                    maximum_count_distribution_error,
                    float(np.max(np.abs(probabilities - predicted_probabilities))),
                )
                maximum_likelihood_norm_error = max(
                    maximum_likelihood_norm_error,
                    abs(float(np.sum(predicted_probabilities)) - 1),
                )
                count += 1
    return dict(
        cases=count,
        maximum_norm_error=float(maximum_norm_error),
        maximum_probability_error=float(maximum_probability_error),
        maximum_count_distribution_error=maximum_count_distribution_error,
        maximum_likelihood_norm_error=maximum_likelihood_norm_error,
    )


def endpoint_checks():
    """At p=0 the count is R; at p=1 the conditional count is F-R."""
    maximum_distribution_error = 0.0
    maximum_return_error = 0.0
    count = 0
    for forward in range(1, 16):
        for inverse in range(forward + 1):
            for p in (0.0, 1.0):
                probabilities = np.abs(
                    count_amplitudes(forward, inverse, complex(math.sqrt(p)))
                ) ** 2
                expected = np.zeros(forward + 1)
                expected[inverse if p == 0 else forward - inverse] = 1.0
                maximum_distribution_error = max(
                    maximum_distribution_error,
                    float(np.max(np.abs(probabilities - expected))),
                )
                maximum_return_error = max(
                    maximum_return_error,
                    abs(return_amplitude(forward, inverse, p) ** 2
                        - expected[inverse]),
                )
                # At p=1 and R>=1 the protocol accepts in reverse preparation;
                # the conditional count expression is used only as a limit.
                detection = 1 - (1 - p) ** inverse * expected[inverse]
                assert abs(detection - p) < 1e-12
                count += 1
    return dict(
        cases=count,
        maximum_distribution_error=maximum_distribution_error,
        maximum_return_error=float(maximum_return_error),
    )


def spin_checks():
    maximum_second_moment_error = 0.0
    maximum_fourth_formula_error = 0.0
    minimum_fourth_bound_slack = float("inf")
    minimum_exit_bound_slack = float("inf")
    count = 0
    for forward in range(2, 26):
        j = forward / 2
        mz = np.arange(forward + 1) - j
        raising = np.diag(
            np.sqrt((forward - np.arange(forward)) * (np.arange(forward) + 1)),
            -1,
        )
        jy = (raising - raising.T) / (2j)
        for inverse in range(1, forward // 2 + 1):
            m = inverse - j
            sensitivity = forward + 2 * inverse * (forward - inverse)
            low = min(0.5, 1 / sensitivity)
            for p in np.unique(np.r_[low, np.linspace(low, 0.5, 7)]):
                theta = math.asin(math.sqrt(p))
                output = expm(2j * theta * jy)[:, inverse]
                probabilities = np.abs(output) ** 2
                q = mz - m
                second = float(probabilities @ q ** 2)
                fourth = float(probabilities @ q ** 4)
                b = -2 * p * m
                c2 = 1 - 2 * p
                s2 = 2 * math.sqrt(p * (1 - p))
                a_up = (forward - inverse) * (inverse + 1)
                b_down = inverse * (forward - inverse + 1)
                a_next = (forward - inverse - 1) * (inverse + 2)
                b_next = (inverse - 1) * (forward - inverse + 2)
                second_formula = b * b + s2 * s2 * sensitivity / 4
                fourth_formula = (
                    second_formula ** 2
                    + s2 ** 2 / 4 * (
                        a_up * (2 * b + c2) ** 2
                        + b_down * (2 * b - c2) ** 2
                    )
                    + s2 ** 4 / 16 * (a_up * a_next + b_down * b_next)
                )
                maximum_second_moment_error = max(
                    maximum_second_moment_error, abs(second - second_formula)
                )
                maximum_fourth_formula_error = max(
                    maximum_fourth_formula_error, abs(fourth - fourth_formula)
                )
                minimum_fourth_bound_slack = min(
                    minimum_fourth_bound_slack,
                    5 * second_formula ** 2 + 2 * second_formula - fourth,
                )
                exit_probability = 1 - probabilities[inverse]
                minimum_exit_bound_slack = min(
                    minimum_exit_bound_slack,
                    exit_probability - second_formula / (5 * second_formula + 2),
                )
                assert fourth <= 5 * second_formula ** 2 + 2 * second_formula + 1e-7
                assert exit_probability + 1e-10 >= second_formula / (5 * second_formula + 2)
                assert exit_probability + 1e-10 >= 1 / 9
                count += 1
    return dict(
        cases=count,
        maximum_second_moment_error=float(maximum_second_moment_error),
        maximum_fourth_formula_error=float(maximum_fourth_formula_error),
        minimum_fourth_bound_slack=float(minimum_fourth_bound_slack),
        minimum_exit_bound_slack=float(minimum_exit_bound_slack),
    )


def main():
    result = dict(
        environment=dict(
            python=platform.python_version(), numpy=np.__version__,
            scipy=scipy.__version__, seed=SEED,
        ),
        random_unitaries=random_unitary_checks(),
        endpoints=endpoint_checks(),
        spin_moments=spin_checks(),
    )
    assert result["random_unitaries"]["maximum_norm_error"] < 1e-10
    assert result["random_unitaries"]["maximum_probability_error"] < 1e-10
    assert result["random_unitaries"]["maximum_count_distribution_error"] < 1e-10
    assert result["random_unitaries"]["maximum_likelihood_norm_error"] < 1e-10
    assert result["endpoints"]["maximum_distribution_error"] < 1e-12
    assert result["endpoints"]["maximum_return_error"] < 1e-12
    assert result["spin_moments"]["maximum_second_moment_error"] < 1e-9
    assert result["spin_moments"]["maximum_fourth_formula_error"] < 1e-7
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
