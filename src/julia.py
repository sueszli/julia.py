import numpy as np
from re import U
import argparse
import time
import math
from multiprocessing import Pool, TimeoutError
import functools


def benchmark(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        stime = time.perf_counter()
        result = func(*args, **kwargs)
        rtime = time.perf_counter() - stime
        rtime_ms = rtime * 1000
        print(f"{func.__name__}() in {rtime_ms:.4f} ms")
        return result

    return wrapper


def sequential_julia(xmin, xmax, ymin, ymax, size, c):
    zabs_max = 10
    nit_max = 300

    xwidth = xmax - xmin
    yheight = ymax - ymin

    julia = np.zeros((size, size))
    for ix in range(size):
        for iy in range(size):
            nit = 0
            z = complex(ix / size * xwidth + xmin, iy / size * yheight + ymin)
            while abs(z) <= zabs_max and nit < nit_max:
                z = z**2 + c
                nit += 1
            ratio = nit / nit_max

            julia[ix, iy] = ratio

    return julia


def patch_sequential_julia(xmin, xmax, ymin, ymax, x_start, x_end, y_start, y_end, size, c):
    zabs_max = 10
    nit_max = 300

    xwidth = xmax - xmin
    yheight = ymax - ymin

    julia_patch = np.zeros((x_end - x_start, y_end - y_start))
    for ix in range(x_start, x_end):
        for iy in range(y_start, y_end):
            nit = 0
            z = complex(ix / size * xwidth + xmin, iy / size * yheight + ymin)
            while abs(z) <= zabs_max and nit < nit_max:
                z = z**2 + c
                nit += 1
            ratio = nit / nit_max

            julia_patch[ix - x_start, iy - y_start] = ratio

    return julia_patch


def parallel_julia(size, xmin, xmax, ymin, ymax, patch, nprocs, c):
    task_list = []
    for x in range(0, size, patch):
        for y in range(0, size, patch):
            x_start = x
            x_end = min(x + patch, size)
            y_start = y
            y_end = min(y + patch, size)
            task_list.append((xmin, xmax, ymin, ymax, x_start, x_end, y_start, y_end, size, c))

    with Pool(nprocs) as pool:
        completed_patches = pool.starmap(patch_sequential_julia, task_list, chunksize=1)

    julia = np.zeros((size, size))
    for i, patch in enumerate(completed_patches):
        x_start = task_list[i][4]
        x_end = task_list[i][5]
        y_start = task_list[i][6]
        y_end = task_list[i][7]
        julia[x_start:x_end, y_start:y_end] = patch

    return julia


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

    # pick julia set type
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

    # benchmark time
    stime = time.perf_counter()
    julia_img = parallel_julia(args.size, args.xmin, args.xmax, args.ymin, args.ymax, args.patch, args.nprocs, c)
    rtime = time.perf_counter() - stime
    print(f"{args.size};{args.patch};{args.nprocs};{rtime}")

    # validate correctness
    seq_stime = time.perf_counter()
    seq = sequential_julia(args.xmin, args.xmax, args.ymin, args.ymax, args.size, c)
    seq_rtime = time.perf_counter() - seq_stime
    assert np.allclose(julia_img, seq), "parallel implementation is incorrect"

    # visualize
    if args.o is not None:
        import matplotlib
        import matplotlib.pyplot as plt
        import matplotlib.cm as cm

        matplotlib.use("agg")
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
        plt.savefig(args.o, bbox_inches="tight")
        # plt.show()
