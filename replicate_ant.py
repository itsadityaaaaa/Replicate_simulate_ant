import xml.etree.ElementTree as ET
import mujoco
import mujoco.viewer
import numpy as np
import time
import os

def simulate_multiple_robots(
    model_xml_path,
    num_envs=1,
    env_separation=3.0,
    envs_per_row=2,
    simulation_steps=10,
    time_per_step=0.1
):
    # Step 1: Replicate XML and save
    replicated_xml_path = replicate_robot_grid(
        model_xml_path=model_xml_path,
        num_envs=num_envs,
        env_separation=env_separation,
        envs_per_row=envs_per_row,
        output_xml_path="replicated_model.xml"
    )

    # Step 2: Load the new model
    model = mujoco.MjModel.from_xml_path(replicated_xml_path)
    data = mujoco.MjData(model)

    # Step 3: Start Viewer
    with mujoco.viewer.launch_passive(model, data) as viewer:
        for step in range(simulation_steps):
            # Apply random control to all actuators
            data.ctrl[:] = np.random.uniform(-0.1, 0.1, size=model.nu)

            mujoco.mj_step(model, data)
            time.sleep(0.02)  # Adjust speed of sim

            if viewer.is_alive:
                viewer.sync()
            else:
                break


simulate_multiple_robots(
    model_xml_path="ant.xml",
    num_envs=1,
    env_separation=4.0,
    envs_per_row=3,
    simulation_steps=100
)
