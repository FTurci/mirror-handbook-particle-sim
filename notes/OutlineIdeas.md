
# Handbook Structure
[TOC]


## Diffusion


### Single-particle diffusion

- Brownian motion and random walks
- The Langevin equation
- The Fokker-Planck equation
- **(numerical)** Implementing random walks in `numpy` 
- **(numerical)** Implementing the Langevin dynamics as an `atooms` backend
- **(numerical)** Probability distribution of the displacement and its moments
- Diffusion in external double-well potential
- **(numerical)** Naive direct simulation of a Brownian particle in a double-well potential
- **(numerical)** Forward flux sampling of a Brownian particle in a double-well potential

### Single-polymer diffusion

- Polymers as a random walk 
- **(numerical)** Noninteracting bead-spring model of a single polymer


## Approaching the liquid state


### Phase diagram of simple substances

- We recall the notion of macroscopic phases of matter
- We contrast a complex example (e.g. water) with a simpler one (argon) to justify our initial focus on simple systems

### Van der Waals equation

- We recall the ideal gas law 
- We present Van der Waals's approach stressing, introducing the notion of mean-field theory
- We summarise its key features, successes and failures
- Maxwell's construction for phase equilibria
- **(numerical)** code for the visualisation of Maxwell's construction

We then follow the example of Widom (cite) and take two limit models to illustrate the behaviour of fluids around and away from the critical point.

###  Critical behaviour: lattice gases and the Ising model

- Recall notions of universality and critical behaviour
-  Connect with the Ising model
- **(numerical)** minimal demonstration of the Ising model (in `numpy`?)

### Dense fluids: hard spheres fluids and crystals

- Dense fluids are dominated by hard-core interactions 
- Limit case of hard spheres and entropy-driven disorder-order transition
- **(numerical)** minimal demonstration with local Monte-Carlo
- **(numerical)** advanced demonstration with event-driven Monte-Carlo (or event-chain?)
- **(numerical)** `atooms`: general ideas and an example  wrapping the MC simulation backends of the previous two points

## Interactions and dynamics

### Particle-based molecular dynamics from scratch

- levels of description: *ab initio*, atomistic force fields, coarse-grained interactions

- virial expansion, virial coefficients and many-body interactions
- Toy model: the Lennard-Jones potential
- Forces vs Potentials: general ideas about Molecular Dynamics vs Monte-Carlo simulations
- **(numerical)** start from identical configuration of a small system (N=200) of LJ particles and evolve it in MD (using a blackbox with no detail, e.g. `ASE`, possibly wrapped in `atooms`) and the Monte Carlo code above to explore basic differences
- **(numerical)** the mean squared displacement: definition and connection with diffusivities. Comparison between MD and MC (using previously prepared trajectories and/or custom trajectories).

- Hamiltonian equations of motion
- The problem of discretisation
- Energy in the system: internal, potential, kinetic and connection with the temperature
- **(numerical)** failure of standard  Euler's method in keeping the energy constant. 
- Symplectic algorithms
- **(numerical)** Semi-implicit Euler's method
- **(numerical)** implementing the velocity Verlet algorithm and simulation of a Lennard-Jones system
- Thermostatting the system: deterministic vs stochastic
- **(numerical)** implementing a simple Nosé-Hoover thermostat
- **(numerical)** implementing a Langevin thermostat with Euler-Maruyama

### Ensembles and coexistence 

- Thermal equilibrium: the canonical ensemble and the isothermal-isobaric ensemble
- **(numerical)** Calculating the average energy using Metropolis Monte-Carlo and a Langevin thermostat
- The microcanonical ensemble
- Widom's insertion and the grand-canonical ensemble
- Phase coexistence and interfaces
- **(numerical)** Liquid-gas coexistence in the Lennard-Jones fluid using elongated boxes
- **(numerical)** Liquid-gas coexistence in the Lennard-Jones fluid using the GCMC

##  Measuring correlations

### Quantifying static correlations 
- radial distribution functions
- angular correlations 
- structural motifs and bond order
- virial coefficients
- **(numerical)** Implementing 2 and 3-body correlation functions
- **(numerical)** Voronoi tessellations
- **(numerical)** Bond-order parameters
- **(numerical)** Virial coefficients from small-box simulations

### Quantifying dynamical correlations
- intermediate scattering functions
- **(numerical)** Algorithm for the self part of the intermediate scattering function + `atooms.postprocessing`
- Relaxation times and viscosities
- **(numerical)** Relaxation times of the Lennard-Jones fluid at  different temperatures
- **(numerical)** Green-Kubo calculation of viscosities at different temperatures
- Overlap order parameter
- **(numerical)** Algorithm for the overlap: comparison with the ISF for a fluid of repulsive spheres under Langevin dynamics

## Atomistic fluids

### Force fields and their parametrizations

- "First-principles" and force fields
- Embedded-atom potentials and the  OpenKIM database
- **(numerical)** Example of an EAM simulation using `lammps`

### The case of water

- Coarse-grained potentials: the case of water
- **(numerical)** A simple model for water : mW
- **(numerical)** A refined model for water: TIP4P using `lammps` 
- **(numerical)** Comparison of structure and dynamics between TIP4P and mW

##  Soft-matter fluids

### Colloids: symmetries and approximations 

- Example: essential ingredients of the DLVO theory
- **(numerical)** Non-spherical particles interacting via the Gay-Berne potential
- Pacthy colloids
- **(numerical)** Modelling a solution of dumbells

### Coarse-grained models of polymers

- Models of interacting polymers, entanglement and topology
- **(numerical)** FENE model of a liquid of short polymeric chains  

### Colloid-polymer mixtures

- Coarse-graining and depletion forces
- **(numerical)** Explore depletion forces for a hard-sphere fluid in a rigid box
- **(numerical)** Explicit-solvent simulation of a colloid-polymer mixture
- **(numerical)** Asakura-Oosawa model  of a colloid-polymer mixture

## Metastability and nonequilibrium

### Metastable liquids

- Metastability: lifetimes and time averages
- Homogeneous nucleation
- Heterogeneous nucleation
- **(numerical)** Seeding a crystal

### Crossing the spinodal 

- Coarsening and growth laws
- **(numerical)** Simple demonstration using Ising-model
- Spinodal and mechanical stability
- **(numerical)** Illustration of a gel coarsening using the Morse potential

### Glass transition

- Slow dynamics
- Strong and fragile glasses
- **(numerical)** Relaxation times of a Lennard-Jones binary mixture
- **(numerical)** BKS silica (at least where it looks strong...)
- (Semi)-empirical laws  and phenomenological models
- **(numerical)** Comparison of different fitting approaches
- (Free) Energy landscape 
- **(numerical)** Swap Monte-Carlo
- Structural motifs
- **(numerical)** Structural changes in dense repulsive spheres.

### Active fluid

- Vicsek model
- **(numerical)** Elementary code for 2d vicsek model simulations
- Noninteracting active Brownian particles
- **(numerical)** Study of the mean squared displacement of noninteracting ABPs
- Repulsive active Brownian Particles and Motility Induced Phase separation
- **(numerical)** Repulsive active Brownian disks at high activity.



## Obviously missing stuff

- driven systems (e.g. shear) 
- deformations/elasticity
- property of crystals
- Surface tensions
- ...







