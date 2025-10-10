class OrientationChecker():
    @staticmethod
    def Triplet_Orientation(p:list, q:list, r:list):
        return (q[-1] - p[-1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[-1] - q[-1])


if __name__ == "__main__":
    oc = OrientationChecker()
    print(oc.Triplet_Orientation([0,0], [4,4],[1,2]))