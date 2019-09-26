from fractions import Fraction as fr
import decimal as dec


def intersection(x1, x2, x3, x4, y1, y2, y3, y4):
    a1 = y2 - y1
    b1 = x1 - x2
    c1 = (a1 * x1) + (b1 * y1)
    a2 = y4 - y3
    b2 = x3 - x4
    c2 = (a2 * x3) + (b2 * y3)
    numerator1 = float((b2 * c1) - (b1 * c2))
    numerator2 = float((a1 * c2) - (a2 * c1))
    denominator = float((a1 * b2) - (a2 * b1))
    if denominator == 0:
        # print 'denom=0', [x1,y1], [x2,y2], [x3,y3], [x4,y4]
        return None, None
    # intersecting coordinates
    x = numerator1 / denominator
    y = numerator2 / denominator
    if (x2 - x1) == 0:
        rx0 = -1
    else:
        rx0 = (x-x1) / (x2-x1)
    if (y2 - y1) == 0:
        ry0 = -1
    else:
        ry0 = (y-y1) / (y2-y1)
    if (x4 - x3) == 0:
        rx1 = -1
    else:
        rx1 = (x-x3) / (x4-x3)
    if (y4 - y3) == 0:
        ry1 = -1
    else:
        ry1 = (y-y3) / (y4-y3)
    # print 'reached here'
    if (0 <= rx0 <= 1 or 0 <= ry0 <= 1) and (0 <= rx1 <= 1 or 0 <= ry1 <= 1):
        return x, y
    else:
        return None, None






