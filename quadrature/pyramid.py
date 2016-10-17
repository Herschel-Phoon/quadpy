# -*- coding: utf-8 -*-
#
import math
import numpy


def show(pyra, scheme, ball_scale=1.0, alpha=0.3):
    '''Shows the quadrature points on a given pyramid. The size of the
    balls around the points coincides with their weights.
    '''
    from matplotlib import pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_aspect('equal')

    edges = numpy.array([
        [pyra[0], pyra[1]],
        [pyra[1], pyra[2]],
        [pyra[2], pyra[3]],
        [pyra[3], pyra[0]],
        #
        [pyra[0], pyra[4]],
        [pyra[1], pyra[4]],
        [pyra[2], pyra[4]],
        [pyra[3], pyra[4]],
        ])
    for edge in edges:
        plt.plot(edge[:, 0], edge[:, 1], edge[:, 2], '-k')

    xi = scheme.points[:, 0]
    eta = scheme.points[:, 1]
    zeta = scheme.points[:, 2]
    transformed_pts = \
        + numpy.outer(pyra[0], 0.125*(1.0-xi)*(1.0-eta)*(1-zeta)) \
        + numpy.outer(pyra[1], 0.125*(1.0+xi)*(1.0-eta)*(1-zeta)) \
        + numpy.outer(pyra[2], 0.125*(1.0+xi)*(1.0+eta)*(1-zeta)) \
        + numpy.outer(pyra[3], 0.125*(1.0-xi)*(1.0+eta)*(1-zeta)) \
        + numpy.outer(pyra[4], 0.500*(1.0+zeta))
    transformed_pts = transformed_pts.T

    weight_scale = abs(_get_det_J(pyra, scheme.points.T))

    s = 1.0
    phi, theta = numpy.mgrid[0:numpy.pi:101j, 0:2*numpy.pi:101j]
    x = numpy.sin(phi)*numpy.cos(theta)
    y = numpy.sin(phi)*numpy.sin(theta)
    z = numpy.cos(phi)
    for tp, weight, beta in zip(transformed_pts, scheme.weights, weight_scale):
        color = 'b' if weight >= 0 else 'r'
        # highlight ball center
        plt.plot([tp[0]], [tp[1]], [tp[2]], '.' + color)

        # plot ball
        # scale the circle volume according to the weight
        r = ball_scale * (
            s * abs(beta*weight) / (4.0/3.0 * numpy.pi)
            )**(1.0/3.0)

        ax.plot_surface(
            r*x + tp[0], r*y + tp[1], r*z + tp[2],
            color=color,
            alpha=alpha,
            linewidth=0
            )

    # http://stackoverflow.com/a/21765085/353337
    alpha = 1.3
    max_range = alpha * 0.5 * numpy.array([
        pyra[:, 0].max() - pyra[:, 0].min(),
        pyra[:, 1].max() - pyra[:, 1].min(),
        pyra[:, 2].max() - pyra[:, 2].min(),
        ]).max()
    mid_x = 0.5 * (pyra[:, 0].max() + pyra[:, 0].min())
    mid_y = 0.5 * (pyra[:, 1].max() + pyra[:, 1].min())
    mid_z = 0.5 * (pyra[:, 2].max() + pyra[:, 2].min())
    #
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    return


def _get_det_J(pyra, xi):
    J0 = \
        - numpy.outer(pyra[0], 0.125*(1.0-xi[1])*(1-xi[2])) \
        + numpy.outer(pyra[1], 0.125*(1.0-xi[1])*(1-xi[2])) \
        + numpy.outer(pyra[2], 0.125*(1.0+xi[1])*(1-xi[2])) \
        - numpy.outer(pyra[3], 0.125*(1.0+xi[1])*(1-xi[2]))
    J1 = \
        - numpy.outer(pyra[0], 0.125*(1.0-xi[0])*(1-xi[2])) \
        - numpy.outer(pyra[1], 0.125*(1.0+xi[0])*(1-xi[2])) \
        + numpy.outer(pyra[2], 0.125*(1.0+xi[0])*(1-xi[2])) \
        + numpy.outer(pyra[3], 0.125*(1.0-xi[0])*(1-xi[2]))
    J2 = \
        - numpy.outer(pyra[0], 0.125*(1.0-xi[0])*(1.0-xi[1])) \
        - numpy.outer(pyra[1], 0.125*(1.0+xi[0])*(1.0-xi[1])) \
        - numpy.outer(pyra[2], 0.125*(1.0+xi[0])*(1.0+xi[1])) \
        - numpy.outer(pyra[3], 0.125*(1.0-xi[0])*(1.0+xi[1])) \
        + numpy.outer(pyra[4], 0.500*numpy.ones(1))
    det = J0[0]*J1[1]*J2[2] + J1[0]*J2[1]*J0[2] + J2[0]*J0[1]*J1[2] \
        - J0[2]*J1[1]*J2[0] - J1[2]*J2[1]*J0[0] - J2[2]*J0[1]*J1[0]
    return det


def integrate(f, pyra, scheme):
    xi = scheme.points.T
    x = \
        + numpy.outer(pyra[0], 0.125*(1.0-xi[0])*(1.0-xi[1])*(1-xi[2])) \
        + numpy.outer(pyra[1], 0.125*(1.0+xi[0])*(1.0-xi[1])*(1-xi[2])) \
        + numpy.outer(pyra[2], 0.125*(1.0+xi[0])*(1.0+xi[1])*(1-xi[2])) \
        + numpy.outer(pyra[3], 0.125*(1.0-xi[0])*(1.0+xi[1])*(1-xi[2])) \
        + numpy.outer(pyra[4], 0.500*(1.0+xi[2]))
    det = _get_det_J(pyra, xi)
    return math.fsum(scheme.weights * f(x).T * abs(det))


class Felippa(object):
    '''
    Carlos Felippa,
    A compendium of FEM integration formulas for symbolic work,
    Engineering Computation,
    Volume 21, Number 8, 2004, pages 867-890,
    <http://dx.doi.org/10.1108/02644400410554362>.

    Abstract:
    This paper presents a set of Mathematica modules that organizes numerical
    integration rules considered useful for finite element work. Seven regions
    are considered: line segments, triangles, quadrilaterals, tetrahedral,
    wedges, pyramids and hexahedra. Information can be returned in
    floating-point (numerical) form, or in exact symbolic form. The latter is
    useful for computer-algebra aided FEM work that carries along symbolic
    variables. A few quadrature rules were extracted from sources in the FEM
    and computational mathematics literature, and placed in symbolic form using
    Mathematica to generate own code. A larger class of formulas, previously
    known only numerically, were directly obtained through symbolic
    computations. Some unpublished non-product rules for pyramid regions were
    found and included in the collection. For certain regions: quadrilaterals,
    wedges and hexahedra, only product rules were included to economize
    programming. The collection embodies most FEM-useful formulas of low and
    moderate order for the seven regions noted above. Some gaps as regard
    region geometries and omission of non-product rules are noted in the
    conclusions. The collection may be used “as is” in support of symbolic FEM
    work thus avoiding contamination with floating arithmetic that precludes
    simplification. It can also be used as generator for low-level
    floating-point code modules in Fortran or C. Floating point accuracy can be
    selected arbitrarily. No similar modular collection applicable to a range
    of FEM work, whether symbolic or numeric, has been published before.
    '''
    def __init__(self, index):
        wg9 = numpy.array([64.0, 40.0, 25.0]) / 81.0

        if index == 1:
            self.weights = numpy.array([128.0/27.0])
            self.points = numpy.array([
                [0.0, 0.0, -0.5],
                ])
            self.degree = 1
        elif index == 2:
            self.weights = numpy.concatenate([
                0.81 * numpy.ones(4),
                125.0/27.0 * numpy.ones(1)
                ])
            self.points = numpy.concatenate([
                self._s4(8 * numpy.sqrt(2.0/15.0) / 5, -2.0/3.0),
                numpy.array([[0.0, 0.0, 0.4]]),
                ])
            self.degree = 2
        elif index == 3:
            self.weights = numpy.concatenate([
                504.0/625.0 * numpy.ones(4),
                576.0/625.0 * numpy.ones(1),
                64.0/15.0 * numpy.ones(1),
                ])
            self.points = numpy.concatenate([
                self._s4(numpy.sqrt(12.0/35.0), -2.0/3.0),
                numpy.array([[0.0, 0.0, 1.0/6.0]]),
                numpy.array([[0.0, 0.0, 0.5]]),
                ])
            self.degree = 2
        elif index == 4:
            w1 = 5 * (68.0 + 5*numpy.sqrt(10.0)) / 432.0
            w2 = 85.0/54.0 - w1
            self.weights = numpy.concatenate([
                w1 * numpy.ones(4),
                w2 * numpy.ones(4),
                ])
            g1 = numpy.sqrt(1.0/3.0)
            g2 = (2*numpy.sqrt(10)-5) / 15.0
            self.points = numpy.concatenate([
                self._s4(g1, g2),
                self._s4(g1, -2.0/3.0 - g2),
                ])
            self.degree = 3
        elif index == 5:
            w1 = (11764.0 - 461.0*numpy.sqrt(51.0)) / 15300.0
            w2 = 346.0 / 225.0 - w1
            self.weights = numpy.concatenate([
                w1 * numpy.ones(4),
                w2 * numpy.ones(4),
                ])
            g1 = numpy.sqrt(2.0/15.0 * (573 - 2*numpy.sqrt(51))) / 15.0
            g2 = numpy.sqrt(2.0/15.0 * (573 + 2*numpy.sqrt(51))) / 15.0
            g3 = -(2*numpy.sqrt(51.0) + 13) / 35.0
            g4 = +(2*numpy.sqrt(51.0) - 13) / 35.0
            self.points = numpy.concatenate([
                self._s4(g1, g3),
                self._s4(g2, g4),
                ])
            self.degree = 2
        elif index == 6:
            w1 = 7.0*(11472415.0 - 70057.0*numpy.sqrt(2865.0)) / 130739500.0
            w2 = 84091.0/68450.0 - w1
            self.weights = numpy.concatenate([
                w1 * numpy.ones(4),
                w2 * numpy.ones(4),
                3.6 * numpy.ones(1),
                ])

            g1 = 8 * numpy.sqrt(
                (573 + 5*numpy.sqrt(2865.0))
                / (109825 + 969*numpy.sqrt(2865.0))
                )
            g2 = numpy.sqrt(2*(8025 + numpy.sqrt(2865.0)) / 35.0) / 37.0
            g3 = -(+87 + numpy.sqrt(2865.0)) / 168.0
            g4 = +(-87 + numpy.sqrt(2865.0)) / 168.0
            self.points = numpy.concatenate([
                self._s4(g1, g3),
                self._s4(g2, g4),
                numpy.array([[0.0, 0.0, 2.0/3.0]])
                ])
            self.degree = 2
        elif index == 7:
            w1 = 170569.0 / 331200.0
            w2 = 276710106577408.0 / 1075923777052725.0
            w3 = 12827693806929.0 / 30577384040000.0
            w4 = 10663383340655070643544192.0 / 4310170528879365193704375.0
            self.weights = numpy.concatenate([
                w1 * numpy.ones(4),
                w2 * numpy.ones(4),
                w3 * numpy.ones(4),
                w4 * numpy.ones(1),
                ])

            g1 = 7 * numpy.sqrt(35.0/59.0) / 8.0
            g2 = 224 * numpy.sqrt(336633710.0/33088740423.0) / 37.0
            g3 = numpy.sqrt(37043.0/35.0) / 56.0
            g4 = -127.0/153.0
            g5 = 1490761.0 / 2842826.0
            self.points = numpy.concatenate([
                self._s4(g1, -1.0/7.0),
                self._s4_0(g2, -9.0/28.0),
                self._s4(g3, g4),
                numpy.array([[0.0, 0.0, g5]])
                ])
            self.degree = 2
        elif index == 8:
            w1 = 5 * (68.0 + 5.0*numpy.sqrt(10)) / 432.0
            w2 = 85.0/54.0 - w1
            self.weights = numpy.concatenate([
                w1*wg9[2] * numpy.ones(4),
                w1*wg9[1] * numpy.ones(4),
                w1*wg9[0] * numpy.ones(1),
                w2*wg9[2] * numpy.ones(4),
                w2*wg9[1] * numpy.ones(4),
                w2*wg9[0] * numpy.ones(1),
                ])

            g1 = numpy.sqrt(0.6)
            g2 = 1.0 - 2*(10.0 - numpy.sqrt(10)) / 15.0
            g3 = -2.0/3.0 - g2
            self.points = numpy.concatenate([
                self._s4(g1, g2),
                self._s4_0(g1, g2),
                numpy.array([[0.0, 0.0, g2]]),
                self._s4(g1, g3),
                self._s4_0(g1, g3),
                numpy.array([[0.0, 0.0, g3]])
                ])
            self.degree = 3
        elif index == 9:
            g1 = numpy.sqrt(0.6)
            g3 = -0.854011951853700535688324041975993416
            g4 = -0.305992467923296230556472913192103090
            g5 = +0.410004419776996766244796955168096505
            self.points = numpy.concatenate([
                self._s4(g1, g3),
                self._s4_0(g1, g3),
                numpy.array([[0.0, 0.0, g3]]),
                self._s4(g1, g4),
                self._s4_0(g1, g4),
                numpy.array([[0.0, 0.0, g4]]),
                self._s4(g1, g5),
                self._s4_0(g1, g5),
                numpy.array([[0.0, 0.0, g5]]),
                ])

            w1 = (4.0/15.0)*(4+5*(g4+g5)+10*g4*g5)/((g3-g4)*(g3-g5)*(1-g3)**2)
            w2 = (4.0/15.0)*(4+5*(g3+g5)+10*g3*g5)/((g3-g4)*(g5-g4)*(1-g4)**2)
            w3 = (4.0/15.0)*(4+5*(g3+g4)+10*g3*g4)/((g3-g5)*(g4-g5)*(1-g5)**2)
            self.weights = numpy.concatenate([
                w1*wg9[2] * numpy.ones(4),
                w1*wg9[1] * numpy.ones(4),
                w1*wg9[0] * numpy.ones(1),
                w2*wg9[2] * numpy.ones(4),
                w2*wg9[1] * numpy.ones(4),
                w2*wg9[0] * numpy.ones(1),
                w3*wg9[2] * numpy.ones(4),
                w3*wg9[1] * numpy.ones(4),
                w3*wg9[0] * numpy.ones(1),
                ])

            self.degree = 5
        else:
            raise ValueError('Illegal Felippa index')

        return

    def _s4(self, a, z):
        return numpy.array([
            [+a, +a, z],
            [-a, +a, z],
            [+a, -a, z],
            [-a, -a, z],
            ])

    def _s4_0(self, a, z):
        return numpy.array([
            [+a, 0.0, z],
            [-a, 0.0, z],
            [0.0, +a, z],
            [0.0, -a, z],
            ])