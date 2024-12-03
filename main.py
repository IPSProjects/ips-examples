import ipsuite as ips

project = ips.Project()

with project:
    water = ips.AddDataH5MD(file="data/water.h5", name="water")
    bmim_bf4 = ips.AddData(file="data/BMIM_BF4_363_15K.extxyz", name="BMIM_BF4_363_15K")

with project.group("gromacs"):
    system = ips.Smiles2Gromacs(
        smiles=["CCCCN1C=C[N+](=C1)C", "CC(=O)[O-]"],
        density=0.9,
        count=[16, 16],
        labels=["Imx", "BFx"],
        config_files=["config/gromacs/gmx_em.yaml"],
        mdp_files=["config/gromacs/gmx_md.mdp"],
        fudgeLJ=1.0,
        fudgeQQ=1.0,
    )

with project.group("pack"):
    etoh = ips.Smiles2Conformers(smiles="CCO", numConfs=10)
    box = ips.MultiPackmol(data=[etoh.frames], count=[16], density=800, n_configurations=10)

project.build()
