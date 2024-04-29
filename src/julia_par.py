from re import U
import numpy as np
import argparse
import time
import math
from multiprocessing import Pool, TimeoutError


CURVE_START = 48 / 64 * math.pi
CURVE_END = 60 / 64 * math.pi
CURVE_SPAN = CURVE_END - CURVE_START
CURVE_SCALE = 0.755


# Update according to your group size and number (see TUWEL)
# GROUP_SIZE = None
# GROUP_NUMBER = None
GROUP_SIZE = 2
GROUP_NUMBER = 13

# do not modify BENCHMARK_C
BENCHMARK_C = complex(-0.2, -0.65)


def c_from_group(group_size: int, group_number: int):
    if group_size is None or group_number is None:
        raise Exception("Please provide your group size and number " + "to the GROUP_SIZE and GROUP_NUMBER variables.")

    # argument checking
    if group_size < 1 or group_size > 2:
        raise Exception("Group size must be either 1 or 2")

    if group_number < 1 or group_number > 30:
        raise Exception("Group number must be between 1 and 30")

    if group_size == 1:
        num_groups = 20
        if group_number > num_groups:
            raise Exception("Group number must be <=20 for 1 person groups")
        phi = 2 * math.pi - CURVE_END + group_number / (num_groups - 1) * CURVE_SPAN
    elif group_size == 2:
        num_groups = 30
        phi = CURVE_END - group_number / (num_groups - 1) * CURVE_SPAN

    return CURVE_SCALE * math.e ** (phi * 1j)


def compute_julia_set_sequential(xmin, xmax, ymin, ymax, im_width, im_height, c):

    zabs_max = 10
    nit_max = 300

    xwidth = xmax - xmin
    yheight = ymax - ymin

    julia = np.zeros((im_width, im_height))
    for ix in range(im_width):
        for iy in range(im_height):
            nit = 0
            # Map pixel position to a point in the complex plane
            z = complex(ix / im_width * xwidth + xmin, iy / im_height * yheight + ymin)
            # Do the iterations
            while abs(z) <= zabs_max and nit < nit_max:
                z = z**2 + c
                nit += 1
            ratio = nit / nit_max
            julia[ix, iy] = ratio

    return julia


def compute_julia_in_parallel(size, xmin, xmax, ymin, ymax, patch, nprocs, c):

    # replace the following code
    # with a parallel version
    julia_img = compute_julia_set_sequential(xmin, xmax, ymin, ymax, size, size, c)

    return julia_img


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", help="image size in pixels (square images)", type=int, default=500)
    parser.add_argument("--xmin", help="", type=float, default=-1.5)
    parser.add_argument("--xmax", help="", type=float, default=1.5)
    parser.add_argument("--ymin", help="", type=float, default=-1.5)
    parser.add_argument("--ymax", help="", type=float, default=1.5)
    parser.add_argument("--group-size", help="", type=int, default=None)
    parser.add_argument("--group-number", help="", type=int, default=None)
    parser.add_argument("--patch", help="patch size in pixels (square images)", type=int, default=20)
    parser.add_argument("--nprocs", help="number of workers", type=int, default=1)
    parser.add_argument("--draw-axes", help="Whether to draw axes", action="store_true")
    parser.add_argument("-o", help="output file")
    parser.add_argument("--benchmark", help="Whether to execute the script with the benchmark Julia set", action="store_true")
    args = parser.parse_args()

    # print(args)
    if args.group_size is not None:
        GROUP_SIZE = args.group_size
    if args.group_number is not None:
        GROUP_NUMBER = args.group_number

    # assign c based on mode
    c = None
    if args.benchmark:
        c = BENCHMARK_C
    else:
        c = c_from_group(GROUP_SIZE, GROUP_NUMBER)

    stime = time.perf_counter()
    julia_img = compute_julia_in_parallel(args.size, args.xmin, args.xmax, args.ymin, args.ymax, args.patch, args.nprocs, c)
    rtime = time.perf_counter() - stime

    print(f"{args.size};{args.patch};{args.nprocs};{rtime}")

    if not args.o is None:
        import matplotlib

        matplotlib.use("agg")
        import matplotlib.pyplot as plt
        import matplotlib.cm as cm

        fig, ax = plt.subplots()
        ax.imshow(julia_img, interpolation="nearest", cmap=plt.get_cmap("hot"))

        if args.draw_axes:
            # set labels correctly
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
            # disable axes
            ax.axis("off")

        plt.tight_layout()
        plt.savefig(args.o, bbox_inches="tight")
        # plt.show()
