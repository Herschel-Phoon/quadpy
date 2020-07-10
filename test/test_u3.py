import numpy
import orthopy
import pytest
from helpers import check_degree_ortho
from matplotlib import pyplot as plt

import quadpy

# Note
# ====
# Instead of testing exact integration against of all monomials of degree at most l, one
# can instead test exact integration of all _spherical harmonics_ of degree at most l.
# While there are 2**l monomials, there are only l**2 spherical harmonics.


@pytest.mark.parametrize(
    "scheme", [quadpy.u3.lebedev_003a(), quadpy.u3.stroud_u3_14_1()]
)
def test_spherical_harmonic(scheme):
    """Assert the norm of the spherical harmonic

    Y_1^1(phi, theta) = -1/2 sqrt(3/2/pi) * exp(i*phi) * sin(theta)

    is indeed 1, i.e.,

    int_0^2pi int_0^pi
        Y_1^1(phi, theta) * conj(Y_1^1(phi, theta)) * sin(theta)
        dphi dtheta = 1.
    """

    def spherical_harmonic_11(azimuthal, polar):
        # y00 = 1.0 / numpy.sqrt(4*numpy.pi)
        y11 = (
            -0.5
            * numpy.sqrt(3.0 / 2.0 / numpy.pi)
            * numpy.exp(1j * azimuthal)
            * numpy.sin(polar)
        )
        return y11 * numpy.conjugate(y11)

    val = scheme.integrate_spherical(spherical_harmonic_11)

    assert abs(val - 1.0) < 1.0e-14


@pytest.mark.parametrize(
    "scheme,tol",
    [
        (quadpy.u3.bazant_oh_09(), 1.0e-10),
        (quadpy.u3.bazant_oh_11(), 1.0e-10),
        (quadpy.u3.bazant_oh_13(), 1.0e-10),
    ]
    + [
        (quadpy.u3.heo_xu_13(), 1.0e-14),
        (quadpy.u3.heo_xu_15(), 1.0e-14),
        (quadpy.u3.heo_xu_17(), 1.0e-13),
        (quadpy.u3.heo_xu_19_1(), 1.0e-13),
        (quadpy.u3.heo_xu_19_2(), 1.0e-12),
        (quadpy.u3.heo_xu_21_1(), 1.0e-9),
        (quadpy.u3.heo_xu_21_2(), 1.0e-9),
        (quadpy.u3.heo_xu_21_3(), 1.0e-9),
        (quadpy.u3.heo_xu_21_4(), 1.0e-9),
        (quadpy.u3.heo_xu_21_5(), 1.0e-9),
        (quadpy.u3.heo_xu_21_6(), 1.0e-9),
        (quadpy.u3.heo_xu_23_1(), 1.0e-9),
        (quadpy.u3.heo_xu_23_2(), 1.0e-9),
        (quadpy.u3.heo_xu_23_3(), 1.0e-9),
        (quadpy.u3.heo_xu_25_1(), 1.0e-9),
        (quadpy.u3.heo_xu_25_2(), 1.0e-9),
        (quadpy.u3.heo_xu_27_1(), 1.0e-9),
        (quadpy.u3.heo_xu_27_2(), 1.0e-9),
        (quadpy.u3.heo_xu_27_3(), 1.0e-9),
        (quadpy.u3.heo_xu_29(), 1.0e-9),
        (quadpy.u3.heo_xu_31(), 1.0e-9),
        (quadpy.u3.heo_xu_33(), 1.0e-9),
        (quadpy.u3.heo_xu_35(), 1.0e-8),
        (quadpy.u3.heo_xu_37(), 1.0e-9),
        (quadpy.u3.heo_xu_39_1(), 1.0e-6),
        (quadpy.u3.heo_xu_39_2(), 1.0e-8),
    ]
    + [
        (quadpy.u3.fliege_maier_04(), 1.0e-6),
        (quadpy.u3.fliege_maier_09(), 1.0e-6),
        (quadpy.u3.fliege_maier_16(), 1.0e-6),
        (quadpy.u3.fliege_maier_25(), 1.0e-6),
    ]
    + [
        (quadpy.u3.lebedev_003a(), 1.0e-11),
        (quadpy.u3.lebedev_003b(), 1.0e-11),
        (quadpy.u3.lebedev_003c(), 1.0e-11),
        (quadpy.u3.lebedev_005(), 1.0e-11),
        (quadpy.u3.lebedev_007(), 1.0e-11),
        (quadpy.u3.lebedev_009(), 1.0e-11),
        (quadpy.u3.lebedev_011(), 1.0e-11),
        (quadpy.u3.lebedev_013(), 1.0e-11),
        (quadpy.u3.lebedev_015(), 1.0e-11),
        (quadpy.u3.lebedev_017(), 1.0e-11),
        (quadpy.u3.lebedev_019(), 1.0e-11),
        (quadpy.u3.lebedev_021(), 1.0e-11),
        (quadpy.u3.lebedev_023(), 1.0e-11),
        (quadpy.u3.lebedev_025(), 1.0e-11),
        (quadpy.u3.lebedev_027(), 1.0e-11),
        (quadpy.u3.lebedev_029(), 1.0e-11),
        (quadpy.u3.lebedev_031(), 1.0e-11),
        (quadpy.u3.lebedev_035(), 1.0e-11),
        (quadpy.u3.lebedev_041(), 1.0e-11),
        (quadpy.u3.lebedev_047(), 1.0e-11),
        (quadpy.u3.lebedev_053(), 1.0e-11),
        (quadpy.u3.lebedev_059(), 1.0e-11),
        (quadpy.u3.lebedev_065(), 1.0e-11),
        (quadpy.u3.lebedev_071(), 1.0e-11),
        (quadpy.u3.lebedev_077(), 1.0e-11),
        (quadpy.u3.lebedev_083(), 1.0e-11),
        (quadpy.u3.lebedev_089(), 1.0e-11),
        (quadpy.u3.lebedev_095(), 1.0e-11),
        (quadpy.u3.lebedev_101(), 1.0e-11),
        (quadpy.u3.lebedev_107(), 1.0e-11),
        (quadpy.u3.lebedev_113(), 1.0e-11),
        (quadpy.u3.lebedev_119(), 1.0e-11),
        (quadpy.u3.lebedev_125(), 1.0e-11),
        (quadpy.u3.lebedev_131(), 1.0e-11),
    ]
    + [
        (quadpy.u3.stroud_u3_3_1(), 1.0e-13),
        (quadpy.u3.stroud_u3_5_1(), 1.0e-13),
        (quadpy.u3.stroud_u3_5_2(), 1.0e-13),
        (quadpy.u3.stroud_u3_5_3(), 1.0e-13),
        (quadpy.u3.stroud_u3_5_4(), 1.0e-13),
        (quadpy.u3.stroud_u3_5_5(), 1.0e-13),
        (quadpy.u3.stroud_u3_7_1(), 1.0e-13),
        (quadpy.u3.stroud_u3_7_2(), 1.0e-13),
        (quadpy.u3.stroud_u3_8_1(), 1.0e-13),
        (quadpy.u3.stroud_u3_9_1(), 1.0e-13),
        (quadpy.u3.stroud_u3_9_2(), 1.0e-13),
        (quadpy.u3.stroud_u3_9_3(), 1.0e-13),
        (quadpy.u3.stroud_u3_11_1(), 1.0e-13),
        # TODO fix equation system in 11_2 for higher precision
        (quadpy.u3.stroud_u3_11_2(), 1.0e-12),
        (quadpy.u3.stroud_u3_11_3(), 1.0e-13),
        (quadpy.u3.stroud_u3_14_1(), 1.0e-13),
    ],
)
def test_scheme_cartesian(scheme, tol):
    assert scheme.points.dtype == numpy.float64, scheme.name
    assert scheme.weights.dtype == numpy.float64, scheme.name

    # We're using the spherical harmonic iterator here; it's much less memory-intensive
    # than computing the full tree at once. Unfortunately, we cannot use
    # scheme.integrate with it, but that's okay.
    evaluator = orthopy.u3.Eval(scheme.points.T, "quantum mechanic")

    degree = None
    for k in range(scheme.degree + 2):
        vals = next(evaluator)
        approximate = 4 * numpy.pi * numpy.dot(vals, scheme.weights)

        # construct exact value
        exact = [numpy.sqrt(4 * numpy.pi)] if k == 0 else numpy.zeros_like(approximate)

        if numpy.any(numpy.abs(approximate - exact) > tol):
            degree = k - 1
            break

    assert degree == scheme.degree, "{}  --  Observed: {}, expected: {}".format(
        scheme.name, degree, scheme.degree
    )


# Test a few schemes with integrate_spherical. -- This is basically the same as above,
# no need to repeat it all in detail.
@pytest.mark.parametrize(
    "scheme,tol",
    [
        (quadpy.u3.heo_xu_13(), 1.0e-6),
        (quadpy.u3.heo_xu_15(), 1.0e-6),
        (quadpy.u3.heo_xu_17(), 1.0e-6),
        (quadpy.u3.heo_xu_19_1(), 1.0e-6),
        (quadpy.u3.heo_xu_19_2(), 1.0e-6),
        (quadpy.u3.heo_xu_21_1(), 1.0e-6),
        (quadpy.u3.heo_xu_21_2(), 1.0e-6),
        (quadpy.u3.heo_xu_21_3(), 1.0e-6),
        (quadpy.u3.heo_xu_21_4(), 1.0e-6),
        (quadpy.u3.heo_xu_21_5(), 1.0e-6),
        (quadpy.u3.heo_xu_21_6(), 1.0e-6),
        (quadpy.u3.heo_xu_23_1(), 1.0e-6),
        (quadpy.u3.heo_xu_23_2(), 1.0e-6),
        (quadpy.u3.heo_xu_23_3(), 1.0e-6),
        (quadpy.u3.heo_xu_25_1(), 1.0e-6),
        (quadpy.u3.heo_xu_25_2(), 1.0e-6),
        (quadpy.u3.heo_xu_27_1(), 1.0e-6),
        (quadpy.u3.heo_xu_27_2(), 1.0e-6),
        (quadpy.u3.heo_xu_27_3(), 1.0e-6),
        (quadpy.u3.heo_xu_29(), 1.0e-6),
        (quadpy.u3.heo_xu_31(), 1.0e-6),
        (quadpy.u3.heo_xu_33(), 1.0e-6),
        (quadpy.u3.heo_xu_35(), 1.0e-6),
        (quadpy.u3.heo_xu_37(), 1.0e-6),
        (quadpy.u3.heo_xu_39_1(), 1.0e-6),
        (quadpy.u3.heo_xu_39_2(), 1.0e-6),
    ]
    + [
        (quadpy.u3.lebedev_003a(), 1.0e-11),
        (quadpy.u3.lebedev_003b(), 1.0e-11),
        (quadpy.u3.lebedev_003c(), 1.0e-11),
        (quadpy.u3.lebedev_005(), 1.0e-11),
        (quadpy.u3.lebedev_007(), 1.0e-11),
        (quadpy.u3.lebedev_009(), 1.0e-11),
        (quadpy.u3.lebedev_011(), 1.0e-11),
        (quadpy.u3.lebedev_013(), 1.0e-11),
        (quadpy.u3.lebedev_015(), 1.0e-11),
        (quadpy.u3.lebedev_017(), 1.0e-11),
        (quadpy.u3.lebedev_019(), 1.0e-11),
    ]
    + [
        (quadpy.u3.stroud_u3_3_1(), 1.0e-13),
        (quadpy.u3.stroud_u3_5_1(), 1.0e-13),
        (quadpy.u3.stroud_u3_5_2(), 1.0e-13),
        (quadpy.u3.stroud_u3_5_3(), 1.0e-13),
        (quadpy.u3.stroud_u3_5_4(), 1.0e-13),
        (quadpy.u3.stroud_u3_5_5(), 1.0e-13),
        (quadpy.u3.stroud_u3_7_1(), 1.0e-13),
        (quadpy.u3.stroud_u3_7_2(), 1.0e-13),
        (quadpy.u3.stroud_u3_8_1(), 1.0e-13),
        (quadpy.u3.stroud_u3_9_1(), 1.0e-13),
        (quadpy.u3.stroud_u3_9_2(), 1.0e-13),
        (quadpy.u3.stroud_u3_9_3(), 1.0e-13),
        (quadpy.u3.stroud_u3_11_1(), 1.0e-13),
        # TODO fix equation system in 11_2 for higher precision
        (quadpy.u3.stroud_u3_11_2(), 1.0e-12),
        (quadpy.u3.stroud_u3_11_3(), 1.0e-13),
        (quadpy.u3.stroud_u3_14_1(), 1.0e-13),
    ],
)
def test_scheme_spherical(scheme, tol):
    def sph_tree(azimuthal, polar):
        evaluator = orthopy.u3.EvalPolar(polar, azimuthal, "quantum mechanic")
        return numpy.concatenate([next(evaluator) for _ in range(scheme.degree + 2)])

    print(scheme)

    vals = scheme.integrate_spherical(sph_tree)
    # Put vals back into the tree structure:
    # len(approximate[k]) == k+1
    approximate = [vals[k ** 2 : (k + 1) ** 2] for k in range(scheme.degree + 2)]

    exact = [numpy.zeros(len(s)) for s in approximate]
    exact[0][0] = numpy.sqrt(4 * numpy.pi)

    degree, _ = check_degree_ortho(approximate, exact, abs_tol=tol)

    assert degree == scheme.degree, "{}  --  observed: {}, expected: {}".format(
        scheme.name, degree, scheme.degree
    )


@pytest.mark.parametrize("scheme", [quadpy.u3.lebedev_007()])
def test_show(scheme):
    scheme.show()
    plt.close()


if __name__ == "__main__":
    scheme_ = quadpy.u3.Stroud("U3 5-2")
    # test_scheme(scheme_)
    test_scheme_spherical(scheme_, tol=1.0e-7)
    # test_show(scheme_)
