---
layout: single
title: "Research"
permalink: /research/
author_profile: true
---

Turbulence sets performance limits across aerospace and energy systems, yet it remains hard to predict because it couples a wide range of scales and resists reduced description. My research advances turbulence prediction on two complementary fronts — developing **interpretable, generalizable data-driven models**, and performing **high-fidelity simulations (DNS and LES)** that resolve the controlling physics of complex flows. I use simulation to expose flow mechanisms and data-driven methods to turn them into models that generalize across regimes, and I apply both to national needs in aero-engines and inertial confinement fusion.

## Interpretable and generalizable turbulence modeling

Predictive turbulence simulation across diverse regimes is limited by the closure and subgrid-modeling problem. My work develops interpretable, data-driven models that generalize across flow conditions and connect to the physical structure of turbulence.

**Interpretable data-driven modeling.** Purely data-driven "black-box" closures lack interpretability, generalize poorly, and are hard to couple with existing solvers. I developed an explicit model-construction methodology based on Gene Expression Programming that balances accuracy and interpretability and extends to large-eddy simulation subgrid modeling and interfacial mixing. To capture the inverse cascade in under-resolved two-dimensional turbulence I proposed a non-local Transformer–convolution framework, and I coupled gene expression programming with a physics-informed neural network to identify governing equations from noisy data. These models generalize well across isotropic, mixing, and particle-laden turbulence.

<p style="text-align:center;">
  <img src="/images/research-gep.png" alt="Gene-expression-programming turbulence modeling" style="width:65%; max-width:400px;" /><br>
  <em style="font-size:0.9em; color:#666;">Interpretable, data-driven turbulence modeling based on gene expression programming.</em>
</p>

**Continual RANS modeling via mixture-of-experts.** A practical RANS model must stay accurate as new regimes appear, yet most data-driven closures are trained for fixed cases and must be retrained from scratch. I proposed a progressive mixture-of-experts framework: an autoencoder-based router assigns each flow to a specialized expert, and when a regime is not represented a new expert is added at low cost without degrading existing ones, naturally avoiding catastrophic forgetting. Across airfoil-wake, channel, periodic-hill, and square-duct flows it improves accuracy on both seen and unseen cases while keeping inference cost fixed as the model grows.

<p style="text-align:center;">
  <img src="/images/research-pmoe.png" alt="Progressive mixture-of-experts RANS modeling" style="width:65%; max-width:400px;" /><br>
  <em style="font-size:0.9em; color:#666;">Progressive mixture-of-experts framework for continual RANS turbulence modeling.</em>
</p>

**Structure-based construction of wall turbulence.** Wall turbulence is organized into hierarchical coherent structures such as hairpin vortices that the attached-eddy model describes only statistically. Modeling wall turbulence as an ensemble of complex vortices, I construct turbulent fields from hierarchically organized hairpin-vortex packets calibrated to reproduce both attached and detached motions. The fields reproduce the key statistics and structures of channel turbulence at friction Reynolds numbers from 1,000 to 10,000, clarify how vortex geometry sets features such as meandering streaks and superstructures, and develop rapidly into fully developed turbulence, providing an efficient way to initialize high-fidelity simulations.

<p style="text-align:center;">
  <img src="/images/research-wallturb.png" alt="Construction of wall turbulence from hairpin-vortex packets" style="width:65%; max-width:400px;" /><br>
  <em style="font-size:0.9em; color:#666;">Wall turbulence constructed from hierarchically organized hairpin-vortex packets.</em>
</p>

## High-fidelity simulation of complex engineering flows

Many engineering flows — in aero-engines, ducts, and particle-laden systems — combine complex geometry, strong unsteadiness, high Reynolds number, and multiphysics coupling that defeat engineering models. Using DNS and LES together with linear-stability and data-driven analysis, my work resolves the underlying physics of these flows and extracts features for engineering prediction.

**Particle-laden turbulence in complex geometries.** Particle-laden turbulence governs problems such as aero-engine blade erosion but demands resolving complex-geometry boundary layers together with many particles. I developed a high-fidelity point-particle DNS framework on multi-block overset grids that, for the first time, performs point-particle DNS of large particle populations in complex cascade flows. Building on it, I carried out the first DNS of particle-laden turbulence in concentric annular ducts and showed that transverse curvature drives asymmetric radial transport, explained by a Sturm–Liouville modal analysis and a reduced-order model.

<p style="text-align:center;">
  <img src="/images/research-particle.png" alt="Point-particle DNS of particle-laden turbulence" style="width:65%; max-width:400px;" /><br>
  <em style="font-size:0.9em; color:#666;">Point-particle DNS of particle-laden turbulence in complex cascade and annular-duct geometries.</em>
</p>

**Boundary-layer transition in aero-engine flows.** Transition strongly affects loss and heat transfer in turbomachinery yet is poorly predicted under realistic disturbances. With DNS of a high-pressure turbine stage at engine-relevant conditions I identified two unsteady transition pathways driven by periodic wakes and free-stream turbulence, and used DNS to disentangle how distributed surface roughness triggers transition. Building on this physical understanding, I developed a machine-learning-enhanced four-equation transition model that accurately predicts transition onset, separation-bubble suppression, and wake loss across cascade geometries, outperforming traditional models.

<p style="text-align:center;">
  <img src="/images/research-transition.png" alt="Boundary-layer transition on turbine blades" style="width:65%; max-width:400px;" /><br>
  <em style="font-size:0.9em; color:#666;">Boundary-layer transition on turbine blades induced by wakes, free-stream turbulence, and surface roughness.</em>
</p>

**Wall-pressure fluctuations and internal-flow aeroacoustics.** Wall-pressure fluctuations and the tonal noise they radiate are central to internal-flow aeroacoustics. Using compressible DNS of concentric annular ducts I characterized the low-wavenumber wall-pressure spectrum and showed that strong transverse curvature excites acoustic duct modes and amplifies the practically important low-wavenumber components; an analytical Green's-function model attributes the amplification to geometry and near-wall sources. In a compressor cascade, combining linear stability with forced Navier–Stokes simulations, I clarified the frequency response of the unsteady separating boundary layer and proposed a modified acoustic-feedback model.

<p style="text-align:center;">
  <img src="/images/research-aeroacoustics.png" alt="Wall-pressure fluctuations and tonal-noise feedback" style="width:65%; max-width:400px;" /><br>
  <em style="font-size:0.9em; color:#666;">Wall-pressure fluctuations and tonal-noise feedback in internal turbulent flows.</em>
</p>

## Interfacial mixing for inertial confinement fusion

In inertial confinement fusion (ICF), turbulent mixing from interfacial instabilities such as Rayleigh–Taylor and Richtmyer–Meshkov lowers compression efficiency and can cause ignition failure. This mixing is strongly compressible, multiscale, and transitional, while standard RANS models capture compressibility and transition poorly. My work develops practical model corrections and an efficient high-fidelity simulation framework.

**Intermittency-based mixing-transition model.** ICF mixing evolves from perturbation growth through transition to developed turbulence, but existing RANS mixing models assume equilibrium turbulence. I introduced intermittency into the interfacial-mixing RANS framework, formulating an intermittency-factor transport equation coupled to the K–L model that tracks the onset and evolution of mixing transition through the local turbulence Reynolds number. Across canonical Rayleigh–Taylor and Richtmyer–Meshkov cases it predicts the full path from laminar to fully developed turbulent mixing.

<p style="text-align:center;">
  <img src="/images/research-intermittency.png" alt="Intermittency-based mixing-transition model" style="width:65%; max-width:400px;" /><br>
  <em style="font-size:0.9em; color:#666;">Intermittency-based RANS model for mixing transition driven by interfacial instabilities.</em>
</p>

**Compressible turbulent-mixing corrections.** During implosion the capsule shell develops strong density stratification, making the mixing intrinsically compressible, yet common RANS models neglect the resulting turbulent composition fluctuations and counter-gradient heat transport. I proposed a compressible mixing model that reformulates the closure of the turbulent mass flux — the core source term in the turbulent kinetic energy equation — to include both effects in a single framework, capturing the full-stage evolution of compressible Rayleigh–Taylor mixing.

<p style="text-align:center;">
  <img src="/images/research-compressible.png" alt="Compressible turbulent-mixing model" style="width:65%; max-width:400px;" /><br>
  <em style="font-size:0.9em; color:#666;">Compressible turbulent-mixing model accounting for composition and heat fluxes.</em>
</p>

**Efficient detached-eddy simulation for mixing.** ICF simulation demands both accuracy and efficiency: DNS and LES need grids of billions of cells, while RANS cannot resolve the initial perturbation spectrum or three-dimensional vortices. I proposed a detached-eddy method for interfacial mixing that uses a local mixing degree to switch automatically between RANS in the mixing core and LES at the mixing front, reaching accuracy comparable to high-resolution LES with about one-eighth of the cells or fewer.

<p style="text-align:center;">
  <img src="/images/research-des.png" alt="Detached-eddy simulation for interfacial mixing" style="width:65%; max-width:400px;" /><br>
  <em style="font-size:0.9em; color:#666;">Detached-eddy simulation for efficient, high-fidelity interfacial mixing.</em>
</p>
