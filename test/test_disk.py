# -*- coding: utf-8 -*-
#
import pytest
import quadpy

from helpers import integrate_monomial_over_unit_nball, check_degree


@pytest.mark.parametrize(
    'scheme,tol',
    [(quadpy.disk.CoolsHaegemans(k), 1.0e-14) for k in range(1, 4)]
    + [(quadpy.disk.CoolsKim(k), 1.0e-14) for k in range(1, 4)]
    + [(quadpy.disk.Lether(k), 1.0e-14) for k in range(1, 6)]
    + [(quadpy.disk.Peirce(k), 1.0e-14) for k in range(1, 6)]
    + [(quadpy.disk.WissmannBecker(k), 1.0e-14) for k in ['6-1', '6-2', '8-1']]
    )
def test_scheme(scheme, tol):
    degree = check_degree(
            lambda poly: quadpy.disk.integrate(
                poly, [0.0, 0.0], 1.0, scheme
                ),
            integrate_monomial_over_unit_nball,
            lambda n: quadpy.helpers.partition(n, 2),
            scheme.degree + 1,
            tol=tol
            )
    assert degree == scheme.degree
    return


@pytest.mark.parametrize(
    'scheme',
    [quadpy.disk.Lether(3)]
    )
def test_show(scheme):
    quadpy.disk.show(scheme)
    return


if __name__ == '__main__':
    # scheme_ = quadpy.disk.Lether(5)
    scheme_ = quadpy.disk.WissmannBecker('6-1')
    test_scheme(scheme_, 1.0e-14)
    test_show(scheme_)