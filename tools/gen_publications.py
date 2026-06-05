#!/usr/bin/env python3
"""Generate academicpages _publications/*.md files for Yaomin Zhao.

Data sourced from the CV (cv_zhao_yaomin-v3.pdf). Re-run to regenerate:
    python3 tools/gen_publications.py

Conventions:
  - The author's own name is wrapped in <b>...</b> (bold) in the citation.
  - An asterisk (*) marks the corresponding author.
  - Categories map to _config.yml `publication_category`:
      corresponding -> First- and Corresponding-Author Papers
      coauthored    -> Co-authored Papers
    (Pre-PKU papers are split into these two groups by authorship role.)
"""
import os
import re

PUB_DIR = os.path.join(os.path.dirname(__file__), "..", "_publications")

# (slug, year, category, authors, title, venue, volpart, extra, url)
PAPERS = [
    # ===== corresponding / first-author (after joining PKU) =====
    ("lowwave-annular-ducts", 2026, "corresponding",
     "<b>Y. Zhao</b>, T. Wang, B. Lyu*",
     "Low-wavenumber wall pressure fluctuations in turbulent flows within concentric annular ducts",
     "Journal of Fluid Mechanics", "", ", in press", "https://arxiv.org/abs/2601.04590"),
    ("asymmetric-particle-transport", 2026, "corresponding",
     "T. Wang, C. Zhang, <b>Y. Zhao</b>*",
     "Asymmetric particle transport in turbulent flows within concentric annular ducts",
     "Journal of Fluid Mechanics", "", ", in press", "https://arxiv.org/abs/2605.26981"),
    ("progressive-moe-rans", 2026, "corresponding",
     "H. Ji, Y. Luo, H. Zhou, <b>Y. Zhao</b>*",
     "Progressive mixture-of-experts with autoencoder routing for continual RANS turbulence modelling",
     "Journal of Fluid Mechanics", "", ", in press", "https://arxiv.org/abs/2601.09305"),
    ("roughness-lpt-transition", 2026, "corresponding",
     "X. Zhu, Y. Ge, <b>Y. Zhao</b>*, Z. Xiao, R. D. Sandberg",
     "Boundary layer transition induced by surface roughness distributed over a low-pressure turbine blade",
     "Journal of Turbomachinery", "", ", in press", "https://doi.org/10.1115/1.4072013"),
    ("hierarchical-hairpin-vortices", 2026, "corresponding",
     "W. Shen, Y. Ge, Z. Han, <b>Y. Zhao</b>*, Y. Yang*",
     "Constructing wall turbulence using hierarchical hairpin vortices",
     "Physical Review Fluids", ", 11, 044604", "", ""),
    ("compressor-cascade-frequency", 2026, "corresponding",
     "T. Wang, B. Lyu, <b>Y. Zhao</b>*",
     "Frequency response of the unsteady separating boundary layer in a compressor cascade",
     "Acta Mechanica Sinica", "", ", in press", ""),
    ("four-equation-roughness", 2026, "corresponding",
     "Y. Ge, X. Zhu, Y. Fang, <b>Y. Zhao</b>*",
     "A machine-learning-enhanced four-equation model for predicting roughness-induced transition",
     "AIAA Journal", "", ", in press", ""),
    ("point-particle-dns-overset", 2026, "corresponding",
     "T. Wang, B. Meng, B. Tian, <b>Y. Zhao</b>*",
     "A high-fidelity and efficient framework for point-particle direct numerical simulation based on multi-block overset grids",
     "Computer Physics Communications", ", 322, 110059", "", ""),
    ("compressible-mixing-model", 2025, "corresponding",
     "H. Xie, T. Luo, <b>Y. Zhao</b>*, Y. Zhang*, J. Wang",
     "A compressible Reynolds-averaged mixing model considering turbulent composition and heat fluxes",
     "Journal of Fluid Mechanics", ", 1019, A56", "", ""),
    ("des-interfacial-mixing", 2025, "corresponding",
     "H. Xie, M. Xiao, <b>Y. Zhao</b>*, Y. Zhang*, J. Wang, Y. Shi",
     "A detached-eddy simulation methodology for interfacial mixing flows",
     "Physica D: Nonlinear Phenomena", ", 482, 134892", "", ""),
    ("intermittency-transition-mixing", 2025, "corresponding",
     "H. Xie, H. Qi, M. Xiao, Y. Zhang*, <b>Y. Zhao</b>*",
     "An intermittency-based Reynolds-averaged transition model for mixing flows induced by interfacial instabilities",
     "Journal of Fluid Mechanics", ", 1002, A31", "", ""),
    ("transformer-inverse-cascade", 2025, "corresponding",
     "H. Li, J. Xie, C. Zhang, Y. Zhang, <b>Y. Zhao</b>*",
     "A transformer-based convolutional method to model inverse cascade in forced two-dimensional turbulence",
     "Journal of Computational Physics", ", 520, 113475", "", ""),
    ("evolutionary-neural-networks", 2024, "corresponding",
     "H. Li, <b>Y. Zhao</b>*, F. Waschkowski, R. D. Sandberg",
     "Evolutionary neural networks for learning turbulence closure models with explicit expressions",
     "Physics of Fluids", ", 36, 055126", "", ""),
    ("pde-identification-enn", 2024, "corresponding",
     "H. Zhou, H. Li, <b>Y. Zhao</b>*",
     "Identification of partial differential equations from noisy data with integrated knowledge discovery and embedding using evolutionary neural networks",
     "Theoretical and Applied Mechanics Letters", ", 14(2), 100511", "", ""),
    ("dns-hpt-stage", 2023, "corresponding",
     "T. Wang, <b>Y. Zhao</b>*, J. Leggett, R. D. Sandberg",
     "Direct numerical simulation of a high-pressure turbine stage: unsteady boundary layer transition and the resulting flow structures",
     "Journal of Turbomachinery", ", 145(12), 121009", "", ""),
    ("kl-mixing-gep", 2023, "corresponding",
     "H. Xie, <b>Y. Zhao</b>*, Y. Zhang*",
     "Data-driven nonlinear K–L turbulent mixing model via gene expression programming method",
     "Acta Mechanica Sinica", ", 39, 322315", "", ""),
    ("unsteady-hpt-performance", 2023, "corresponding",
     "J. Leggett, <b>Y. Zhao</b>*, R. D. Sandberg",
     "High-fidelity simulation study of the unsteady flow effects on high-pressure turbine blade performance",
     "Journal of Turbomachinery", ", 145(1), 011002", "", ""),
    ("les-particle-laden-ml", 2022, "corresponding",
     "Q. Wu, <b>Y. Zhao</b>*, Y. Shi, S. Chen",
     "Large-eddy simulation of particle-laden isotropic turbulence using machine-learned subgrid-scale model",
     "Physics of Fluids", ", 34, 065129", " (Editor's Pick)", ""),
    ("les-gep-model", 2021, "corresponding",
     "H. Li, <b>Y. Zhao</b>*, J. Wang, R. D. Sandberg",
     "Data-driven model development for large-eddy simulation of turbulence using gene-expression programming",
     "Physics of Fluids", ", 33, 125127", "", ""),
    ("turbulence-modelling-gep-cn", 2021, "corresponding",
     "<b>Y. Zhao</b>*, X. Xu",
     "Data-driven turbulence modelling based on gene-expression programming",
     "Chinese Journal of Theoretical and Applied Mechanics", ", 53(10), 1–16", " (in Chinese)", ""),

    # ===== co-authored (after joining PKU) =====
    ("quantum-fluid-vortex", 2026, "coauthored",
     "Z. Wang, J. Zhong, K. Wang, Z. Zhu, Z. Bao, C. Zhu, W. Zhao, <b>Y. Zhao</b>, Y. Yang, C. Song*, S. Xiong*",
     "Simulating fluid vortex interactions on a superconducting quantum processor",
     "Nature Communications", ", 17, 2602", "", ""),
    ("oneshot-transformer-turbine", 2026, "coauthored",
     "Y. Fang*, M. Reissmann, R. Pacciani, <b>Y. Zhao</b>, A. S. H. Ooi, M. Marconcini, H. D. Akolekar, R. D. Sandberg",
     "Accelerating CFD-driven training of transition and turbulence models for turbine flows by one-shot and real-time transformer integration",
     "Computers & Fluids", ", 306, 106927", "", ""),
    ("quantum-lattice-boltzmann", 2025, "coauthored",
     "B. Wang, Z. Meng, <b>Y. Zhao</b>, Y. Yang*",
     "Quantum lattice Boltzmann method for simulating nonlinear fluid dynamics",
     "npj Quantum Information", ", 11, 196", "", ""),
    ("quantum-computing-review-cn", 2025, "coauthored",
     "Z. Meng, Z. Lu, S. Xiong, <b>Y. Zhao</b>, Y. Yang*",
     "Advances in quantum computing for fluid dynamics",
     "Advances in Mechanics", ", 55(3), 541–566", " (in Chinese)", ""),
    ("quantum-vortex-filaments", 2025, "coauthored",
     "C. Zhu, Z. Wang, S. Xiong*, <b>Y. Zhao</b>, Y. Yang",
     "Quantum implicit representation of vortex filaments in turbulence",
     "Journal of Fluid Mechanics", ", 1014, A31", "", ""),
    ("gradient-gep-closure", 2024, "coauthored",
     "F. Waschkowski*, H. Li, A. Deshmukh, T. Grenga, <b>Y. Zhao</b>, H. Pitsch, J. Klewicki, R. D. Sandberg",
     "Gradient information and regularization for gene expression programming to develop data-driven physics closure models",
     "Flow, Turbulence and Combustion", "", "", ""),
    ("lke-generalization", 2024, "coauthored",
     "Y. Fang*, <b>Y. Zhao</b>, H. D. Akolekar, A. S. H. Ooi, R. D. Sandberg, R. Pacciani, M. Marconcini",
     "A data-driven approach for generalizing the laminar kinetic energy model for separation and bypass transition in low- and high-pressure turbines",
     "Journal of Turbomachinery", ", 146(9), 091005", "", ""),
    ("multicase-cfd-training", 2023, "coauthored",
     "Y. Fang*, <b>Y. Zhao</b>, F. Waschkowski, A. S. H. Ooi, R. D. Sandberg",
     "Toward more general turbulence models via multicase computational-fluid-dynamics-driven training",
     "AIAA Journal", ", 65(5)", "", ""),
    ("micro-grooves-taylor-couette", 2023, "coauthored",
     "B. Xu, H. Li, X. Liu, Y. Xiang, P. Lv, X. Tan, <b>Y. Zhao</b>, C. Sun, H. Duan*",
     "Effect of micro-grooves on drag reduction in Taylor–Couette flow",
     "Physics of Fluids", ", 35, 063608", "", ""),
    ("coupled-symbolic-deeplearning", 2023, "coauthored",
     "C. Lav*, A. J. Banko, F. Waschkowski, <b>Y. Zhao</b>, C. J. Elkins, J. K. Eaton, R. D. Sandberg",
     "A coupled framework for symbolic turbulence models from deep learning",
     "International Journal of Heat and Fluid Flow", ", 101, 109140", "", ""),
    ("ml-turbulence-heatflux-review", 2022, "coauthored",
     "R. D. Sandberg*, <b>Y. Zhao</b>",
     "Machine-learning for turbulence and heat-flux model development: a review of challenges associated with distinct physical phenomena and progress to date",
     "International Journal of Heat and Fluid Flow", ", 95, 108983", " (Review)", ""),
    ("multiobjective-cfd-closure", 2022, "coauthored",
     "F. Waschkowski*, <b>Y. Zhao</b>, R. D. Sandberg, J. Klewicki",
     "Multi-objective CFD-driven development of coupled turbulence closure models",
     "Journal of Computational Physics", ", 452, 110922", "", ""),

    # ===== before joining PKU =====
    ("ml-cfd-lpt-wakemixing", 2021, "coauthored",
     "H. D. Akolekar*, <b>Y. Zhao</b>, R. D. Sandberg, R. Pacciani",
     "Integration of machine learning and computational fluid dynamics to develop turbulence models for improved low-pressure turbine wake mixing prediction",
     "Journal of Turbomachinery", ", 143, 121001", "", ""),
    ("hpt-vane-large-disturbances", 2021, "corresponding",
     "<b>Y. Zhao</b>*, R. D. Sandberg",
     "High-fidelity simulations of a high-pressure turbine vane subject to large disturbances: effect of exit Mach number on losses",
     "Journal of Turbomachinery", ", 143, 091002", "", ""),
    ("bypass-transition-pg-curvature", 2020, "corresponding",
     "<b>Y. Zhao</b>*, R. D. Sandberg",
     "Bypass transition in boundary layers subject to strong pressure gradient and curvature effects",
     "Journal of Fluid Mechanics", ", 888, A4", " (Featured on cover)", ""),
    ("rans-model-cfd-driven-ml", 2020, "corresponding",
     "<b>Y. Zhao</b>*, H. D. Akolekar, J. Weatheritt, V. Michelassi, R. D. Sandberg",
     "RANS turbulence model development using CFD-driven machine learning",
     "Journal of Computational Physics", ", 411, 109413", "", ""),
    ("entropy-loss-rans-hpt", 2020, "corresponding",
     "<b>Y. Zhao</b>*, R. D. Sandberg",
     "Using a new entropy loss analysis to assess the accuracy of RANS predictions of a high-pressure turbine vane",
     "Journal of Turbomachinery", ", 142, 081008", "", ""),
    ("scalar-flux-jet-crossflow", 2020, "coauthored",
     "J. Weatheritt, <b>Y. Zhao</b>, R. D. Sandberg*, S. Mizukami, K. Tanimoto",
     "Data-driven scalar-flux model development with application to jet in cross flow",
     "International Journal of Heat and Mass Transfer", ", 147, 118931", "", ""),
    ("endwall-lpt-part1", 2019, "coauthored",
     "R. Pichler, <b>Y. Zhao</b>, R. D. Sandberg*, V. Michelassi, R. Pacciani, M. Marconcini, A. Arnone",
     "Large-eddy simulation and RANS analysis of the end-wall flow in a linear low-pressure turbine cascade, part I: flow and secondary vorticity fields under varying inlet condition",
     "Journal of Turbomachinery", ", 141, 121005", "", ""),
    ("endwall-lpt-part2", 2019, "coauthored",
     "M. Marconcini*, R. Pacciani, A. Arnone, V. Michelassi, R. Pichler, <b>Y. Zhao</b>, R. D. Sandberg",
     "Large-eddy simulation and RANS analysis of the end-wall flow in a linear low-pressure turbine cascade, part II: loss generation",
     "Journal of Turbomachinery", ", 141, 051004", "", ""),
    ("sinuous-vortex-spots", 2018, "corresponding",
     "<b>Y. Zhao</b>, S. Xiong, Y. Yang*, S. Chen",
     "Sinuous distortion of vortex surfaces in the lateral growth of turbulent spots",
     "Physical Review Fluids", ", 3, 074701", "", ""),
    ("vortex-reconnection-transition", 2016, "corresponding",
     "<b>Y. Zhao</b>, Y. Yang*, S. Chen",
     "Vortex reconnection in the late transition in channel flow",
     "Journal of Fluid Mechanics", ", 802, R4", "", ""),
    ("material-surfaces-transition", 2016, "corresponding",
     "<b>Y. Zhao</b>, Y. Yang*, S. Chen",
     "Evolution of material surfaces in the temporal transition in channel flow",
     "Journal of Fluid Mechanics", ", 793, 840–876", "", ""),
    ("shear-improved-smagorinsky", 2015, "coauthored",
     "Z. Xia*, Y. Shi, <b>Y. Zhao</b>",
     "Assessment of the shear-improved Smagorinsky model in laminar-turbulent transitional channel flow",
     "Journal of Turbulence", ", 16(10), 925–936", "", ""),
    ("constrained-les-transition", 2014, "corresponding",
     "<b>Y. Zhao</b>, Z. Xia*, Y. Shi, Z. Xiao, S. Chen",
     "Constrained large-eddy simulation of laminar-turbulent transition in channel flow",
     "Physics of Fluids", ", 26, 095103", "", ""),
]


# DOIs resolved from Crossref (tools/find_dois.py) for entries that had no link.
# The 4 papers omitted here are either still in press (no DOI yet) or in
# Chinese-language journals not indexed by Crossref.
DOIS = {
    "hierarchical-hairpin-vortices": "10.1103/q3gt-v8jm",
    "point-particle-dns-overset": "10.1016/j.cpc.2026.110059",
    "compressible-mixing-model": "10.1017/jfm.2025.10614",
    "des-interfacial-mixing": "10.1016/j.physd.2025.134892",
    "intermittency-transition-mixing": "10.1017/jfm.2024.1160",
    "transformer-inverse-cascade": "10.1016/j.jcp.2024.113475",
    "evolutionary-neural-networks": "10.1063/5.0203975",
    "pde-identification-enn": "10.1016/j.taml.2024.100511",
    "dns-hpt-stage": "10.1115/1.4063510",
    "kl-mixing-gep": "10.1007/s10409-022-22315-x",
    "unsteady-hpt-performance": "10.1115/1.4055576",
    "les-particle-laden-ml": "10.1063/5.0098399",
    "les-gep-model": "10.1063/5.0076693",
    "quantum-fluid-vortex": "10.1038/s41467-026-69168-8",
    "oneshot-transformer-turbine": "10.1016/j.compfluid.2025.106927",
    "quantum-lattice-boltzmann": "10.1038/s41534-025-01142-6",
    "quantum-vortex-filaments": "10.1017/jfm.2025.10278",
    "gradient-gep-closure": "10.1007/s10494-024-00579-7",
    "lke-generalization": "10.1115/1.4065124",
    "multicase-cfd-training": "10.2514/1.j062572",
    "micro-grooves-taylor-couette": "10.1063/5.0145900",
    "coupled-symbolic-deeplearning": "10.1016/j.ijheatfluidflow.2023.109140",
    "ml-turbulence-heatflux-review": "10.1016/j.ijheatfluidflow.2022.108983",
    "multiobjective-cfd-closure": "10.1016/j.jcp.2021.110922",
    "ml-cfd-lpt-wakemixing": "10.1115/1.4051417",
    "hpt-vane-large-disturbances": "10.1115/1.4050453",
    "bypass-transition-pg-curvature": "10.1017/jfm.2020.39",
    "rans-model-cfd-driven-ml": "10.1016/j.jcp.2020.109413",
    "entropy-loss-rans-hpt": "10.1115/1.4046531",
    "scalar-flux-jet-crossflow": "10.1016/j.ijheatmasstransfer.2019.118931",
    "endwall-lpt-part1": "10.1115/1.4045080",
    "endwall-lpt-part2": "10.1115/1.4042208",
    "sinuous-vortex-spots": "10.1103/physrevfluids.3.074701",
    "vortex-reconnection-transition": "10.1017/jfm.2016.492",
    "material-surfaces-transition": "10.1017/jfm.2016.152",
    "shear-improved-smagorinsky": "10.1080/14685248.2015.1043131",
    "constrained-les-transition": "10.1063/1.4895589",
}


def yaml_sq(value):
    """Single-quote a YAML scalar, escaping embedded single quotes."""
    return "'" + value.replace("'", "''") + "'"


def main():
    os.makedirs(PUB_DIR, exist_ok=True)
    # Remove any pre-existing publication markdown (e.g. the template samples).
    for fn in os.listdir(PUB_DIR):
        if fn.endswith(".md"):
            os.remove(os.path.join(PUB_DIR, fn))

    # Assign ordering dates: within each category, newer CV entries (listed first)
    # get a later date so `for post in site.publications reversed` shows them first.
    # The displayed year is the real publication year; only the day encodes order.
    day_counter = {}
    written = 0
    for slug, year, category, authors, title, venue, volpart, extra, url in PAPERS:
        if not url and slug in DOIS:
            url = "https://doi.org/" + DOIS[slug]
        key = (category, year)
        day = day_counter.get(key, 28)
        day_counter[key] = day - 1
        date = "%04d-12-%02d" % (year, day)

        citation = '%s. (%d). "%s." <i>%s</i>%s%s.' % (
            authors, year, title, venue, volpart, extra)

        lines = ["---"]
        lines.append('title: "%s"' % title.replace('"', "'"))
        lines.append("collection: publications")
        lines.append("category: %s" % category)
        lines.append("permalink: /publication/%s" % slug)
        lines.append("date: %s" % date)
        lines.append("venue: %s" % yaml_sq(venue))
        if url:
            lines.append("paperurl: %s" % yaml_sq(url))
        lines.append("citation: %s" % yaml_sq(citation))
        lines.append("---")
        lines.append("")

        fname = "%s-%s.md" % (date, slug)
        with open(os.path.join(PUB_DIR, fname), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        written += 1

    print("wrote %d publication files to %s" % (written, os.path.normpath(PUB_DIR)))


if __name__ == "__main__":
    main()
