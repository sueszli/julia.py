import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from re import U
import argparse
import time
import math
from multiprocessing import Pool, TimeoutError


def sequential_julia(size, xmin, xmax, ymin, ymax, c):
    zabs_max = 10
    nit_max = 300
    xwidth = xmax - xmin
    yheight = ymax - ymin

    julia = np.zeros((size, size))
    for x in range(size):
        for y in range(size):
            nit = 0
            z = complex(x / size * xwidth + xmin, y / size * yheight + ymin)
            while abs(z) <= zabs_max and nit < nit_max:
                z = z**2 + c
                nit += 1
            ratio = nit / nit_max

            julia[x, y] = ratio

    return julia


def parallel_julia(size, xmin, xmax, ymin, ymax, patch, nprocs, c):
    seq = sequential_julia(size, xmin, xmax, ymin, ymax, c)

    """
    # assuming size (mod patch) = 0
    for x in 0 to size (step patch):
        for y in 0 to size (step patch):
            task_list.append( (x, y, patch, meta_information) )
    
    # meta information may contain offsets, original image size, original boundaries of complex plane, etc.
    create Pool with nprocs workers
    
    # make sure that each task in the task_list is handled alone
    # in multiprocessing.Pool.map, we need to specify chunksize=1
    completed_patches = Pool.map(compute_patch, task_list, 1)
    for p in completed_patches:
        copy subimage of p to correct final position
    """

    return seq


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", help="image size in pixels (square images)", type=int, default=500)
    parser.add_argument("--xmin", help="", type=float, default=-1.5)
    parser.add_argument("--xmax", help="", type=float, default=1.5)
    parser.add_argument("--ymin", help="", type=float, default=-1.5)
    parser.add_argument("--ymax", help="", type=float, default=1.5)

    parser.add_argument("--patch", help="patch size in pixels (square images)", type=int, default=20)
    parser.add_argument("--nprocs", help="number of workers", type=int, default=1)

    parser.add_argument("--draw-axes", help="whether to draw axes", action="store_true")
    parser.add_argument("--benchmark", help="whether to execute the script with the benchmark julia set", action="store_true")
    parser.add_argument("-o", help="output file")
    args = parser.parse_args()

    c = None
    if args.benchmark:
        c = complex(-0.2, -0.65)
    else:
        CURVE_START = 48 / 64 * math.pi
        CURVE_END = 60 / 64 * math.pi
        CURVE_SPAN = CURVE_END - CURVE_START
        CURVE_SCALE = 0.755
        phi = CURVE_END - 13 / (30 - 1) * CURVE_SPAN
        c = CURVE_SCALE * math.e ** (phi * 1j)

    stime = time.perf_counter()
    julia_img = parallel_julia(args.size, args.xmin, args.xmax, args.ymin, args.ymax, args.patch, args.nprocs, c)
    rtime = time.perf_counter() - stime
    print(f"{args.size};{args.patch};{args.nprocs};{rtime}")

    if args.o is not None:
        # matplotlib.use("agg") <-- uncomment to save img
        fig, ax = plt.subplots()
        ax.imshow(julia_img, interpolation="nearest", cmap=plt.get_cmap("hot"))

        if args.draw_axes:
            im_width = args.size
            im_height = args.size
            xmin = args.xmin
            xmax = args.xmax
            xwidth = args.xmax - args.xmin
            ymin = args.ymin
            ymax = args.ymax
            yheight = args.ymax - args.ymin

            xtick_labels = np.linspace(xmin, xmax, 7)
            ax.set_xticks([(x - xmin) / xwidth * im_width for x in xtick_labels])
            ax.set_xticklabels(["{:.1f}".format(xtick) for xtick in xtick_labels])
            ytick_labels = np.linspace(ymin, ymax, 7)
            ax.set_yticks([(y - ymin) / yheight * im_height for y in ytick_labels])
            ax.set_yticklabels(["{:.1f}".format(-ytick) for ytick in ytick_labels])
            ax.set_xlabel("Imag")
            ax.set_ylabel("Real")
        else:
            ax.axis("off")

        plt.tight_layout()
        # plt.savefig(args.o, bbox_inches="tight") <-- uncomment to save img
        plt.show()
