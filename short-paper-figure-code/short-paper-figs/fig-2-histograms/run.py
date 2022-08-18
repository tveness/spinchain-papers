#!/usr/bin/env python
import tomli, tomli_w
import shutil
import os
import glob
import stat
import math
from math import pi


with open("sc-default-config.toml", "rb") as f:
    sc_default_config = tomli.load(f)


def check_sc():
    name = "sc"
    if shutil.which(name) is None:
        raise Exception(
            name
            + " is not in PATH, cannot generate data without this, please follow main repository README and include sc in your path"
        )


def run_all():
    run_hf_dyn()
    run_hf_mc()
    run_lf_dyn()
    run_lf_mc()


def run_hf_dyn():
    check_sc()
    print("\x1b[0;32mRunning high frequency dynamics\x1b[0m")
    with open("run-params.toml", "rb") as f:
        params = tomli.load(f)
    l = params["l"]
    L = params["L"]
    tau = params["tau_hf"]

    with open("sc-default-config.toml", "rb") as f:
        sc_config = tomli.load(f)
    sc_config["l"] = l
    sc_config["L"] = L
    sc_config["tau"] = tau
    sc_config["t"] = 10000 * tau

    # For this high frequency regime, we run a number of large simulations, and then take many trajectory samples after equilibration, similar to the single trajetory

    sc_config["runs"] = 36

    # Change dir
    os.chdir("hf-dyn")
    # Write config
    print("\x1b[0;32mWriting config\x1b[0m")
    with open("config.toml", "wb") as f:
        tomli_w.dump(sc_config, f)
    # Run sc
    print("\x1b[0;32mRunning simulations\x1b[0m")
    print(f"\x1b[0;32mExecuting:\x1b[0m sc")
    os.system("sc")

    print("\x1b[0;32mCollating data\x1b[0m")
    # Collate
    with open("dyn.dat", "w") as f:
        for name in glob.glob("log*.dat"):
            with open(name, "r") as g:
                for i, line in enumerate(g.readlines()):
                    if i > 5000:
                        f.write(line)
            os.remove(name)

    print("\x1b[0;32mCleaning log data\x1b[0m")

    os.chdir("..")
    print("\x1b[0;32mDone\x1b[0m")


def run_lf_dyn():
    check_sc()
    print("\x1b[0;32mRunning low frequency dynamics\x1b[0m")
    with open("run-params.toml", "rb") as f:
        params = tomli.load(f)
    l = params["l"]
    L = params["L"]
    tau = params["tau_lf"]
    samples = params["dyn_samples"]

    with open("sc-default-config.toml", "rb") as f:
        sc_config = tomli.load(f)
    sc_config["l"] = l
    sc_config["L"] = L
    sc_config["tau"] = tau
    sc_config["t"] = 1000 * tau

    # Max number of files open is 1000
    loops = 1 + (samples // 1000)
    runs = samples // loops

    sc_config["runs"] = runs

    # Change dir
    os.chdir("lf-dyn")
    # Write config
    print("\x1b[0;32mWriting config\x1b[0m")
    with open("config.toml", "wb") as f:
        tomli_w.dump(sc_config, f)
    # Run sc
    print("\x1b[0;32mRunning simulations\x1b[0m")
    for l in range(loops):
        print(f"\x1b[0;32mExecuting {l+1} of {loops}:\x1b[0m sc")

        os.system("sc")

        print("\x1b[0;32mCollating data\x1b[0m")
        # Collate, by writing only last line
        with open("dyn-samples.dat", "a") as f:
            for name in glob.glob("log*.dat"):
                with open(name, "r") as g:
                    for line in g:
                        pass
                    f.write(line)
                os.remove(name)

        print("\x1b[0;32mCleaned log data\x1b[0m")

    os.chdir("..")

    print("\x1b[0;32mDone\x1b[0m")


def run_hf_mc():
    check_sc()
    print("\x1b[0;32mRunning high frequency MC\x1b[0m")

    with open("run-params.toml", "rb") as f:
        params = tomli.load(f)
    l = params["l"]
    L = params["L"]
    tau = params["tau_hf"]
    samples = params["mc_samples"]

    with open("sc-default-config.toml", "rb") as f:
        sc_config = tomli.load(f)
    sc_config["l"] = l
    sc_config["L"] = L
    sc_config["tau"] = tau
    omega = 2.0 * pi / tau
    sc_config["hs"] = [0.0, 0.0, -1.0 / (2.0 * omega)]
    sc_config["mc_points"] = samples

    # Change dir
    os.chdir("hf-mc")
    # Write config
    with open("config.toml", "wb") as f:
        tomli_w.dump(sc_config, f)
    # Run sc
    print("\x1b[0;32mRunning simulations\x1b[0m")
    # Clear file
    with open("mc_live.dat", "w") as f:
        pass
    print(f"\x1b[0;32mExecuting:\x1b[0m sc -m")
    os.system("sc -m")
    os.chdir("..")
    print("\x1b[0;32mDone\x1b[0m")


def run_lf_mc():
    check_sc()
    print("\x1b[0;32mRunning low frequency MC\x1b[0m")

    with open("run-params.toml", "rb") as f:
        params = tomli.load(f)
    l = params["l"]
    L = params["L"]
    tau = params["tau_lf"]
    samples = params["mc_samples"]

    with open("sc-default-config.toml", "rb") as f:
        sc_config = tomli.load(f)
    sc_config["l"] = l
    sc_config["L"] = L
    sc_config["tau"] = tau
    sc_config["t"] = 10000 * tau
    omega = 2.0 * pi / tau
    sc_config["hs"] = [1.0, 0.0, 0.0]
    sc_config["hfield"] = [0.0, 0.0, -omega]
    sc_config["mc_points"] = samples

    # Change dir
    os.chdir("lf-mc")

    # Determine beta_rot_stat for this case
    print("\x1b[0;32mGetting beta_rot^stat\x1b[0m")
    beta_rot_stat = get_beta_rot(sc_config)

    print(f"\x1b[0;32mbeta_rot^stat: {beta_rot_stat}\x1b[0m")
    ed = 1.0 / beta_rot_stat - 1.0 / math.tanh(beta_rot_stat)
    sc_config["ednsty"] = ed
    print(f"\x1b[0;32me: {ed}\x1b[0m")

    # Make sure these are set to correct values again afterwards
    sc_config["hs"] = [1.0, 0.0, 0.0]
    sc_config["hfield"] = [0.0, 0.0, -omega]

    # Write config
    with open("config.toml", "wb") as f:
        tomli_w.dump(sc_config, f)
    # Run sc
    print("\x1b[0;32mRunning simulations\x1b[0m")
    # Clear file
    with open("mc_live.dat", "w") as f:
        pass
    print("\x1b[0;32mExecuting:\x1b[0m sc -m")
    os.system("sc -m")
    print("\x1b[0;32mCleaning up log files\x1b[0m")
    for log_name in glob.glob("log*.dat"):
        os.remove(log_name)
    print("\x1b[0;32mDone\x1b[0m")


def get_beta_rot(config):
    config["hs"] = [0.0, 0.0, 0.0]
    config["hfield"] = [0.0, 0.0, 0.0]
    with open("config.toml", "wb") as f:
        tomli_w.dump(config, f)
    ed = config["ednsty"]
    print(f"\x1b[0;32mExecuting:\x1b[0m sc --rot-frame {ed}")
    os.system(f"sc --rot-frame {ed}")
    # Now find final line in betat-rot.dat
    with open("betat-rot.dat") as f:
        for line in f:
            pass
        last_line = line
        beta = float(line.split(" ")[2])
    return beta


def control_mc():
    check_sc()
    print("\x1b[0;32mRunning high frequency MC\x1b[0m")

    with open("run-params.toml", "rb") as f:
        params = tomli.load(f)
    l = params["l"]
    L = params["L"]
    samples = params["mc_samples"]

    with open("sc-default-config.toml", "rb") as f:
        sc_config = tomli.load(f)
    sc_config["l"] = l
    sc_config["L"] = L
    sc_config["hs"] = [0.0, 0.0, 0.0]
    sc_config["hfield"] = [0.0, 0.0, 0.0]
    sc_config["mc_points"] = samples

    # This is crucial and also tau-dependent: would be good to automate this, as this is a value that comes from the statistical procedure as outline in the paper

    # Change dir
    os.chdir("control-mc")
    # Write config
    with open("config.toml", "wb") as f:
        tomli_w.dump(sc_config, f)
    # Run sc
    print("\x1b[0;32mRunning simulations\x1b[0m")
    # Clear file
    with open("mc_live.dat", "w") as f:
        pass
    print(f"\x1b[0;32mExecuting:\x1b[0m sc -m")
    os.system("sc -m")
    print("\x1b[0;32mDone\x1b[0m")


def plot():
    print("\x1b[0;32mPlotting data\x1b[0m")
    os.chdir("plot-files")
    print(f"\x1b[0;32mExecuting:\x1b[0m gnuplot plot-hist.gp")
    os.system("gnuplot plot-hist.gp")
    print(f"\x1b[0;32mExecuting:\x1b[0m pdflatex fig.tex")
    os.system("pdflatex fig.tex")
    shutil.copy("fig.pdf", "../fig-2-hist.pdf")

    print("\x1b[0;32mPlot available at fig-2-hist.pdf\x1b[0m")


if __name__ == "__main__":
    print("\x1b[0;32mGenerate data and plots for Fig. 1\x1b[0m")
    print("1) Run all \x1b[0;31mWILL DELETE DATA FROM RUNS\x1b[0m")
    print("2) Run HF dynamics \x1b[0;31mWILL DELETE DATA FROM RUNS\x1b[0m")
    print("3) Run HF Monte Carlo \x1b[0;31mWILL DELETE DATA FROM RUNS\x1b[0m")
    print("4) Run LF dynamics \x1b[0;31mWILL DELETE DATA FROM RUNS\x1b[0m")
    print("5) Run LF Monte Carlo \x1b[0;31mWILL DELETE DATA FROM RUNS\x1b[0m")
    print("6) Run control Monte Carlo \x1b[0;31mWILL DELETE DATA FROM RUNS\x1b[0m")
    print("7) Produce plots (requires gnuplot and pdflatex)")
    option = input()

    switch = {
        "1": run_all,
        "2": run_hf_dyn,
        "3": run_hf_mc,
        "4": run_lf_dyn,
        "5": run_lf_mc,
        "6": control_mc,
        "7": plot,
    }
    while option not in switch.keys():
        option = input("Invalid option, please try again: ")

    switch.get(option)()
