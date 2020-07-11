import numpy
import orthopy
import pytest

import quadpy

schemes = [
    quadpy.e2r2.haegemans_piessens_a(),
    quadpy.e2r2.haegemans_piessens_b(),
    quadpy.e2r2.rabinowitz_richter_1(),
    quadpy.e2r2.rabinowitz_richter_2(),
    quadpy.e2r2.rabinowitz_richter_3(),
    quadpy.e2r2.rabinowitz_richter_4(),
    quadpy.e2r2.rabinowitz_richter_5(),
    quadpy.e2r2.stroud_4_1(),
    quadpy.e2r2.stroud_5_1(),
    quadpy.e2r2.stroud_5_2(),
    quadpy.e2r2.stroud_7_1(),
    quadpy.e2r2.stroud_7_2(),
    quadpy.e2r2.stroud_9_1(),
    quadpy.e2r2.stroud_11_1(),
    quadpy.e2r2.stroud_11_2(),
    quadpy.e2r2.stroud_13_1(),
    quadpy.e2r2.stroud_15_1(),
    quadpy.e2r2.stroud_secrest_5(),
    quadpy.e2r2.stroud_secrest_6(),
]


@pytest.mark.parametrize("scheme", schemes)
def test_scheme(scheme, tol=1.0e-14):
    assert scheme.points.dtype == numpy.float64, scheme.name
    assert scheme.weights.dtype == numpy.float64, scheme.name

    print(scheme)

    evaluator = orthopy.enr2.Eval(scheme.points.T, "physicists")

    degree = None
    for k in range(scheme.degree + 2):
        approximate = scheme.integrate(lambda x: next(evaluator)[0])
        exact = numpy.sqrt(numpy.pi) if k == 0 else 0.0
        err = numpy.abs(approximate - exact)
        if numpy.any(err > tol):
            degree = k - 1
            break

    max_err = numpy.max(err)
    assert degree >= scheme.degree, (
        f"{scheme.name} -- observed: {degree}, expected: {scheme.degree} "
        f"(max err: {max_err:.3e})"
    )


@pytest.mark.parametrize("scheme", [quadpy.e2r2.rabinowitz_richter_1()])
def test_show(scheme):
    scheme.show()


if __name__ == "__main__":
    # scheme_ = quadpy.e2r2.Stroud["7-2"]()
    # test_scheme(scheme_, 1.0e-14)
    # test_show(scheme_)
    from helpers import find_equal

    find_equal(schemes)
