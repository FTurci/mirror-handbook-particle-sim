# Handbook of Particle-Based Simulation of Fluids

An introduction to the computational physics of supercooled liquids and glasses.


## Authors

Daniele Coslovich, dcoslovich@units.it

Francesco Turci, f.turci@bristol.ac.uk


## Building the book

Build from the repository folder directly thorugh the command

```shell
jupyter-book build ../handbook
```

# Goals for Trieste

- chapter 1: diffusion 
  - [X] (T) theory rw
  - [X] (C) notebook on random walks
  - [ ] (T) theory Langevin
  - [X] (C) notebook with `numpy`
  - [X] (C) notebook with ` atooms` (possibly `numpy-->atooms`)
  - [ ] (T) Fokker-Planck? Smoluchowski 
  - [X] (C) double well potential : brute force
  - [ ] (C) double well pootential: FFS
  - [X] Reference list + internal links
  - [X] Fix environment
  - [X] Cleanup the notebooks with https://github.com/kynan/nbstripout and removing the checkpoints
  - [X] Fix CI
