# Erratic motion: random walks

## Introduction

A stochastic (i.e. *random*) process is a temporal **sequence** of random variables. Possibly the simplest instance of stochastic processes are **random walks**, where the successive elements of the sequence are defined by the following recursive relation

$$
\begin{equation}
x_{n+1} = x_{n}+l \xi_n,
\end{equation}
$$ (rw)

where $\xi_n$ is a random variable with zero average $\langle \xi_n\rangle=0$ and unit variance $\langle \xi_n \xi_{n\prime}\rangle=1$ and $\ell$ the scale for the random steps.

The index $n$ represents a discretisation of time, so that one can rewrite Eq.{eq}`rw` as 

$$
\begin{equation}
x_{t+\Delta t} = x_{t}+l \xi_t,
\end{equation}
$$

The erratic motion of a random walker constitutes a minimal model for what is called **Brownian motion**. 


```{admonition} Historical note: Brownian motion
:class: history dropdown


In 1827 Robert Brown reported about his optical microscope observations of the irregular motions of pollen grains suspended in water. His serendipituous discovery was originally motivated by a biological motive: to understand the machanisms of reproduction in plants.

What he found, instead, was that pollen in water exhibited an erratic motion, regardless of the kind of plant considered, whether the plant was alive or not and regardless of whether the plant was believed to have sexual organs.

Link to the original notes by Brown  [&rarr;](https://sciweb.nybg.org/science2/pdfs/dws/Brownian.pdf) .

Brown did not attempt an explanation, but did not exclude that the motion was inanimated.

Only much later Albert Einstein provided a physical description that could rationalise Brownian motion. Einstein did this in his seminal 1905 article in *Annalen der Physik* (see a later account in English in {cite}`einstein1956investigations`).

```

When time is not discretised, random walks are treated rigorously within the mathematical theory of [Wiener processes](https://en.wikipedia.org/wiki/Wiener_process).

Here we characterise the key properties of random walks, and we do so by focusing initially on simplest case of **one-dimensional random walks**


## One dimensional motion and its statistics

In one dimension, eq.{eq}`rw` illustrates the motion of a particle on a line, kicked to the left or the right with equal proability and always performing a step of length $\ell$.







## Mean squared displacement (MSD)





Tab set here (to compare algorithms):
````{tab-set}
```{tab-item} Tab 1 title
My first tab
```

```{tab-item} Tab 2 title
My second tab with `some code`!
```
````


```{toggle}
Some hidden toggle content!

![](../images/cool.jpg)
```


```{admonition} Proof
:class: dropdown

$$
\begin{equation}
y = f(x)
\end{equation}
$$

![](../images/cool.jpg)
```

```{bibliography}
:filter: docname in docnames
```