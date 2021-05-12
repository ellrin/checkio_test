def similar_triangles(Coord1, Coord2):

    def getAngle(coordinate):

        def getSideLength(coordinate1, coordinate2):

            lenx = abs(coordinate1[0] - coordinate2[0])
            leny = abs(coordinate1[1] - coordinate2[1])
            return (lenx**2+leny**2)**0.5

        sLen1 = getSideLength(coordinate[0], coordinate[1])
        sLen2 = getSideLength(coordinate[1], coordinate[2])
        sLen3 = getSideLength(coordinate[0], coordinate[2])

        cos1 = (sLen2**2+sLen3**2-sLen1**2)/(2*sLen2*sLen3)
        cos2 = (sLen1**2+sLen3**2-sLen2**2)/(2*sLen1*sLen3)
        cos3 = (sLen1**2+sLen2**2-sLen3**2)/(2*sLen1*sLen2)

        cos1 = float("%0.4f" % (cos1))
        cos2 = float("%0.4f" % (cos2))
        cos3 = float("%0.4f" % (cos3))
        return cos1, cos2, cos3

    return True if set(getAngle(Coord1))==set(getAngle(Coord2)) else False


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")





