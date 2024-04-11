# Author: Nicolas Legrand <nicolas.legrand@cfin.au.dk>

import papermill as pm
import subprocess
import os
import multiprocessing as mp


def reportHRD(
    sub,
    datapath="/home/xavfunk/repos/bp_bodily_self/HRD",
    reportPath="/home/xavfunk/repos/bp_bodily_self/HRD/reports",
    #session="Del1",
):

    #try:
        
    pm.execute_notebook(
        "/home/xavfunk/repos/bp_bodily_self/HeartRateDiscrimination.ipynb",
        f"{reportPath}/{sub}.ipynb",
        parameters=dict(subject=sub, path=datapath),
    )
    #command = f"jupyter nbconvert --to html --execute --TemplateExporter.exclude_input=True {reportPath}/{sub}.ipynb --output {reportPath}/{sub}_report.html"
    # This does not quite work so did this step by hand
    command = [
    "jupyter",
    "nbconvert",
    "--to",
    "html",
    "--execute",
    #"--TemplateExporter.exclude_input=True",
    f"{reportPath}/{sub}.ipynb",
    "--output",
    f"{reportPath}/{sub}_report.html"]
    
    subprocess.call(command)
    #os.remove(reportPath + "/" + sub + ".ipynb")
    #except:
        #print(f"Subject {sub} not found.")


if __name__ == "__main__":
    datapath = "/home/xavfunk/repos/bp_bodily_self/HRD"
    subList = os.listdir(datapath)
    subList = [sub for sub in subList if 'sub' in sub]
    print(subList)
    pool = mp.Pool(processes=4)
    pool.map(reportHRD, subList)
