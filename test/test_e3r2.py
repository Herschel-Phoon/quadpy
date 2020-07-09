import numpy
import pytest
from helpers import check_degree
from matplotlib import pyplot as plt

import quadpy
from quadpy.enr2._helpers import integrate_monomial_over_enr2


@pytest.mark.parametrize(
    "scheme",
    [
        quadpy.e3r2.stroud_e3r2_5_1(),
        quadpy.e3r2.stroud_e3r2_5_2a(),
        quadpy.e3r2.stroud_e3r2_5_2b(),
        quadpy.e3r2.stroud_e3r2_5_3(),
        quadpy.e3r2.stroud_e3r2_7_1a(),
        quadpy.e3r2.stroud_e3r2_7_1b(),
        quadpy.e3r2.stroud_e3r2_7_2a(),
        quadpy.e3r2.stroud_e3r2_7_2b(),
        quadpy.e3r2.stroud_e3r2_14_1(),
    ],
)
def test_scheme(scheme):
    assert scheme.points.dtype == numpy.float64, scheme.name
    assert scheme.weights.dtype == numpy.float64, scheme.name

    print(scheme)

    degree, err = check_degree(
        lambda poly: scheme.integrate(poly),
        integrate_monomial_over_enr2,
        3,
        scheme.degree + 1,
        tol=scheme.test_tolerance,
    )
    assert (
        degree >= scheme.degree
    ), "{} -- observed: {}, expected: {} (max err: {:.3e})".format(
        scheme.name, degree, scheme.degree, err
    )


@pytest.mark.parametrize("scheme", [quadpy.e3r2.stroud_e3r2_5_1()])
def test_show(scheme, backend="mpl"):
    scheme.show(backend=backend)
    plt.close()


if __name__ == "__main__":
    scheme_ = quadpy.e3r2.Stroud("7-2b")
    test_scheme(scheme_, 1.0e-14)
    test_show(scheme_, backend="vtk")
