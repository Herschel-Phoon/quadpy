import numpy

from ..helpers import QuadratureScheme, plot_disks


class U2Scheme(QuadratureScheme):
    def __init__(self, name, source, degree, weights, points, tol=1.0e-14):
        super().__init__(name, weights, points, degree, source, tol)
        self.domain = "U2"

    def show(self, *args, **kwargs):
        from matplotlib import pyplot as plt

        self.plot(*args, **kwargs)
        plt.show()

    def plot(self, show_axes=False):
        from matplotlib import pyplot as plt

        ax = plt.gca()
        # change default range so that new disks will work
        ax.axis("equal")
        ax.set_xlim((-1.5, 1.5))
        ax.set_ylim((-1.5, 1.5))

        if not show_axes:
            ax.set_axis_off()

        disk1 = plt.Circle((0, 0), 1, color="k", fill=False)
        ax.add_artist(disk1)

        # The total area is used to gauge the disk radii. This is only meaningful for 2D
        # manifolds, not for the circle. What we do instead is choose the total_area
        # such that the sum of the disk radii equals pi.
        total_area = numpy.pi ** 3 / len(self.weights)
        plot_disks(plt, self.points, self.weights, total_area)

    def integrate(self, f, center, radius, dot=numpy.dot):
        center = numpy.array(center)
        rr = numpy.multiply.outer(radius, self.points)
        rr = numpy.swapaxes(rr, 0, -2)
        ff = numpy.array(f((rr + center).T))
        ref_vol = 2 * numpy.pi * numpy.asarray(radius)
        return ref_vol * dot(ff, self.weights)
