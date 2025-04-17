#!/usr/bin/env python3
import subprocess

def cleanup_containers():
    # The same IDs used when launching
    render_ids = [128, 136, 144, 152, 160, 168, 176, 184]

    for rid in render_ids:
        name = f"vllm_dev_{rid}"
        print(f"Stopping container {name}…")
        try:
            subprocess.run(["docker", "stop", name], check=True, stdout=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            print(f"  ⚠️  Could not stop {name} (it may not be running)")

        print(f"Removing container {name}…")
        try:
            subprocess.run(["docker", "rm", name], check=True, stdout=subprocess.DEVNULL)
            print(f"  🗑  {name} removed")
        except subprocess.CalledProcessError:
            print(f"  ⚠️  Could not remove {name} (it may not exist)")

    print("Cleanup complete.")

if __name__ == "__main__":
    cleanup_containers()
