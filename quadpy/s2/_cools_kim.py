import numpy

from ..helpers import article, untangle
from ._helpers import S2Scheme

_citation = article(
    authors=["R. Cools", "K.J. Kim"],
    title="A survey of known and new cubature formulas for the unit disk",
    journal="Korean J. Comput. & Appl. Math.",
    volume="7",
    month="sep",
    year="2000",
    number="3",
    pages="477-485",
    # url="https://doi.org/10.1007/BF03012263"
)


def cools_kim_1():
    data = [
        (0.11498334179998566, numpy.array([[0.0, 0.0]])),
        (0.042666281539386779, _s40(0.88696766316393713)),
        (0.087938325357145539, _s40(0.42463390374323367)),
        (0.076206570461793249, _s40(0.69446902308083445)),
        (0.019156522218855521, _s4(0.68785354082699271)),
        (0.062085722273139239, _s4(0.59664767781455707)),
        (0.095664962820418119, _s4(0.23562252091530831)),
        (0.085162533604288747, _s8(0.31294754888343992, 0.54894025523701459)),
        (0.020201237989565462, _s8(0.96121228504617867, 0.17385745088683603)),
        (0.056834571713156972, _s8(0.30538732225214729, 0.79035487531148609)),
        (0.024268628331345539, _s8(0.84937290409632805, 0.46270056598293749)),
    ]
    points, weights = untangle(data)
    return S2Scheme("Cools-Kim 1", weights, points, 17, _citation)


def cools_kim_2():
    data = [
        (0.092826182741729107, numpy.array([[0.0, 0.0]])),
        (0.061210649714171629, _s40(0.79836610957931832)),
        (0.084701305074092631, _s40(0.30042292336770777)),
        (0.0064918529741922661, _s40(0.99615333438631671)),
        (0.014104347317113714, _s4(0.69583191637449732)),
        (0.077590938349196292, _s4(0.28670391168237706)),
        (0.046841922848831439, _s4(0.61667878163587778)),
        (0.071523458803010660, _s4(0.47214212637530880)),
        (0.077267777905420501, _s8(0.56686082157858617, 0.15587783378762243)),
        (0.034350583657896668, _s8(0.92555127310854838, 0.17347695471172525)),
        (0.028368949384516057, _s8(0.83822144355055265, 0.46025996563724600)),
        (0.0018669074320751099, _s8(0.96670876580048578, 0.33737925901740466)),
        (0.058009352935795362, _s8(0.73773390012389973, 0.32685240870845720)),
    ]
    points, weights = untangle(data)
    return S2Scheme("Cools-Kim 2", weights, points, 19, _citation)


def cools_kim_3():
    data = [
        (0.064712088156233115, _s40(0.18089963670914432)),
        (0.012203257346077736, _s40(0.98391537714755427)),
        (4.6214466764876138e-05, _s4(0.77364389614737803)),
        (0.020941123674084990, _s4(0.67975937134823609)),
        (0.044321766954122515, _s4(0.59230560995561076)),
        (0.052715691149269700, _s4(0.41774444740353380)),
        (0.028690025849304919, _s8(0.89789289495208579, 0.13375169526590821)),
        (0.013819709344648730, _s8(0.93927352486965313, 0.27985732696474981)),
        (0.037034888202855274, _s8(0.79099671385625722, 0.39385576573951899)),
        (0.047520136607474831, _s8(0.56605481445792489, 0.10885005806786229)),
        (0.014296165120136605, _s8(0.83180776464845906, 0.51224072541565606)),
        (0.042923763669888949, _s8(0.76010583069266321, 0.12830595415488073)),
        (0.047444099811669938, _s8(0.62209339812108792, 0.34691040719842391)),
        (0.063500222219468438, _s8(0.36200059276768541, 0.16676191877222966)),
    ]
    points, weights = untangle(data)
    return S2Scheme("Cools-Kim 3", weights, points, 21, _citation)


def _s4(a):
    return numpy.array([[+a, +a], [-a, +a], [+a, -a], [-a, -a]])


def _s40(a):
    return numpy.array([[+a, 0.0], [-a, 0.0], [0.0, +a], [0.0, -a]])


def _s8(a, b):
    return numpy.array(
        [[+a, +b], [-a, +b], [+a, -b], [-a, -b], [+b, +a], [-b, +a], [+b, -a], [-b, -a]]
    )
