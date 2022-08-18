#!/usr/bin/env python
import tomli, tomli_w
import shutil
import glob
import os
import glob
import stat


with open("sc-default-config.toml", "rb") as f:
    sc_default_config = tomli.load(f)


def check_sc():
    name = "sc"
    if shutil.which(name) is None:
        raise Exception(
            name
            + " is not in PATH, cannot generate data without this, please follow main repository README and include sc in your path"
        )


def init():
    check_sc()
    with open("run-params.toml", "rb") as f:
        params = tomli.load(f)
    l = params["l"]
    L = params["L"]
    avg = params["avg"]
    taus = params["taus"]
    with open("sc-default-config.toml", "rb") as f:
        sc_config = tomli.load(f)
    return [l, L, taus, avg, sc_config]


def run_dyn():
    # This is very similar to run() of fig-1-heating's open system
    # The main differences are: 1. dj=1e-3 instead of 2e-2
    #                           2. only run for 1000 cycles

    [l, L, taus, avg, sc_config] = init()

    print("\x1b[0;32mGenerating dynamic curve\x1b[0m")
    # Change dir
    os.chdir("dyn-curve")

    # Need to determine the number of loops
    loops = 1 + avg // 1000

    runs = avg // loops

    print("\x1b[0;32mGenerating scripts for closed system\x1b[0m")
    # First, generate the script to run everything
    with open("runs.sh", "w") as f:
        f.write("#!/usr/bin/bash\n\n")
        f.write("for tau in {")
        for tau in taus:
            f.write(f"{tau}")
            if tau != taus[-1]:
                f.write(",")
        f.write("}\n")
        f.write("do\n")
        f.write("   for j in {1..")
        f.write(f"{loops}")
        f.write("}\n")
        f.write("   do\n")
        f.write("      cd t-$tau\n")
        f.write("      sc\n")
        f.write("      sc -a\n")
        f.write("      rm log*\n")
        f.write("      cd ..\n")
        f.write("   done\n")
        f.write("done")

    st = os.stat("runs.sh")
    os.chmod("runs.sh", st.st_mode | stat.S_IEXEC)
    sc_config["l"] = l
    sc_config["L"] = L
    sc_config["runs"] = runs

    # Now create the directories and each associate config file
    for tau in taus:
        # Clear old directories
        dirname = "t-" + str(tau)
        try:
            shutil.rmtree(dirname)
        except FileNotFoundError:
            pass
        os.mkdir(dirname)
        sc_config["tau"] = tau
        # Total run time is determined by largest number of cycles
        sc_config["t"] = 1000 * tau

        # Write config file
        with open("t-" + str(tau) + "/config.toml", "wb") as f:
            tomli_w.dump(sc_config, f)

    print("\x1b[0;32mRunning dynamic simulations\x1b[0m")
    print("\x1b[0;32mExecuting:\x1b[0m bash runs.sh")
    os.system("bash runs.sh")

    print("\x1b[0;32mProcessing results\x1b[0m")

    # First clear all of the data
    for datfile in glob.glob("*cycles.dat"):
        os.remove(datfile)

    with open("1000-cycles.dat", "w") as f:
        for tau in taus:
            t_file = "t-" + str(tau) + "/avg.dat"
            with open(t_file, "r") as g:
                for line in g.readlines():
                    pass
                f.write(line)
    print("\x1b[0;32mDone\x1b[0m")


def run_PF():
    [l, L, taus, avg, sc_config] = init()

    print("\x1b[0;32mGenerating P_F curve\x1b[0m")
    os.chdir("pf-curve")

    for tau in taus:
        sc_config["tau"] = tau
        with open("config.toml", "wb") as f:
            tomli_w.dump(sc_config, f)
        ed = sc_config["ednsty"]
        print(f"\x1b[0;32mExecuting:\x1b[0m sc --high-freq {ed} --tau {tau}")
        os.system(f"sc --high-freq {ed} --tau {tau}")


def run_PRF():
    [l, L, taus, avg, sc_config] = init()

    print("\x1b[0;32mGenerating P_RF curve\x1b[0m")
    os.chdir("prf-curve")

    for tau in taus:
        sc_config["tau"] = tau
        with open("config.toml", "wb") as f:
            tomli_w.dump(sc_config, f)
        ed = sc_config["ednsty"]
        print(f"\x1b[0;32mExecuting:\x1b[0m sc --rot-frame {ed} --tau {tau}")
        os.system(f"sc --rot-frame {ed} --tau {tau}")


def plot():
    print("\x1b[0;32mPlotting data\x1b[0m")
    os.chdir("plot-files")
    print(f"\x1b[0;32mExecuting:\x1b[0m gnuplot plot-log-only.gp")
    os.system("gnuplot plot-log-only.gp")
    print(f"\x1b[0;32mExecuting:\x1b[0m pdflatex beta-comp.tex")
    os.system("pdflatex beta-comp.tex")
    shutil.copy("beta-comp.pdf", "../fig-3-comparison.pdf")

    print("\x1b[0;32mPlot available at fig-3-comparison.pdf\x1b[0m")


print("\x1b[0;32mGenerate data and plots for Fig. 1\x1b[0m")
print("1) Generate dynamics data \x1b[0;31mWILL DELETE DATA FROM RUNS\x1b[0m")
print("2) Generate P_F curve \x1b[0;31mWILL DELETE DATA FROM RUNS\x1b[0m")
print("3) Generate P_RF curve \x1b[0;31mWILL DELETE DATA FROM RUNS\x1b[0m")
print("4) Produce plot (requires gnuplot and pdflatex)")
option = input()

switch = {"1": run_dyn, "2": run_PF, "3": run_PRF, "4": plot}
while option not in switch.keys():
    option = input("Invalid option, please try again: ")

switch.get(option)()
