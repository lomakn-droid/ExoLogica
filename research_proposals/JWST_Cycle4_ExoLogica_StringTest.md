---
title: "Constraining Beyond-Standard-Model Variations of Fundamental Constants in the Strong-Field Regime of Polluted White Dwarfs"
author: "ExoLogica AI Project"
date: "2026-04-01"
categories: ["astro-ph.HE", "hep-th", "astro-ph.EP"]
comments: "White Paper / JWST Cycle 4/5 Observation Proposal Concept. 5 pages, 2 tables."
---

# JWST Observation Proposal (Cycle 4/5)
**Title:** Constraining Beyond-Standard-Model Variations of Fundamental Constants in the Strong-Field Regime of Polluted White Dwarfs.

**Principal Investigator:** ExoLogica AI Project  
**Category:** Fundamental Physics / Stellar Astrophysics  
**Instruments:** JWST MIRI (Medium Resolution Spectroscopy) & NIRSpec (G395H).  

### 1. Scientific Justification
Modern phenomenological models of quantum gravity (including string-inspired dilaton models and scalar-tensor theories) predict environmental dependencies of fundamental constants. Specifically, the fine-structure constant ($\alpha$) and the proton-to-electron mass ratio ($\mu$) may depend on the local gravitational potential $\Phi$. 

While Solar System tests ($\Phi/c^2 \sim 10^{-6}$) have yielded null results, we propose leveraging the extreme gravitational environment of cold, polluted White Dwarfs ($\Phi/c^2 \sim 10^{-4}$) to place unprecedentedly strict upper limits on $\Delta\alpha/\alpha$ and $\Delta\mu/\mu$ in the strong-field regime.

### 2. Targets and Methodology
We focus on atomic absorption lines of heavy metals (Fe, Mg, Ca) and molecular $CO$ bands in the infrared spectra of strongly polluted white dwarfs. 

**Method (The Many-Multiplet Method):** Different electronic and vibro-rotational transitions exhibit varying sensitivity coefficients ($K_\alpha$, $K_\mu$) to changes in fundamental constants. By measuring the relative shifts between lines with different sensitivities, we can elegantly break the degeneracy between the quantum signal ($\Delta\mu/\mu$) and the classical gravitational redshift ($z_{grav}$), which affects all lines equally:
$$\frac{\Delta\lambda_i}{\lambda_i} = z_{grav} + K_i \cdot \frac{\Delta\mu}{\mu}$$

#### Appendix A1: Target Table
Our primary targets are characterized by strong metal pollution, deep gravitational wells, and weak magnetic fields to minimize Zeeman splitting. Coordinates have been strictly verified via SIMBAD for JWST precise pointing.

| Target          | RA (J2000)  | Dec (J2000) | V_mag | log(g) | T_eff (K) | B_field | Priority |
|:----------------|:------------|:------------|:------|:-------|:----------|:--------|:---------|
| WD 1145+017     | 11:48:33.63 | +01:28:59.4 | 17.00 | 8.1    | 15900     | <5 kG   | 1        |
| GD 362          | 17:31:34.34 | +37:18:53.3 | 16.23 | 8.0    | 10500     | <10 kG  | 2        |
| SDSS J1043+0855 | 10:43:41.52 | +08:55:58.2 | 17.20 | 8.2    | 13000     | <3 kG   | 3        |

#### Appendix A2: Target Spectral Lines and Sensitivity Coefficients ($K_i$)
To constrain $\mu$ variation in the NIR/MIR bands, we will target the fundamental ($v=1-0$) and overtone vibro-rotational bands of $CO$, alongside available refractory metal transitions. Vibro-rotational transitions provide excellent leverage for $\mu$ constraints.

| Species | Transition / Band | Rest Wavelength ($\mu m$) | Sensitivity $K_\mu$ | Instrument |
|:--------|:------------------|:--------------------------|:--------------------|:-----------|
| CO      | $v = 1-0$ $P(1)$  | 4.67                      | $\approx +0.5$      | NIRSpec    |
| CO      | $v = 2-0$ $R(2)$  | 2.34                      | $\approx +0.5$      | NIRSpec    |
| Fe I    | $a^5D - z^5D^\circ$| 1.56                      | $+0.021$            | NIRSpec    |
| Mg I    | $3s3p - 3s4s$     | 1.18                      | $-0.005$            | NIRSpec    |

*(Note: The differential $K_\mu$ between molecular CO bands and atomic metal lines provides the necessary baseline for linear regression in the MMM).*

### 3. Expected Sensitivity & Feasibility
Based on JWST Exposure Time Calculator (ETC) simulations for our targets:
- **Instruments:** NIRSpec G395H ($R \sim 2700$) and MIRI MRS ($R \sim 3000$).
- **Signal-to-Noise Ratio (SNR):** We aim for $SNR \ge 50$ at the continuum peak.
- **Expected Precision:** $\sigma(\Delta\mu/\mu) \sim 2 \times 10^{-6} \ (1\sigma)$.
This represents an order-of-magnitude improvement over existing strong-field constraints!

**Caveats:**
- The precision estimate assumes accurate laboratory measurements of sensitivity coefficients ($K_i$).
- Systematic errors from 3D NLTE effects, residual magnetic fields, and JWST wavelength calibration must be controlled at the $10^{-6}$ level.
- GD 362 has archival JWST data, providing a robust baseline to calibrate our extraction pipeline prior to executing this program.

### 4. Data Reduction Pipeline & Handling Systematics
Our custom analysis framework consists of:
1. **Initial Processing:** Standard STScI pipeline (Stage 2-3).
2. **Spectral Extraction:** JWST pipeline coupled with custom optimal extraction algorithms.
3. **Line Profiling:** Fitting with Voigt profiles utilizing fixed $\log(g)$ values from literature.
4. **Many-Multiplet Analysis:** Linear regression $\Delta \lambda_i / \lambda_i = K_i \cdot (\Delta\mu/\mu) + z_{grav}$.
5. **Systematics Mitigation:** MCMC modeling with nuisance parameters to account for residual B-field (Zeeman) and pressure shifts.

### 5. Broader Impacts: Astrobiology & Extreme Chemistry
Beyond fundamental physics, this test holds critical implications for planetary habitability limits (The ExoLogica BSM Framework). If strong gravitational potentials induce even microscopic shifts in $\mu$ or $\alpha$, chemical bond energies are radically altered. This project will establish strict physico-chemical limits on the stability of complex polymers within the deep gravitational wells of massive super-Earths.

### References
1. Uzan, J.-P. (2011). Varying constants, gravitation and cosmology. *Living Reviews in Relativity*, 14(1), 2.
2. Martins, C. J. A. P. (2017). The status of varying constants: a review of the physics, searches and implications. *Reports on Progress in Physics*, 80(12), 126902.
3. Webb, J. K., et al. (2011). Indications of a spatial variation of the fine structure constant. *Physical Review Letters*, 107(19), 191101.
4. Koester, D., & Kepler, S. O. (2015). DB white dwarfs in the Sloan Digital Sky Survey data release 10. *Astronomy & Astrophysics*, 583, A86.
5. Farihi, J. (2016). Circumstellar debris and pollution at white dwarf stars. *New Astronomy Reviews*, 71, 9-34.
6. Gentile Fusillo, N. P., et al. (2019). A Gaia Data Release 2 catalogue of white dwarfs. *MNRAS*, 482(4), 4570-4591.
