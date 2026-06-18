---
layout: single
title: "Research"
permalink: /research/
author_profile: true
---

<style>
.page__content p { text-align: justify; }
</style>

Predictive simulation of realistic turbulent flows remains challenging because turbulence involves multi-scale nonlinear interactions and couples strongly with geometry and multiphysics effects. Our research develops simulation and modeling methods for complex turbulent flows, with an emphasis on mechanism-resolving computation, interpretable model development, and engineering application. We use direct numerical simulations (DNS) and large-eddy simulations (LES) to identify governing mechanisms, and then translate those mechanisms into closures and reduced models that can be tested across flow regimes. Our work is applied to aero-engine internal flows, particle-laden turbulence, wall-bounded turbulence, and interfacial mixing.

## Interpretable and generalizable turbulence modeling

The main bottleneck in predictive turbulence simulation is the closure problem: unresolved turbulent effects must be modeled, yet closures calibrated for one configuration often fail when geometry, Reynolds number, or dominant physics change. Our work focuses on data-driven turbulence models that are interpretable, generalizable, and compatible with existing solvers.

**Interpretable data-driven modeling.** Purely data-driven "black-box" closures are difficult to interpret, often generalize poorly, and can be hard to couple with existing solvers. We make data-driven closures explicit and solver-compatible, using machine learning to discover model forms that respect physical constraints. One line of work uses gene-expression programming to build turbulence closures from invariants and tensor bases, producing explicit equations rather than neural-network surrogates. We developed GENets to combine GEP, neural-network optimization, and sparsity promotion for compact explicit models, and extended this approach to LES subgrid modeling for particle-laden turbulence and to nonlinear K–L closures for interfacial mixing. We also explored non-local Transformer–convolutional models for under-resolved two-dimensional turbulence, and coupled GEP with physics-informed learning to identify parsimonious governing equations from noisy data.

<p style="text-align:center;">
  <img src="/images/research/ml-closure.png" alt="Machine-learning turbulence closure development" style="width:95%; max-width:570px;" /><br>
  <em style="font-size:0.9em; color:#666;">Workflow of interpretable closure development using machine learning approaches.</em>
</p>

**Continual RANS modeling via mixture-of-experts.** A practical RANS model must remain useful as new flow regimes are encountered, yet most data-driven closures are trained for fixed cases and must be retrained when the flow changes. We proposed a progressive mixture-of-experts framework: a similarity router assigns each local flow state to a specialized expert, and when a new regime appears a new expert can be added without modifying trained components. Tested across airfoil wakes, channel flows, periodic hills, and square ducts, the model improves predictions for both seen and unseen cases while keeping inference cost tied to the selected expert. This gives data-driven RANS modeling a practical path toward expanding its range of validity without forgetting previously learned regimes.

<p style="text-align:center;">
  <img src="/images/research/pmoe.png" alt="Progressive mixture-of-experts RANS modeling" style="width:95%; max-width:570px;" /><br>
  <em style="font-size:0.9em; color:#666;">Progressive mixture-of-experts framework for continual RANS turbulence modeling.</em>
</p>

**Structure-based construction of wall turbulence.** Wall-bounded turbulence contains hierarchical coherent structures such as hairpin vortices. The attached-eddy model gives a successful statistical framework for the log-law region, but turning this structural picture into constructive flow fields remains difficult. We developed a method that represents wall turbulence as an ensemble of realistic hairpin-vortex packets whose geometry and organization are calibrated from observations. The constructed fields reproduce major statistics and coherent structures of channel turbulence at friction Reynolds numbers from 1,000 to 10,000, clarify how vortex geometry sets features such as meandering streaks and superstructures, and rapidly develop into fully developed turbulence in DNS, providing a physically grounded way to generate wall-turbulence initial conditions.

<p style="text-align:center;">
  <img src="/images/research/swat.png" alt="Construction of wall turbulence from hairpin-vortex packets" style="width:95%; max-width:570px;" /><br>
  <em style="font-size:0.9em; color:#666;">Wall turbulence constructed from hierarchically organized hairpin-vortex packets.</em>
</p>

## High-fidelity simulation of complex engineering flows

Many engineering flows, especially aero-engine internal flows, combine complex geometry, strong unsteadiness, high Reynolds number, and multiphysics coupling. In our research, high-fidelity simulation is not an end in itself — it is a way to expose mechanisms, create benchmark data, and guide reduced modeling. Using DNS and LES together with stability theory and data-driven analysis, we study particle transport, boundary-layer transition, and wall-pressure fluctuations in engine-relevant flows.

**Particle-laden turbulence in complex geometries.** Particle-laden turbulence governs problems such as aero-engine blade erosion, but predictive simulation requires resolving complex-geometry boundary layers together with large numbers of particles. We developed a point-particle DNS framework on multi-block overset curvilinear grids, enabling large-scale Lagrangian particle tracking in complex geometries, and applied it to particle-laden flow in a compressor cascade at engine-relevant conditions. Using the same capability, we carried out the first DNS of particle-laden turbulence in concentric annular ducts. The simulations showed that transverse curvature drives asymmetric radial transport, with particles preferentially drifting toward the outer wall while centrifugal effects near the inner wall compete with turbophoresis. A modal analysis and reduced-order model explain this behavior through competing transport modes.

<p style="text-align:center;">
  <img src="/images/research/particles.png" alt="Point-particle DNS of particle-laden turbulence" style="width:95%; max-width:570px;" /><br>
  <em style="font-size:0.9em; color:#666;">Point-particle DNS of particle-laden turbulence in compressor cascade and annular-duct geometries.</em>
</p>

**Boundary-layer transition in aero-engine flows.** Transition strongly affects loss and heat transfer in turbomachinery, yet engineering models predict it poorly under realistic disturbances. Using high-fidelity data of a high-pressure turbine stage, we identified two rotor suction-side transition pathways — bypass transition through Klebanoff streak instability, and wake-induced transition through interaction between incoming wakes and separation bubbles — and quantified how inlet free-stream turbulence changes intermittency, wall shear stress, and heat flux. For low-pressure turbine blades, DNS showed how distributed roughness can either sustain turbulence or be suppressed by favorable pressure gradients, depending on roughness scale and organization. These simulations informed a machine-learning-enhanced four-equation transition model that improves predictions of roughness-induced transition, separation-bubble suppression, blade loading, and wake losses across diverse geometries.

<p style="text-align:center;">
  <img src="/images/research/stage.png" alt="Boundary-layer transition on turbine blades" style="width:95%; max-width:570px;" /><br>
  <em style="font-size:0.9em; color:#666;">Boundary-layer transition on turbine blades induced by wakes and free-stream turbulence.</em>
</p>

**Wall-pressure fluctuations and internal-flow aeroacoustics.** Wall-pressure fluctuations and discrete tones are important aeroacoustic signatures of internal turbulent flows, but their low-wavenumber components are weak, geometry-sensitive, and coupled to acoustic feedback. Using compressible DNS of annular-duct turbulence, we showed that increasing curvature suppresses high-wavenumber wall-pressure energy while amplifying practically important low-wavenumber components; an analytical model based on Lighthill's acoustic analogy attributes the amplification mainly to geometric effects. In a compressor cascade, DNS and stability analysis reveal that suction-side absolute instability, trailing-edge scattering, and upstream-propagating acoustic waves form a feedback loop that selects the dominant tone. These studies connect high-fidelity aeroacoustic simulation with reduced physical models for noise-source identification and control.

<p style="text-align:center;">
  <img src="/images/research/wpf.png" alt="Wall-pressure fluctuations in internal turbulent flows" style="width:95%; max-width:570px;" /><br>
  <em style="font-size:0.9em; color:#666;">Wall-pressure fluctuations in internal turbulent flows.</em>
</p>

## Interfacial mixing flows induced by RT/RM instabilities

Rayleigh–Taylor (RT) and Richtmyer–Meshkov (RM) instabilities drive interfacial mixing in many variable-density flows. These flows evolve through instability growth, transition, and turbulent mixing, often with strong compressibility, sparse data, and limited experimental access. Standard RANS models usually assume fully developed turbulence and therefore miss important non-equilibrium stages of the mixing process. Our group develops model corrections and hybrid simulation methods for RT/RM-induced mixing, with inertial confinement fusion (ICF) serving as one important application that motivates and tests these methods.

**Intermittency-based mixing-transition model.** RT/RM-induced mixing evolves from initial perturbation growth through transition to fully developed turbulence, but existing RANS mixing models often assume equilibrium turbulence and miss the intermittency of the transition stage. We extended the intermittency concept from boundary-layer transition to interfacial mixing by defining an enstrophy-based factor and coupling it with the K–L model. Across canonical RT and RM cases, the model captures transition onset and turbulent mixing, while recovering the baseline model when the flow rapidly becomes fully turbulent. It gives RANS simulations a practical way to represent pre-turbulent and transitional stages that strongly affect later mixing width and intensity.

<p style="text-align:center;">
  <img src="/images/research/rt-transition.png" alt="Intermittency-based mixing-transition model" style="width:85%; max-width:510px;" /><br>
  <em style="font-size:0.9em; color:#666;">Intermittency-based RANS model for mixing transition driven by interfacial instabilities.</em>
</p>

**Compressible turbulent-mixing corrections.** In compressible RT/RM mixing, density stratification can make the dynamics differ substantially from incompressible mixing — ICF implosions being one important example. Using density-stratified RT flows as representative cases, we showed why the baseline K–L–γ model fails when static compressibility is important, and derived compressibility corrections for the turbulent mass-flux closure that incorporate turbulent composition effects and counter-gradient turbulent heat flux. The resulting model improves predictions of compressible RT mixing and clarifies which physical terms must be retained in RANS simulations of density-stratified mixing flows.

**Efficient detached-eddy simulation for mixing.** Three-dimensional RT/RM mixing simulations require both accuracy and efficiency: DNS and LES resolve initial perturbation spectra and coherent vortices but can be prohibitively expensive, while RANS is efficient but cannot resolve these structures. We extended detached-eddy simulation to interfacial mixing by blending RANS behavior in the small-scale mixing core with LES behavior near bubble/spike fronts. In density-stratified RT and reshocked RM cases, the method approaches LES-level accuracy for key mixing measures at much lower cost than pure LES.

<p style="text-align:center;">
  <img src="/images/research/des.png" alt="Detached-eddy simulation for interfacial mixing" style="width:85%; max-width:510px;" /><br>
  <em style="font-size:0.9em; color:#666;">(a) Mass fraction contour of RT mixing and (b) schematic of computational mode partition in detached-eddy simulation for efficient, high-fidelity interfacial mixing.</em>
</p>
