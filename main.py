import ipsuite as ips

project = ips.Project()

with project:
    water = ips.nodes.AddDataH5MD(file="data/water.h5", name="water")

project.repro()
