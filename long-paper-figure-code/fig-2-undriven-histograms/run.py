#!/usr/bin/env python
import tomli, tomli_w
import shutil
import glob
import os
import glob
import stat
import analyticcurve
import numpy as np
from math import pi


def check_sc():
    name = "sc"
    if shutil.which(name) is None:
        raise Exception(
            name
            + " is not in PATH, cannot generate data without this, please follow main repository README and include sc in your path"
        )

def analytic(config):
    print("l: ",config["l"])
    e_arr,p_arr = analyticcurve.gen_data(ell = config["l"]-1)
    ep = list(zip(e_arr,p_arr))

    np.savetxt("analytic-hist.dat",ep)
    pass

def generate_samples(config):
    check_sc()

    # Read config
    with open("config.toml","rb") as f:
        sc_config = tomli.load(f)
    sc_config["hsize"] = config["L"]
    sc_config["ssize"] = config["l"]
    sc_config["mc_points"] = config["points"]

    # Write new config

    with open("config.toml","wb") as f:
        tomli_w.dump(sc_config, f)


    os.system("sc --histogram "+str(config["points"]) )
    pass


def plot(config):
    # Generate plot
    os.system("gnuplot plot_hist_agg.gp")
    os.system("pdflatex fig-2-undriven-histograms.tex")
    pass


if __name__ == "__main__":

    with open("figure.toml", "rb") as f:
        figure_config = tomli.load(f)
    l = figure_config["l"]
    L = figure_config["L"]

    print("\x1b[0;32mGenerate data and plots for Fig. 2 (finite-size histograms for undriven system)\x1b[0m")
    print(
        "1) Generate analytic curve \x1b[0;31mWILL DELETE DATA FROM RUNS\x1b[0m"
    )
    print(
        "2) Generate dynamical and MC samples \x1b[0;31mWILL DELETE DATA FROM RUNS\x1b[0m"
    )
    print("3) Produce plots (requires gnuplot and pdflatex)")

    option = input()

    switch = {"1": analytic, "2": generate_samples, "3": plot}
    while option not in switch.keys():
        option = input("Invalid option, please try again: ")

    switch.get(option)(figure_config)
