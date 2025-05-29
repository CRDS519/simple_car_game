def lerp(A, B, t):
    return A + (B - A)*t

def get_intersection(A, B, C, D):
    t_top = (D[0] - C[0])*(A[1] - C[1]) - (D[1] - C[1])*(A[0] - C[0])
    u_top = (C[1] - A[1])*(A[0] - B[0]) - (C[0] - A[0])*(A[1] - B[1])
    bottom = (D[1] - C[1])*(B[0] - A[0]) - (D[0] - C[0])*(B[1] - A[1])

    if bottom != 0:
        t = t_top/bottom
        u = u_top/bottom
        if t >= 0 and t <= 1 and u >= 0 and u <= 1:
            return [
                lerp(A[0], B[0], t),
                lerp(A[1], B[1], t),
                t
                ]

def poly_intersect(poly1, poly2):
    n = len(poly1)
    m = len(poly2)
    for i in range(n):
        for j in range(m):
            touch = get_intersection(
                poly1[i],
                poly1[(i + 1) % n],
                poly2[j],
                poly2[(j + 1) % m]
            )
            if touch:
                return True
    return False
