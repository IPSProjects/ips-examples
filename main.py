import ipsuite as ips

project = ips.Project()

with project:
    water = ips.AddDataH5MD(file="data/water.h5", name="water")
    bmim_bf4 = ips.AddData(file="data/BMIM_BF4_363_15K.extxyz", name="BMIM_BF4_363_15K")

project.repro()
