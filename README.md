
# 🚀 Multi-GPU Docker Container Launcher with Jupyter & Rocm 

This project provides two Python scripts to manage Docker containers configured for AMD GPUs using the `rocm/vllm:instinct_main` image. Each container is equipped with JupyterLab and assigned a unique GPU render node and port. It is ideal for launching multiple containers for inference/model experimentation on AMD Instinct™ platforms.

---
## Installing requirements:
```bash
pip install -r requirements.txt
```

## 📁 Files

### `pyDocker.py`

Launches 8 separate Docker containers with the following features:

- Uses the `rocm/vllm:instinct_main` image
- Mounts `/home/shepande/models` to `/models` inside the container
- Binds a unique GPU render node (`/dev/dri/renderD*`)
- Installs JupyterLab inside the container 
- Starts JupyterLab with bash shell in the terminal
- Assigns separate ports for Jupyter and VLLM (`echo #VLLM_PORT` inside jupyter lab terminal and it will provide your vllm port)
- Prints the public access URL with Jupyter token

### `removeDocker.py`

Stops and removes the containers launched by `pydocker.py`, named like `vllm_dev_128`, `vllm_dev_136`, etc.

---

## ✅ Prerequisites

- Docker installed and configured
- Access to AMD ROCm devices:
    - `/dev/kfd`
    - `/dev/dri/renderD*`
- Python 3.6+
- Internet access inside containers (for installing JupyterLab)
- Local model directory at: `/home/shepande/models`
- Docker image: `rocm/vllm:instinct_main` (must be available locally)

---

## 🚀 Usage

### 1. Launch Containers

```bash
python3 pydocker.py

```

This will:

- Launch 8 containers
- Assign each a JupyterLab instance on ports starting at 5000
- Print public URLs with tokens for browser access

### 2. Stop and Remove Containers

```bash
python3 removeDocker.py

```

This will:

- Stop each container (if running)
- Remove the container

## 🛠 Configuration

You can customize the following inside `pydocker.py`:

- **GPU IDs used for container bindings**

```python

render_ids = [128, 136, 144, 152, 160, 168, 176, 184]

```

- **Volume mapping**

```python

model_volume = {"/home/shepande/models": {"bind": "/models", "mode": "rw"}}

```

---

## 🔗 Sample Output

```

[vllm_dev_128] launching container…
[vllm_dev_128] installing jupyterlab…
[vllm_dev_128] starting jupyter-lab on port 5000…
[vllm_dev_128] Jupyter URL: http://<public-ip>:5000/?token=<token>
[vllm_dev_128] VLLM_PORT inside container: 8000

```

---

## 🧹 Cleanup Tips

If containers are stuck or not removed:

```bash

docker container prune
docker rm -f $(docker ps -aq --filter "name=vllm_dev_")

```

---

## 👨‍💻 Author

**Shekhar Pandey** : This Entire project was vibecoded.
