<div align="center">

![header](https://capsule-render.vercel.app/api?type=waving&height=190&color=0:0f766e,55:2563eb,100:111827&text=Clihef&fontColor=ffffff&fontSize=48&fontAlignY=36&desc=Robotics%20%7C%20Reinforcement%20Learning%20%7C%20Control&descAlignY=56&descSize=16)

### Robotics RL learner with a control background

I am working toward embodied intelligence, robot reinforcement learning, and control-oriented autonomy.  
Currently focusing on **Gymnasium-Robotics**, **MuJoCo**, **SAC + HER**, and continuous-control robot tasks.

[![GitHub](https://img.shields.io/badge/GitHub-Clihef-111827?style=flat-square&logo=github)](https://github.com/Clihef)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![MuJoCo](https://img.shields.io/badge/MuJoCo-0F766E?style=flat-square)](https://mujoco.org/)
[![Gymnasium](https://img.shields.io/badge/Gymnasium--Robotics-2563EB?style=flat-square)](https://robotics.farama.org/)

</div>

---

## About Me

- Undergraduate background in automation and control.
- Incoming graduate study direction: control science and engineering.
- Interested in robot learning, continuous control, goal-conditioned reinforcement learning, and simulation-based robotics.
- Previous research/project experience includes Dueling DQN, Fetch robot tasks with SAC + HER, morphing quadrotor hardware, and mobile manipulator consensus control.

## Current Focus

```text
Robot Reinforcement Learning
├── Goal-conditioned RL
├── Sparse reward learning
├── Hindsight Experience Replay
├── Off-policy continuous control
└── MuJoCo / Gymnasium-Robotics simulation
```

## Featured Projects

### Fetch SAC + HER Robotics Reproduction

[![Repo](https://github-readme-stats.vercel.app/api/pin/?username=Clihef&repo=fetch-sac-her-robotics&theme=default&hide_border=true)](https://github.com/Clihef/fetch-sac-her-robotics)

Reproduced Fetch robot manipulation tasks with **Gymnasium-Robotics + MuJoCo + Stable-Baselines3**.

- Implemented a general SAC + HER training pipeline for `FetchReach-v4`, `FetchPush-v4`, `FetchSlide-v4`, and `FetchPickAndPlace-v4`.
- Used `MultiInputPolicy` to process GoalEnv dictionary observations: `observation`, `achieved_goal`, and `desired_goal`.
- Used HER goal relabeling to improve sample efficiency under sparse reward.
- Recorded evaluation curves, success rate, summary files, and MuJoCo GIF visualizations.
- Results: Push and PickAndPlace reached above 0.90 success rate; Slide showed improvement but remained less stable due to contact dynamics.

### Dueling DQN Undergraduate Thesis

Applied value-based reinforcement learning to a dynamic decision-making problem.

- Built an MDP formulation around state, action, reward, and termination conditions.
- Used Dueling DQN to separate state-value and action-advantage estimation.
- Compared discrete-action value learning with actor-critic continuous-control methods used in robot tasks.

### Morph-Rotor Aerial Grasping Platform

Participated in the development and debugging of a morphing quadrotor capable of aerial grasping and transportation.

- Worked on hardware selection, wiring, soldering, and full-system debugging.
- Helped iterate multiple versions of the platform for stable flight, morphing, grasping, and transport.
- Studied control adjustments related to changing arm length, torque allocation, and PID tuning.

### Mobile Manipulator Consensus Control

Implemented and analyzed consensus-control strategies for mobile manipulators.

- Studied leaderless and leader-following consensus settings.
- Considered task-space dynamics, nonholonomic constraints, and null-space simplification.
- Added artificial-potential-field obstacle avoidance in simulation and verification.

## Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)
![MuJoCo](https://img.shields.io/badge/MuJoCo-0F766E?style=for-the-badge)
![Gymnasium](https://img.shields.io/badge/Gymnasium--Robotics-2563EB?style=for-the-badge)
![Stable-Baselines3](https://img.shields.io/badge/Stable--Baselines3-111827?style=for-the-badge)
![MATLAB](https://img.shields.io/badge/MATLAB-0076A8?style=for-the-badge)

</div>

## GitHub Overview

<div align="center">

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Clihef&show_icons=true&hide_border=true&theme=default&rank_icon=github)

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Clihef&layout=compact&hide_border=true&theme=default)

</div>

## Learning Notes

I use this profile to record practical learning around robotics and reinforcement learning:

- Reading robot task source code instead of only running demos.
- Understanding how MDP definitions appear in environment implementations.
- Separating simulation reproduction from real-robot deployment claims.
- Keeping experiment results reproducible with scripts, metrics, curves, and visualizations.

---

<div align="center">

Focused on building small but explainable robotics learning projects.

</div>
