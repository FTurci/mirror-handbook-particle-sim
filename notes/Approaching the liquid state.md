# Approaching the liquid state

[TOC]

## Phase diagram of simple substances

- We recall the notion of macroscopic phases of matter
- We contrast a complex example (e.g. water) with a simpler one (argon) to justify our initial focus on simple systems

### Van der Waals equation

- We recall the ideal gas law 
- We present Van der Waals's approach stressing, introducing the notion of mean field theory
- We summarise its key features, successes and failures
- Maxwell's construction for phase equilibria
- **(numerical)** code for the visualisation of Maxwell's construction

We then follow the example of Widom (cite) and take two limit models to illustrate the behaviour of fluids around and way from the critical point.

###  Critical behaviour: lattice gases and the Ising model

- Recall notions of universality and critical behaviour
-  Connect with the Ising model
- **(numerical)** minimal demonstration of the Ising model (in numpy?)

### Dense fluids: hard spheres and crystallisation

- Dense fluids are dominated by hard-core interactions 
- Limit case of hard spheres and entropy driven disorder-order transition
- **(numerical)** minimal demonstration with local Monte-Carlo
- **(numerical)** advanced demonstration with event-driven Monte-Carlo (or event-chain?)
- **(numerical)** `atooms`: general ideas and an example  wrapping the MC simulation backends of teh previous two points

### The equilibrium liquid

- Briefly discuss the  liquid as a dense fluid phase where both attractive and repulsive interactions play a role
-  As we cool a supercritical fluid into the liquid state, the energetic contributions to the free energy become progressively more important
- The specific shape of the interactions between the constituents dictates the nature of the equilibrium correlations.
- **(numerical)** minimal example with a square well potential (as a simple modification of the hard sphere case)
- **(numerical)** intorduction of first correlation function: the radial distribution function and comparison of its featrues for two square-well fluids at same density and temperature but different interaction ranges.

### Interactions and dynamics

- levels of description: *ab initio*, atomistic force fields, coarse-grained interactions

- virial expansion, virial coefficients and many-body interactions
- Toy model: the Lennard-Jones potential
- Forces vs Potentials: general ideas about Molecular Dynamics vs Monte-Carlo simulations
- **(numerical)** start from identical confiuguration of a small system (N=200) of LJ particles and evolve it in MD (using a blackbox with no detail, e.g. `ASE`, possibly wrapped in `atooms`) and the Monte Carlo code above to explore basic differences
- **(numerical)** the mean squared displacement: definition and connection with diffusivities. Comparison between MD and MC ( using previously prepared trajectories and/or custom trajectories).

### Writing Molecular Dynamics codes from scratch

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

















