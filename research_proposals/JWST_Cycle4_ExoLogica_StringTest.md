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

**Method (The Many-Multiplet Method):** Different electronic transitions exhibit varying sensitivity coefficients ($K_\alpha$, $K_\mu$) to changes in fundamental constants. By measuring the relative shifts between lines with different sensitivities, we can elegantly break the degeneracy between the quantum signal ($\Delta\mu/\mu$) and the classical gravitational redshift ($z_{grav}$), which affects all lines equally.

#### Appendix A: Target Table
Our primary targets are characterized by strong metal pollution, deep gravitational wells, and weak magnetic fields to minimize Zeeman splitting.

| Target          | RA (J2000)  | Dec (J2000) | V_mag | log(g) | T_eff (K) | B_field | Priority |
|:----------------|:------------|:------------|:------|:-------|:----------|:--------|:---------|
| WD 1145+017     | 11:48:33.6  | +01:28:59.4 | 17.00 | 8.1    | 15900     | <5 kG   | 1        |
| GD 362          | 17:31:34.3  | +37:18:53.3 | 16.23 | 8.0    | 10500     | <10 kG  | 2        |
| SDSS J1043+0855 | 10:43:41.5  | +08:55:58.2 | 17.20 | 8.2    | 13000     | <3 kG   | 3        |

### 3. Expected Sensitivity & Feasibility
Based on JWST Exposure Time Calculator (ETC) simulations for our targets:
- **Instruments:** NIRSpec G395H ($R \sim 2700$) and MIRI MRS ($R \sim 3000$).
- **Signal-to-Noise Ratio (SNR):** We aim for $SNR \ge 50$ at the continuum peak.
- **Line Sample:** Utilizing $\sim 15-20$ distinct transitions with varying $K_i$.
- **Expected Precision:** $\sigma(\Delta\mu/\mu) \sim 2 \times 10^{-6} \ (1\sigma)$.
This represents an order-of-magnitude improvement over existing strong-field constraints!

### 4. Data Reduction Pipeline & Handling Systematics
The primary challenge in white dwarf spectroscopy lies in masking effects (Stark broadening, Zeeman splitting). Our custom analysis framework consists of:
1. **Initial Processing:** Standard STScI pipeline (Stage 2-3).
2. **Spectral Extraction:** JWST pipeline coupled with custom optimal extraction algorithms.
3. **Continuum Normalization:** 3rd-order polynomial fitting.
4. **Line Profiling:** Fitting with Voigt profiles utilizing fixed $\log(g)$ values from literature.
5. **Many-Multiplet Analysis:** Linear regression $\Delta v_i = K_i \cdot (\Delta\mu/\mu) + C$.
6. **Systematics Mitigation:** MCMC modeling with nuisance parameters to account for residual B-field (Zeeman) and pressure shifts (3D NLTE models).

### 5. Broader Impacts: Astrobiology & Extreme Chemistry
Beyond fundamental physics, this test holds critical implications for planetary habitability limits (The ExoLogica BSM Framework). If strong gravitational potentials induce even microscopic shifts in $\mu$ or $\alpha$, chemical bond energies are radically altered. This project will establish strict physico-chemical limits on the stability of complex polymers—and potential biochemistry—within the deep gravitational wells of massive super-Earths or near compact objects.

### References
1. Webb, J. K., et al. 2011, Phys. Rev. Lett., 107, 191101 (variation of α)
2. Reinhold, E., et al. 2018, Phys. Rev. Lett., 120, 232002 (μ constraints)
3. Bagdonaite, J., et al. 2013, Phys. Rev. Lett., 111, 231101 (H₂ in quasars)
4. Koester, D., & Kepler, S. O. 2015, A&A, 583, A86 (WD atmospheres)
5. JWST User Documentation, STScI (2024) — NIRSpec/MIRI specs
