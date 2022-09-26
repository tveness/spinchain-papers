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


def run_5(config):
    check_sc()

    os.chdir("t-5.0")

    os.rm("betat-rot.dat")
    print("Sweeping e")

    for et in np.arange(-0.66, -0.5, 0.01):
        print(f"Fitting for e: {et}")
        os.system(f"sc --rot-frame {et}")

    print("Running dynamical simulations")
    # Read config
    with open("config.toml", "rb") as f:
        sc_config = tomli.load(f)

    sc_config["hsize"] = config["L"]
    sc_config["ssize"] = config["l"]
    sc_config["tau"] = 5.0
    sc_config["t"] = 20000 * sc_config["tau"]

    # Write new config
    with open("config.toml", "wb") as f:
        tomli_w.dump(sc_config, f)

    os.system("sc")
    os.system("sc -a")
    os.system("rm log*.dat")

    pass


def run_10(config):
    check_sc()

    os.chdir("t-10.0")

    os.rm("betat-rot.dat")
    print("Sweeping e")

    for et in np.arange(-0.66, -0.5, 0.01):
        print(f"Fitting for e: {et}")
        os.system(f"sc --rot-frame {et}")

    print("Running dynamical simulations")
    # Read config
    with open("config.toml", "rb") as f:
        sc_config = tomli.load(f)

    sc_config["hsize"] = config["L"]
    sc_config["ssize"] = config["l"]
    sc_config["tau"] = 10.0
    sc_config["t"] = 20000 * sc_config["tau"]

    # Write new config
    with open("config.toml", "wb") as f:
        tomli_w.dump(sc_config, f)

    os.system("sc")
    os.system("sc -a")
    os.system("rm log*.dat")

    pass


def plot(config):
    # Generate plot
    os.chdir("t-5.0")
    os.system("gnuplot plot-drift.gp")
    os.system("pdflatex fig-9-drift-tau-5.0.tex")
    os.remove("fig-9-drift-tau-5.0.aux")
    os.remove("fig-9-drift-tau-5.0.log")
    os.remove("fig-9-drift-tau-5.0.tex")
    os.remove("fig-9-drift-tau-5.0-inc.eps")
    os.remove("fig-9-drift-tau-5.0-inc-eps-converted-to.pdf")
    os.chdir("..")

    os.chdir("t-10.0")
    os.system("gnuplot plot-drift.gp")
    os.system("pdflatex fig-9-drift-tau-10.0.tex")
    os.remove("fig-9-drift-tau-10.0.aux")
    os.remove("fig-9-drift-tau-10.0.log")
    os.remove("fig-9-drift-tau-10.0.tex")
    os.remove("fig-9-drift-tau-10.0-inc.eps")
    os.remove("fig-9-drift-tau-10.0-inc-eps-converted-to.pdf")
    os.chdir("..")
    pass


if __name__ == "__main__":

    with open("figure.toml", "rb") as f:
        figure_config = tomli.load(f)
    l = figure_config["l"]
    L = figure_config["L"]

    print("\x1b[0;32mGenerate data and plots for Fig. 9 (drifts)\x1b[0m")
    print(
        "1) Generate data for tau = 5.0 \x1b[0;31mWILL OVERWRITE PREVIOUS DATA\x1b[0m"
    )
    print(
        "2) Generate data for tau = 10.0 \x1b[0;31mWILL OVERWRITE PREVIOUS DATA\x1b[0m"
    )
    print("3) Produce plot (requires gnuplot and pdflatex)")

    option = input()

    switch = {"1": run_5, "2": run_10, "3": plot}
    while option not in switch.keys():
        option = input("Invalid option, please try again: ")

    switch.get(option)(figure_config)
