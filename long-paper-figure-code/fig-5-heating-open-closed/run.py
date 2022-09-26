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


def closed_run(config):
    pass


def open_run(config):
    check_sc()

    os.chdir("open")
    # Read config
    with open("config.toml", "rb") as f:
        sc_config = tomli.load(f)

    sc_config["hsize"] = config["L"]
    sc_config["ssize"] = config["l"]

    # Write new config
    with open("config.toml", "wb") as f:
        tomli_w.dump(sc_config, f)

    os.chdir("..")
    pass


def plot(config):
    # Generate plot
    os.system("gnuplot plot-dj-oc.gp")
    os.system("pdflatex fig-5-heating-open-closed.tex")
    os.remove("fig-5-heating-open-closed.aux")
    os.remove("fig-5-heating-open-closed.log")
    os.remove("fig-5-heating-open-closed.tex")
    os.remove("fig-5-heating-open-closed-inc.eps")
    os.remove("fig-5-heating-open-closed-inc-eps-converted-to.pdf")
    pass


if __name__ == "__main__":

    with open("figure.toml", "rb") as f:
        figure_config = tomli.load(f)
    l = figure_config["l"]
    L = figure_config["L"]

    print(
        "\x1b[0;32mGenerate data and plots for Fig. 5 (heating in open and closed systems)\x1b[0m"
    )
    print("1) Generate closed curves \x1b[0;31mWILL OVERWRITE PREVIOUS DATA\x1b[0m")
    print("2) Generate open curves \x1b[0;31mWILL OVERWRITE PREVIOUS DATA\x1b[0m")
    print("3) Produce plots (requires gnuplot and pdflatex)")

    option = input()

    switch = {"1": closed_run, "2": open_run, "3": plot}
    while option not in switch.keys():
        option = input("Invalid option, please try again: ")

    switch.get(option)(figure_config)
