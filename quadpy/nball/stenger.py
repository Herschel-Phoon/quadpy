# -*- coding: utf-8 -*-
#
"""
Review: Tabulation of Certain Fully Symmetric Numerical Integration
Formulas of Degree 7, 9 and 11 by Frank Stenger,
Mathematics of Computation,
Vol. 25, No. 116 (Oct., 1971), pp. 935+s58-s125,
<https://www.jstor.org/stable/2004361>.
"""
# TODO According to Stroud, Stenger's original article has data up to n == 20.
from __future__ import division

from ..helpers import untangle, fsd, z
from .helpers import NBallScheme


def stenger_7a(n):
    u, v, B = {
        3: (
            0.285231516480645,
            0.765055323929465,
            [
                -0.542565297000466e01,
                +0.490769827031175e01,
                +0.318402337562406,
                -0.391335495408044e01,
                +0.436675887074467e-01,
                +0.308676098900275e01,
            ],
        ),
        4: (
            0.266216481931920,
            0.727412389740367,
            [
                -0.678226800331914e02,
                +0.299222999307746e02,
                +0.240390523860780,
                -0.118821423811283e02,
                +0.459003238309213e-01,
                +0.361018024911844e01,
            ],
        ),
        # TODO fix
        # 5: (
        #     0.250562808085732,
        #     0.694746590606866,
        #     [
        #         -0.220221371883822e+03,
        #         +0.730167125339176e+02,
        #         +0.143281369027706,
        #         -0.203714128400494e+02,
        #         +0.448293291677155e-01,
        #         +0.383685702879441e+01,
        #     ],
        # ),
        6: (
            0.237383303308445,
            0.666069941755647,
            [
                -0.472474075695084e03,
                +0.127114265148486e03,
                +0.477511403723473e-01,
                -0.275405124688594e02,
                +0.410240990676946e-01,
                +0.376041809497708e01,
            ],
        ),
    }[n]

    data = [
        (B[0], z(n)),
        (B[1], fsd(n, (u, 1))),
        (B[2], fsd(n, (v, 1))),
        (B[3], fsd(n, (u, 2))),
        (B[4], fsd(n, (v, 2))),
        (B[5], fsd(n, (u, 3))),
    ]

    points, weights = untangle(data)
    return NBallScheme("Stenger 7a", n, 7, weights, points)


def stenger_7b(n):
    u, v, B = {
        3: (
            0.765055323929465,
            0.285231516480645,
            [
                +0.192021185324132e02,
                +0.351560542364457,
                -0.743934568569924e01,
                +0.270884863064213e-01,
                +0.226016702392506e01,
                +0.828955120051268e-02,
            ],
        ),
        4: (
            0.727412389740367,
            0.266216481931920,
            [
                +0.474254976042737e02,
                +0.344486899232533,
                -0.133998630586466e02,
                +0.112015320403370e-01,
                +0.255857861534543e01,
                +0.867469794764608e-02,
            ],
        ),
        5: (
            0.694746590606866,
            0.250562807085732,
            [
                +0.860517194425776e02,
                +0.345922662173719,
                -0.190678561571482e02,
                -0.583099411878751e-02,
                +0.264972933271699e01,
                +0.844338721441717e-02,
            ],
        ),
        6: (
            0.666069941755647,
            0.237383303308445,
            [
                +0.127959890358419e03,
                +0.355983426079872,
                -0.233024586505972e02,
                -0.206223580738102e-01,
                +0.254283229095729e01,
                +0.770580714268811e-02,
            ],
        ),
    }[n]

    data = [
        (B[0], z(n)),
        (B[1], fsd(n, (u, 1))),
        (B[2], fsd(n, (v, 1))),
        (B[3], fsd(n, (u, 2))),
        (B[4], fsd(n, (v, 2))),
        (B[5], fsd(n, (u, 3))),
    ]

    points, weights = untangle(data)
    return NBallScheme("Stenger 7b", n, 7, weights, points)


def stenger_9a(n):
    u, v, B = {
        3: (
            0.468848793470714,
            0.830223896278566,
            [
                -0.287231328328341e-01,
                +0.199630268052470,
                +0.636651162483951e-01,
                +0.214860470062486e-01,
                -0.323488968539688e-02,
                +0.543046730120527e-01,
                +0.138854806789114,
                +0.572067170204320e-03,
            ],
        ),
        4: (
            0.442930458136056,
            0.798214220988774,
            [
                -0.713264931069213,
                +0.399661978095933,
                -0.399833383634508e-01,
                -0.114245162120668,
                -0.380033830313039e-02,
                +0.528728807201216e-01,
                +0.771286345600799e-01,
                +0.606328581574664e-03,
                +0.361445580516503e-01,
            ],
        ),
        5: (
            0.420914805023811,
            0.769455324331787,
            [
                -0.148607372859000e01,
                +0.517337302000060,
                -0.128693800819958,
                -0.972921046543696e-01,
                -0.434640813962413e-02,
                +0.485386100042993e-01,
                +0.418811699326262e-03,
                +0.591022411210733e-03,
                +0.370636589159518e-01,
            ],
        ),
        6: (
            0.401905036089210,
            0.743477004521219,
            [
                -0.141522888827140e01,
                +0.225283928934273,
                -0.189925600936916,
                +0.767542859780860e-01,
                -0.467837989649319e-02,
                +0.422029877037414e-01,
                -0.736785106177554e-01,
                +0.537264443490880e-03,
                +0.353013676287120e-01,
            ],
        ),
    }[n]

    data = [
        (B[0], z(n)),
        (B[1], fsd(n, (u, 1))),
        (B[2], fsd(n, (v, 1))),
        (B[3], fsd(n, (u, 2))),
        (B[4], fsd(n, (v, 2))),
        (B[5], fsd(n, (u, 1), (v, 1))),
        (B[6], fsd(n, (u, 3))),
        (B[7], fsd(n, (v, 3))),
    ]
    if n > 3:
        data += [(B[8], fsd(n, (u, 4)))]

    points, weights = untangle(data)
    return NBallScheme("Stenger 9a", n, 9, weights, points)


def stenger_9b(n):
    u, v, B = {
        4: (
            0.798214220988774,
            0.442930458136056,
            [
                -0.128637919793059e01,
                -0.425826693459664e-01,
                +0.688818442509136,
                -0.250067281187269e-02,
                -0.258823394327268,
                +0.528728807201216e-01,
                -0.435041640541910e-04,
                +0.149417750663380,
                +0.324916372814428e-03,
            ],
        ),
        5: (
            0.769455324331787,
            0.420914805023811,
            [
                -0.442739121785452e01,
                -0.138203890424606,
                +0.170337438731052e01,
                -0.780124537881237e-03,
                -0.542056011645791,
                +0.485386100042993e-01,
                -0.597738789370232e-03,
                +0.148673447363133,
                +0.297190300145242e-03,
            ],
        ),
        6: (
            0.743477004521219,
            0.401905036089210,
            [
                -0.982577681614207e01,
                -0.210519035276982,
                +0.304939333923123e01,
                +0.149965040552639e-02,
                -0.770478537111000,
                +0.422029877037414e-01,
                -0.100724313201402e-02,
                +0.138129695154516,
                +0.257417929250816e-03,
            ],
        ),
    }[n]

    data = [
        (B[0], z(n)),
        (B[1], fsd(n, (u, 1))),
        (B[2], fsd(n, (v, 1))),
        (B[3], fsd(n, (u, 2))),
        (B[4], fsd(n, (v, 2))),
        (B[5], fsd(n, (u, 1), (v, 1))),
        (B[6], fsd(n, (u, 3))),
        (B[7], fsd(n, (v, 3))),
    ]
    if n > 3:
        data += [(B[8], fsd(n, (u, 4)))]

    points, weights = untangle(data)
    return NBallScheme("Stenger 9b", n, 9, weights, points)


def stenger_11a(n):
    u, v, w, B = {
        3: (
            0.871740148509601,
            0.209299217902484,
            0.591700181433148,
            [
                -0.241858949226757e02,
                -0.260615043902870,
                +0.135920710866830e02,
                +0.128644782328402,
                -0.827362457508920e-02,
                -0.773259998046230e01,
                +0.121529267823348,
                +0.107430092990906,
                -0.457147160368296e-02,
                -0.454573469083632e-03,
                +0.453152994236346e01,
                +0.249979156876400e-01,
                +0.537579305958677e-02,
            ],
        ),
        4: (
            0.844750603518454,
            0.198187323325469,
            0.564399481003361,
            [
                +0.142841140985092e03,
                -0.409969170254506,
                -0.833355966329160e02,
                +0.477233536818062e-01,
                -0.167713384337120e-01,
                +0.486046977166435e02,
                +0.762265878588936e-01,
                +0.945800683336929e-01,
                -0.500622516633870e-02,
                -0.498867819405501e-03,
                -0.283869034949532e02,
                +0.255516059013563e-01,
                +0.504633074872994e-02,
                +0.535903211027872e-04,
                +0.166581940110341e02,
            ],
        ),
        # TODO find typo
        # 5: (
        #     0.819845995463488,
        #     0.540604637387361,
        #     0.188677422490785,
        #     [
        #         -0.455346412352218e+03,
        #         -0.643198057179463,
        #         -0.313723910937508,
        #         +0.142863899851242e+03,
        #         -0.115044196304602e-02,
        #         +0.149484688898586,
        #         -0.373831314185824e+02,
        #         -0.141469445049282e-01,
        #         +0.104863970436266,
        #         -0.973070178977534e-03,
        #         -0.862234640073899e-02,
        #         +0.654476925250512e+01,
        #         +0.153312717360660e-02,
        #         -0.611928443128898e-04,
        #         +0.622126777947090e-02,
        #         +0.887274197302674e-05,
        #     ],
        # ),
    }[n]

    data = [
        (B[0], z(n)),
        (B[1], fsd(n, (u, 1))),
        (B[2], fsd(n, (v, 1))),
        (B[3], fsd(n, (w, 1))),
        (B[4], fsd(n, (u, 2))),
        (B[5], fsd(n, (v, 2))),
        (B[6], fsd(n, (w, 2))),
        (B[7], fsd(n, (u, 1), (v, 1))),
        (B[8], fsd(n, (u, 1), (w, 1))),
        (B[9], fsd(n, (u, 3))),
        (B[10], fsd(n, (v, 3))),
        (B[11], fsd(n, (w, 3))),
        (B[12], fsd(n, (u, 2), (v, 1))),
    ]
    if n > 3:
        data += [(B[13], fsd(n, (u, 4))), (B[14], fsd(n, (v, 4)))]
    if n > 4:
        data += [(B[15], fsd(n, (u, 5)))]

    points, weights = untangle(data)
    return NBallScheme("Stenger 11a", n, 11, weights, points)


def stenger_11b(n):
    u, v, w, B = {
        # TODO find typo
        # 3: (
        #     0.871740148509601,
        #     0.591700181433148,
        #     0.209299217902484,
        #     [
        #         -0.369608422804220e+02,
        #         -0.292281498761429,
        #         +0.981554121166593e-01,
        #         +0.200417005906264e+02,
        #         +0.915649460852702e-03,
        #         +0.140881585655056,
        #         -0.109681663185532e+02,
        #         -0.867910432951898e-02,
        #         +0.118181679110079,
        #         -0.172723379038583e-02,
        #         +0.153215767717862e-01,
        #         +0.614931311140891e+01,
        #         +0.205381636291801e-02,
        #     ],
        # ),
        4: (
            0.844750603518454,
            0.564399481003361,
            0.198187323325469,
            [
                -0.176252077581424e03,
                -0.499462881047293,
                -0.922793735873844e-01,
                +0.698573153138448e02,
                -0.179342748736783e-04,
                +0.138909533618563,
                -0.246907169366506e02,
                -0.122578300082603e-01,
                +0.114765391328613,
                -0.134570335654617e-02,
                +0.330804559042674e-02,
                +0.659514417940443e01,
                +0.181290121048040e-02,
                -0.544956432165929e-04,
                +0.657282387101229e-02,
            ],
        ),
        5: (
            0.819845995463488,
            0.188677422490785,
            0.540604637387361,
            [
                +0.101979474263003e04,
                -0.483876622763145,
                -0.435066365787229e03,
                +0.431869862745281e-01,
                -0.229234716520547e-01,
                +0.174586702318035e03,
                +0.261731304360525e-01,
                +0.779664996582579e-01,
                -0.494818146328864e-02,
                -0.473327076222103e-03,
                -0.625137212983254e02,
                +0.243721155686252e-01,
                +0.448291181300128e-02,
                +0.284624253627758e-04,
                +0.168650924640304e02,
                +0.887274197302674e-05,
            ],
        ),
    }[n]

    data = [
        (B[0], z(n)),
        (B[1], fsd(n, (u, 1))),
        (B[2], fsd(n, (v, 1))),
        (B[3], fsd(n, (w, 1))),
        (B[4], fsd(n, (u, 2))),
        (B[5], fsd(n, (v, 2))),
        (B[6], fsd(n, (w, 2))),
        (B[7], fsd(n, (u, 1), (v, 1))),
        (B[8], fsd(n, (u, 1), (w, 1))),
        (B[9], fsd(n, (u, 3))),
        (B[10], fsd(n, (v, 3))),
        (B[11], fsd(n, (w, 3))),
        (B[12], fsd(n, (u, 2), (v, 1))),
    ]
    if n > 3:
        data += [(B[13], fsd(n, (u, 4))), (B[14], fsd(n, (v, 4)))]
    if n > 4:
        data += [(B[15], fsd(n, (u, 5)))]

    points, weights = untangle(data)
    return NBallScheme("Stenger 11b", n, 11, weights, points)


Stenger = {
    "7a": stenger_7a,
    "7b": stenger_7b,
    "9a": stenger_9a,
    "9b": stenger_9b,
    "11a": stenger_11a,
    "11b": stenger_11b,
}
