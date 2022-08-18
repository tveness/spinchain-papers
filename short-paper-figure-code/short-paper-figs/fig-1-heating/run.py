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


def run_sample():
    check_sc()
    print("\x1b[0;32mRunning sample\x1b[0m")
    with open("sample-config.toml", "rb") as f:
        params = tomli.load(f)
    run(params)


def run_full():
    check_sc()
    print("\x1b[0;32mRunning full\x1b[0m")
    with open("full-config.toml", "rb") as f:
        params = tomli.load(f)
    run(params)


def run(params):
    [l, L, taus, dj, cycles, avg, threads] = [
        params["l"],
        params["L"],
        params["taus"],
        params["dj"],
        params["cycles"],
        params["avg"],
        params["threads"],
    ]

    print("l:", l)
    print("L:", L)
    print("taus:", taus)
    print("dj:", dj)
    print("cycles:", cycles)
    print("avg:", avg)

    # Need to determine the number of loops
    loops = 1 + avg // 1000

    runs = avg // loops

    print("\x1b[0;32mGenerating scripts for closed system\x1b[0m")
    # Change dir
    os.chdir("closed-system")
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
    sc_conf = sc_default_config
    sc_conf["l"] = l
    sc_conf["L"] = l  # This is not a mistake: this is the closed system, where L=l
    sc_conf["dj"] = dj
    sc_conf["runs"] = runs
    sc_conf["threads"] = threads

    with open("cycles.toml", "wb") as f:
        cycles_dict = {"cycles": cycles, "taus": taus}
        tomli_w.dump(cycles_dict, f)

    # Now create the directories and each associate config file
    for tau in taus:
        # Clear old directories
        dirname = "t-" + str(tau)
        try:
            shutil.rmtree(dirname)
        except FileNotFoundError:
            pass
        os.mkdir(dirname)
        sc_conf["tau"] = tau
        # Total run time is determined by largest number of cycles
        sc_conf["t"] = cycles[-1] * tau

        # Write config file
        with open("t-" + str(tau) + "/config.toml", "wb") as f:
            tomli_w.dump(sc_conf, f)

    print("\x1b[0;32mGenerating scripts for open system\x1b[0m")
    # Generate scripts for open system
    sc_conf["L"] = L
    os.chdir("..")
    shutil.copy("closed-system/runs.sh", "open-system/runs.sh")
    os.chdir("open-system")

    with open("cycles.toml", "wb") as f:
        cycles_dict = {"cycles": cycles, "taus": taus}
        tomli_w.dump(cycles_dict, f)

    st = os.stat("runs.sh")
    os.chmod("runs.sh", st.st_mode | stat.S_IEXEC)
    # Now create the directories and each associate config file, only difference is now L is not equal to l
    for tau in taus:
        # Clear old directories
        dirname = "t-" + str(tau)
        try:
            shutil.rmtree(dirname)
        except FileNotFoundError:
            pass

        os.mkdir(dirname)
        sc_conf["tau"] = tau
        # Total run time is determined by largest number of cycles
        sc_conf["t"] = cycles[-1] * tau

        # Write config file
        with open("t-" + str(tau) + "/config.toml", "wb") as f:
            tomli_w.dump(sc_conf, f)


def execute():
    print("\x1b[0;32mGenerating data for closed system\x1b[0m")
    os.chdir("closed-system")
    print("\x1b[0;32mExecuting:\x1b[0m bash runs.sh")
    os.system("bash runs.sh")

    print("\x1b[0;32mGenerating data for open system\x1b[0m")
    os.chdir("../open-system")
    print("\x1b[0;32mExecuting:\x1b[0m bash runs.sh")
    os.system("bash runs.sh")
    os.chdir("..")


def process():

    os.chdir("open-system")
    # Process data
    for dirs in ["open-system", "closed-system"]:
        print("\x1b[0;32mProcessing data for " + dirs + "\x1b[0m")
        os.chdir("..")
        os.chdir(dirs)

        # First clear all of the data
        for datfile in glob.glob("*cycles.dat"):
            os.remove(datfile)

        with open("cycles.toml", "rb") as f:
            dat = tomli.load(f)
            cycles = dat["cycles"]
            taus = dat["taus"]
        # Now create all of the n-cycle files
        cycle_files = []
        for i, item in enumerate(cycles):
            cycle_files.append(open(str(item) + "-cycles.dat", "w"))

        for t in taus:
            t_file = "t-" + str(t) + "/avg.dat"
            with open(t_file, "r") as f:
                for line_num, line in enumerate(f.readlines()):
                    if line_num in cycles:
                        idx = cycles.index(line_num)
                        cycle_files[idx].write(line)

        # Run through all the t-*/avg.dat

        #


def plot():
    print("\x1b[0;32mGenerating gnuplot files\x1b[0m")
    os.chdir("plot-files")
    with open("plot-heating.gp", "w") as f:
        f.write(
            'set terminal epslatex standalone color size 4.0in,3.0in background rgb "white"\n'
        )
        f.write(
            """set output "fig-1-heating.tex"
set xlabel "$\\\\tau = 2\\\\pi/\\\\omega$"
set label "$e$" rotate by 0 at graph 0 offset char -6, graph 0.5
set yrange [-1.1:0]
set xrange [:14]
set ytics 0.5
set mytics 5
set key Left reverse at graph 0.5, 0.3
set rmargin 1.0
set lmargin 7.0

"""
        )

        # Now do plotting
        f.write("plot ")
        # Do closed system
        os.chdir("../closed-system")
        with open("cycles.toml", "rb") as g:
            cycles = tomli.load(g)["cycles"]
        for i, item in enumerate(cycles):
            lc = i + 1
            f.write(
                f"\042../closed-system/{item}-cycles.dat\042 u ($1/{item}):3 w l lw 2 dt 2 lc {lc} title \042\042,\\\n"
            )

        # Now open system
        os.chdir("../open-system")
        with open("cycles.toml", "rb") as g:
            cycles = tomli.load(g)["cycles"]
            cycles.reverse()
        for i, item in enumerate(cycles):
            lc = len(cycles) - i
            f.write(
                f"\042../open-system/{item}-cycles.dat\042 u ($1/{item}):3 w l lw 2 dt 1 lc {lc} title \042$t={item}\\\\tau$\042,\\\n"
            )

    print("\x1b[0;32mPlotting data\x1b[0m")
    os.chdir("../plot-files")
    print("\x1b[0;32mExecuting:\x1b[0m gnuplot plot-heating.gp")
    os.system("gnuplot plot-heating.gp")
    print("\x1b[0;32mExecuting:\x1b[0m pdflatex fig-1-heating.tex")
    os.system("pdflatex fig-1-heating.tex")
    shutil.copy("fig-1-heating.pdf", "../fig-1-heating.pdf")

    print("\x1b[0;32mPlot available at fig-1-heating.pdf\x1b[0m")


print("\x1b[0;32mGenerate data and plots for Fig. 1\x1b[0m")
print("1) Generate scripts for sample run \x1b[0;31mWILL DELETE DATA FROM RUNS\x1b[0m")
print(
    "2) Generate scripts for full run (reproduce paper results) \x1b[0;31mWILL DELETE DATA FROM RUNS\x1b[0m"
)
print(
    "3) Execute scripts (closed-system/runs.sh, open-system/runs.sh) \x1b[0;31mWILL DELETE DATA FROM RUNS\x1b[0m"
)
print("4) Process data")
print("5) Produce plots (requires gnuplot and pdflatex)")
option = input()

switch = {"1": run_sample, "2": run_full, "3": execute, "4": process, "5": plot}
while option not in switch.keys():
    option = input("Invalid option, please try again: ")

switch.get(option)()
