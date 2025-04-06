import mujoco
import glfw
import numpy as np
import os
import sys
from mujoco import viewer


MODEL_XML_PATH = "replicated_ant.xml"  


if not os.path.exists(MODEL_XML_PATH):
    print(f"Model file {MODEL_XML_PATH} not found.")
    sys.exit(1)

# Load the model
model = mujoco.MjModel.from_xml_path(MODEL_XML_PATH)

# Create the data object
data = mujoco.MjData(model)

# Simulation function
def run_simulation():
    with viewer.launch_passive(model, data) as viewer_window:
        mujoco.mj_resetData(model, data)

        # Optionally set camera to track the first torso
        if viewer_window.cam.type == mujoco.mjtCamera.mjCAMERA_TRACKING:
            try:
                viewer_window.cam.trackbodyid = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "torso")
            except:
                pass  

        # Run the simulation loop
        while viewer_window.is_running():
            # Apply random control input (replace with real policy later)
            data.ctrl[:] = np.random.uniform(-0.1, 0.1, size=model.nu)

            mujoco.mj_step1(model, data)
            mujoco.mj_step2(model, data)

            
            viewer_window.sync()
            

if __name__ == "__main__":
    run_simulation()
