from numpy import random, argmax, argmin, cross, argwhere, arange, array, hstack, vstack
from matplotlib import pyplot as plt


def segment(u, v, indices, points):

    if indices.shape[0] == 0:
        return array([], dtype=int)

    def crossProduct(i, j):
        return cross(points[indices, :] - points[i, :], points[j, :] - points[i, :])

    w = indices[argmin(crossProduct(u, v))]
    a = indices[argwhere(crossProduct(w, v) < 0).flatten()]
    b = indices[argwhere(crossProduct(u, w) < 0).flatten()]

    return hstack((segment(w, v, a, points), w, segment(u, w, b, points)))


def convex_hull(points):

    u = argmin(points[:, 0])
    v = argmax(points[:, 0])
    indices = arange(0, points.shape[0])
    parted = cross(points[indices, :] - points[u, :], points[v, :] - points[u, :]) < 0

    a = indices[argwhere(~parted)]
    b = indices[argwhere(parted)]

    return hstack((u, segment(v, u, a, points), v, segment(u, v, b, points), u))


groups = (
    random.random((100, 2)),
    0.5 * random.random((100, 2)) + 1,
    0.5 * random.random((100, 2)) - 1,
)

hulls = tuple(map(convex_hull, groups))
hullsUnion = vstack(tuple(group[hi, :] for hi, group in zip(hulls, groups)))
union = convex_hull(hullsUnion)
pts = vstack(groups)
subset = convex_hull(pts)

fig, ax = plt.subplots(1, 2)
ax[0].set_title("Convex hull of all points")
ax[0].axis("equal")
ax[0].scatter(pts[:, 0], pts[:, 1], color="black")
ax[0].plot(pts[subset, 0], pts[subset, 1], color="black")

ax[1].set_title("Convex hull of hulls")
ax[1].axis("equal")
ax[1].plot(hullsUnion[union, 0], hullsUnion[union, 1], color="black")
for hull, group in zip(hulls, groups):
    ax[1].plot(group[hull, 0], group[hull, 1], color="black")

fig.tight_layout()
fig.savefig(fname="convex-hull.png", bgcolor="none")
