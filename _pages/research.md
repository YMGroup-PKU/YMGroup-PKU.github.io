---
layout: single
title: "Research"
permalink: /research/
author_profile: true
---

Turbulence sets performance limits across aerospace and energy systems, yet it remains hard to predict because it couples a wide range of scales and resists reduced description. My research advances turbulence prediction on two complementary fronts — developing **interpretable, generalizable data-driven models**, and performing **high-fidelity simulations (DNS and LES)** that resolve the controlling physics of complex flows. I use simulation to expose flow mechanisms and data-driven methods to turn them into models that generalize across regimes, and I apply both to national needs in aero-engines and inertial confinement fusion.

## Interpretable and generalizable turbulence modeling

Predictive turbulence simulation across diverse regimes is limited by the closure and subgrid-modeling problem. I develop interpretable, data-driven models that generalize across flow conditions and connect to the physical structure of turbulence. Building on Gene Expression Programming, I construct explicit, human-readable closures for RANS and large-eddy simulation; a combined Transformer–convolution framework captures the inverse cascade in under-resolved two-dimensional turbulence; and a progressive mixture-of-experts framework enables continual learning of RANS closures that improve on new flow regimes without forgetting previous ones. Modeling wall turbulence as hierarchically organized hairpin-vortex packets, I also construct realistic turbulent fields that reproduce channel-flow statistics from friction Reynolds numbers of 1,000 to 10,000 and rapidly initialize high-fidelity simulations.

<p style="text-align:center;">
  <img src="/images/research-modeling.png" alt="Interpretable data-driven turbulence modeling" style="width:70%; max-width:420px;" /><br>
  <em style="font-size:0.9em; color:#666;">Interpretable, data-driven turbulence modeling and structure-based construction of wall turbulence.</em>
</p>

## High-fidelity simulation of complex engineering flows

Many engineering flows — in aero-engines, ducts, and particle-laden systems — combine complex geometry, strong unsteadiness, high Reynolds number, and multiphysics coupling that defeat engineering models. Using DNS and LES together with linear-stability and data-driven analysis, I resolve their underlying physics and extract features for engineering prediction. I developed a high-fidelity point-particle DNS framework on multi-block overset grids and performed the first DNS of particle-laden turbulence in complex cascades and concentric annular ducts. With DNS of high- and low-pressure turbine configurations I identified the unsteady transition pathways set by wake impingement, free-stream turbulence, and surface roughness, and turned this understanding into a machine-learning-enhanced four-equation transition model. Compressible DNS of annular ducts and compressor cascades further clarifies the wall-pressure fluctuations and tonal-noise feedback central to internal-flow aeroacoustics.

<p style="text-align:center;">
  <img src="/images/research-simulation.png" alt="High-fidelity simulation of engineering flows" style="width:70%; max-width:420px;" /><br>
  <em style="font-size:0.9em; color:#666;">High-fidelity DNS/LES of particle-laden turbulence, aero-engine transition, and internal-flow aeroacoustics.</em>
</p>

## Interfacial mixing for inertial confinement fusion

In inertial confinement fusion (ICF), turbulent mixing driven by Rayleigh–Taylor and Richtmyer–Meshkov instabilities lowers implosion compression efficiency and can cause ignition failure. This mixing is strongly compressible, multiscale, and transitional — regimes that standard RANS models capture poorly. I introduced an intermittency-based transport equation, coupled to the K–L model, that tracks the full path from laminar perturbation growth through transition to fully developed turbulence; a compressible mixing model that accounts for turbulent composition and counter-gradient heat fluxes under strong density stratification; and an efficient detached-eddy method that switches automatically between RANS in the mixing core and LES at the mixing front, reaching LES-level accuracy with roughly one-eighth of the cells or fewer.

<p style="text-align:center;">
  <img src="/images/research-mixing.png" alt="Interfacial mixing modeling for ICF" style="width:70%; max-width:420px;" /><br>
  <em style="font-size:0.9em; color:#666;">Modeling and efficient high-fidelity simulation of compressible interfacial mixing for ICF.</em>
</p>
