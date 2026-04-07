import subprocess
import sys 
from pathlib import Path

if __name__ == "__main__":
  subprocess.run([sys.executable, "-m", "orizaba_dashboard.py"], cwd = str(Path(__file__).parent))
