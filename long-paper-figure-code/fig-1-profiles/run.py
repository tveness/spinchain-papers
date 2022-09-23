#!/usr/bin/env python
import tomli, tomli_w
import shutil
import glob
import os
import glob
import stat
from math import pi


def check_sc():
    name = "sc"
    if shutil.which(name) is None:
        raise Exception(
            name
            + " is not in PATH, cannot generate data without this, please follow main repository README and include sc in your path"
        )


def run_fast(config):
    check_sc()
    # Change directory
    os.chdir("dyn-big-fast")
    # Generate config
    conf = {
        "hsize": config["hsize"],
        "ssize": config["ssize"],
        "t": config["tau_fast "] * 4000.0,
        "dt": config["dt"],
        "runs": config["runs"],
        "trel": config["trel"],
        "threads": config["threads"],
        "tau": config["tau_fast"],
        "lambda": config["lambda"],
        "hfield": config["hfield"],
        "hs": config["hs"],
        "jvar": config["jvar"],
        "hvar": config["hvar"],
        "method": config["method"],
        "ednsty": config["ednsty"],
        "file": config["file"],
        "strob": config["strob"],
        "offset": config["offset"],
        "beta": config["beta"],
        "mc_points": config["mc_points"],
        "e": config["e"],
        "drive": config["drive"],
        "log": config["log"],
    }

    with open("config.toml", "wb") as f:
        tomli_w.dump(conf, f)

    # Run
    os.system("sc -P")
    os.chdir("..")

    pass


def run_slow(config):
    check_sc()
    # Change directory
    os.chdir("dyn-big-slow")
    # Generate config
    conf = {
        "hsize": config["hsize"],
        "ssize": config["ssize"],
        "t": config["tau_slow "] * 4000.0,
        "dt": config["dt"],
        "runs": config["runs"],
        "trel": config["trel"],
        "threads": config["threads"],
        "tau": config["tau_slow"],
        "lambda": config["lambda"],
        "hfield": config["hfield"],
        "hs": config["hs"],
        "jvar": config["jvar"],
        "hvar": config["hvar"],
        "method": config["method"],
        "ednsty": config["ednsty"],
        "file": config["file"],
        "strob": config["strob"],
        "offset": config["offset"],
        "beta": config["beta"],
        "mc_points": config["mc_points"],
        "e": config["e"],
        "drive": config["drive"],
        "log": config["log"],
    }

    with open("config.toml", "wb") as f:
        tomli_w.dump(conf, f)

    # Run
    os.system("sc -P")
    os.chdir("..")

    pass


def mc_slow(config):
    check_sc()
    # Change directory
    os.chdir("profile-mc-slow")
    # Generate config

    om = 2 * pi / config["tau_slow"]
    hfield = [1.0, 0.0, 0.0]
    hs = [0.0, 0.0, -om]
    conf = {
        "hsize": config["hsize"],
        "ssize": config["ssize"],
        "t": config["tau_slow "] * 4000.0,
        "dt": config["dt"],
        "runs": config["runs"],
        "trel": config["trel"],
        "threads": config["threads"],
        "tau": config["tau_slow"],
        "lambda": config["lambda"],
        "hfield": hfield,
        "hs": hs,
        "jvar": config["jvar"],
        "hvar": config["hvar"],
        "method": config["method"],
        "ednsty": config["ednsty"],
        "file": config["file"],
        "strob": config["strob"],
        "offset": config["offset"],
        "beta": config["beta"],
        "mc_points": config["mc_points"],
        "e": config["e"],
        "drive": "staticfield",
        "log": config["log"],
    }

    with open("config.toml", "wb") as f:
        tomli_w.dump(conf, f)

    # Run
    os.system("sc -p")
    os.chdir("..")

    pass


def mc_fast(config):
    check_sc()
    # Change directory
    os.chdir("profile-mc-fast")
    # Generate config

    om = 2 * pi / config["tau_fast"]
    hs = [0.0, 0.0, -1 / (2.0 * om)]
    conf = {
        "hsize": config["hsize"],
        "ssize": config["ssize"],
        "t": config["tau_fast "] * 4000.0,
        "dt": config["dt"],
        "runs": config["runs"],
        "trel": config["trel"],
        "threads": config["threads"],
        "tau": config["tau_fast"],
        "lambda": config["lambda"],
        "hfield": config["hfield"],
        "hs": hs,
        "jvar": config["jvar"],
        "hvar": config["hvar"],
        "method": config["method"],
        "ednsty": config["ednsty"],
        "file": config["file"],
        "strob": config["strob"],
        "offset": config["offset"],
        "beta": config["beta"],
        "mc_points": config["mc_points"],
        "e": config["e"],
        "drive": "staticfield",
        "log": config["log"],
    }

    with open("config.toml", "wb") as f:
        tomli_w.dump(conf, f)

    # Run
    os.system("sc -p")
    os.chdir("..")

    pass


def plot(config):
    # Change directory
    os.chdir("plot-files")

    # Generate plot
    os.system("gnuplot plot_sz_comp.gp")
    os.system("pdflatex fig-1-profile-comparison.tex")

    pass


if __name__ == "__main__":

    with open("figure.toml", "rb") as f:
        figure_config = tomli.load(f)

    print("\x1b[0;32mGenerate data and plots for Fig. 1 (profiles)\x1b[0m")
    print(
        "1) Generate data for fast dynamical profile \x1b[0;31mWILL DELETE DATA FROM RUNS\x1b[0m"
    )
    print(
        "2) Generate data for slow dynamical profile \x1b[0;31mWILL DELETE DATA FROM RUNS\x1b[0m"
    )
    print(
        "3) Generate data for fast MC profile \x1b[0;31mWILL DELETE DATA FROM RUNS\x1b[0m"
    )
    print(
        "4) Generate data for slow MC profile \x1b[0;31mWILL DELETE DATA FROM RUNS\x1b[0m"
    )
    print("5) Produce plots (requires gnuplot and pdflatex)")

    option = input()

    switch = {"1": run_fast, "2": run_slow, "3": mc_fast, "4": mc_slow, "5": plot}
    while option not in switch.keys():
        option = input("Invalid option, please try again: ")

    switch.get(option)(figure_config)
