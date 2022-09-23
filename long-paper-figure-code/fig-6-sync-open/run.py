#!/usr/bin/env python
import tomli, tomli_w
import shutil
import glob
import os
import glob
import stat
import numpy as np
from math import pi


def check_sc():
    name = "sc"
    if shutil.which(name) is None:
        raise Exception(
            name
            + " is not in PATH, cannot generate data without this, please follow main repository README and include sc in your path"
        )


def run(config):
    check_sc()

    # Read config
    with open("config.toml", "rb") as f:
        sc_config = tomli.load(f)

    sc_config["hsize"] = config["L"]
    sc_config["ssize"] = config["l"]
    sc_config["tau"] = config["tau"]
    sc_config["t"] = 200 * config["tau"]

    # Write new config
    with open("config.toml", "wb") as f:
        tomli_w.dump(sc_config, f)

    os.system("sc")
    os.system("sc -a")
    os.system("rm log*.dat")
    os.rename("avg.dat", "open-sync-avg.dat")

    pass


def plot(config):
    # Generate plot
    os.system("gnuplot plot-sync-open.gp")
    os.system("pdflatex fig-6-sync-open.tex")
    os.remove("fig-6-sync-open.aux")
    os.remove("fig-6-sync-open.log")
    os.remove("fig-6-sync-open.tex")
    os.remove("fig-6-sync-open-inc.eps")
    os.remove("fig-6-sync-open-inc-eps-converted-to.pdf")
    pass


if __name__ == "__main__":

    with open("figure.toml", "rb") as f:
        figure_config = tomli.load(f)
    l = figure_config["l"]
    L = figure_config["L"]

    print(
        "\x1b[0;32mGenerate data and plots for Fig. 2 (finite-size histograms for undriven system)\x1b[0m"
    )
    print("1) Generate data \x1b[0;31mWILL OVERWRITE PREVIOUS DATA\x1b[0m")
    print("2) Produce plot (requires gnuplot and pdflatex)")

    option = input()

    switch = {"1": run, "2": plot}
    while option not in switch.keys():
        option = input("Invalid option, please try again: ")

    switch.get(option)(figure_config)
