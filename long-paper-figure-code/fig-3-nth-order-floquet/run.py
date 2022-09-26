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


def dyn(config):
    check_sc()

    os.chdir("dyn")
    # Read config
    with open("config.toml", "rb") as f:
        sc_config = tomli.load(f)

    sc_config["hsize"] = config["L"]
    sc_config["ssize"] = config["l"]
    sc_config["mc_points"] = config["points"]
    sc_config["tau"] = config["tau"]
    sc_config["t"] = 10000 * config["tau"]

    # Write new config
    with open("config.toml", "wb") as f:
        tomli_w.dump(sc_config, f)

    os.remove("dyn.dat")
    os.system("run.sh")
    os.chdir("..")
    pass


def mc_control(config):
    check_sc()

    os.chdir("mc-control")

    # Read config
    with open("config.toml", "rb") as f:
        sc_config = tomli.load(f)

    # For Monte Carlo simulation L=l
    sc_config["hsize"] = config["l"]
    sc_config["ssize"] = config["l"]
    sc_config["tau"] = config["tau"]
    sc_config["mc_points"] = config["mc_points"]

    # Write new config
    with open("config.toml", "wb") as f:
        tomli_w.dump(sc_config, f)

    os.remove("mc_live.dat")
    os.system("sc -m")
    os.chdir("..")
    pass


def mc(config):
    check_sc()

    os.chdir("mc")
    # Read config
    with open("config.toml", "rb") as f:
        sc_config = tomli.load(f)

    # For Monte Carlo simulation L=l
    sc_config["hsize"] = config["l"]
    sc_config["ssize"] = config["l"]

    sc_config["tau"] = config["tau"]
    omega = 2 * pi / config["tau"]
    sc_config["hfield"] = [0.0, 0.0, -omega]
    sc_config["hs"] = [1.0, 0.0, 0.0]

    sc_config["mc_points"] = config["mc_points"]

    # Write new config
    with open("config.toml", "wb") as f:
        tomli_w.dump(sc_config, f)

    os.remove("mc_live.dat")
    os.system("sc -m")
    os.chdir("..")
    pass


def plot(config):
    # Generate plot
    os.system("gnuplot plot_hist_fig.gp")
    os.system("pdflatex fig-4-low-frequency-histograms.tex")
    os.remove("fig-4-low-frequency-histograms.aux")
    os.remove("fig-4-low-frequency-histograms.log")
    os.remove("fig-4-low-frequency-histograms.tex")
    os.remove("fig-4-low-frequency-histograms-inc.eps")
    os.remove("fig-4-low-frequency-histograms-inc-eps-converted-to.pdf")
    pass


if __name__ == "__main__":

    with open("figure.toml", "rb") as f:
        figure_config = tomli.load(f)
    l = figure_config["l"]
    L = figure_config["L"]

    print(
        "\x1b[0;32mGenerate data and plots for Fig. 3 (histograms at high frequencies, compared with Floquet-Magnus results)\x1b[0m"
    )
    print(
        "1) Generate dynamics histogram \x1b[0;31mWILL OVERWRITE PREVIOUS DATA\x1b[0m"
    )
    print(
        "2) Generate MC histogram (control P_0) \x1b[0;31mWILL OVERWRITE PREVIOUS DATA\x1b[0m"
    )
    print(
        "3) Generate MC histogram, P_rot \x1b[0;31mWILL OVERWRITE PREVIOUS DATA\x1b[0m"
    )
    print("4) Produce plots (requires gnuplot and pdflatex)")

    option = input()

    switch = {"1": dyn, "2": mc_control, "3": mc, "4": plot}
    while option not in switch.keys():
        option = input("Invalid option, please try again: ")

    switch.get(option)(figure_config)
