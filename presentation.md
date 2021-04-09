---
title: "Reproducible Engineering"
author: "Mitchell Paulus"
date: "2021-04-08"
---

## Background

- Command Commissioning
- Building Optimization Group

## Reproducible Science

> "Scientific research involves using the scientific method, which seeks
> to objectively explain the events of nature in a reproducible way." -
> Wikipedia


## Replication Crisis

- Ideas need to stand up to *repeated experimentation* by others.
- Engineering analysis (data and code) should be easily inspected and
  repeatable, but often isn't.

## Industry

- Clients deserve to have access to:
    - data
    - analysis
    - results

- at any time
- *including the past*

## Reproducible Engineering

Built on two foundations:

1. Version Control
2. Build systems
    - *Anything that can be derived shall be derived.*

## Prerequisites

1. Version Control: You've used a computer
2. Build Systems: You've written a for loop
    - You haven't? Recommend start with *Python*

## Live Demo

Common workflow:

- Run model on data
- Analyze results
- Include results in paper/report

## Live Demo

Our example:

- Run EnergyPlus simulation model
- Produce visualization
- Build paper using Latex or Markdown/Pandoc

## Live Demo

- Start with baseline - no reproducibility steps taken
- Add version control
- Add build script
- Add build system(s)
- Discuss Containerization

## Version Control

- Git
- GitHub

## Tell me how to get started!

- GitHub Desktop

## Build Systems

Improve on build scripts

- Only build what you you need
- Parallelization

## Tell me how to get started!

- `make`: Domain specific language
- `redo`: Shell or other interpreted language
- `doit`: Python

## Containerization

- Bundle up code and all *dependencies, including the OS*.

## Other cool things to explore

- Overleaf
- Docker
- Windows Subsystem for Linux
- My blog/websites/YouTube channel

