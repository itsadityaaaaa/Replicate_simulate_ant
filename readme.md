# 🐜 Replicate and Simulate Multiple Ant Robots with MuJoCo

This project allows you to **replicate the Ant robot** multiple times in a grid layout within a single MuJoCo environment and simulate them simultaneously. Each robot is controlled independently using random actions, and the simulation is visualized in real time.

---

## 📦 Features

- Replicates any MuJoCo-compatible robot (e.g., `ant.xml`) into a grid of multiple environments.
- Automatically offsets positions to avoid overlap.
- Supports customizing:
  - Number of robots (`num_envs`)
  - Distance between robots (`env_separation`)
  - Robots per row (`envs_per_row`)
- Simulates the environment using `mujoco` and `mujoco.viewer`.

---


