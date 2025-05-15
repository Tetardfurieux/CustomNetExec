import os
import sys
import nxc


current_dir = os.getcwd()

# Set paths relative to current directory
NXC_PATH = os.path.join(current_dir, ".nxc")
TMP_PATH = os.path.join(current_dir, "nxc_hosted")

os.environ["TEMP"] = TMP_PATH
os.environ["TMP"] = TMP_PATH
os.environ["TMPDIR"] = TMP_PATH
os.environ["PIP_TMPDIR"] = TMP_PATH
os.environ["PYTHONTEMP"] = TMP_PATH
os.environ["XDG_DATA_HOME"] = TMP_PATH
os.environ["XDG_CONFIG_HOME"] = TMP_PATH
os.environ["XDG_CACHE_HOME"] = TMP_PATH

CERT_PATH = os.path.join(NXC_PATH, "nxc.pem")
CONFIG_PATH = os.path.join(NXC_PATH, "nxc.conf")
WORKSPACE_DIR = os.path.join(NXC_PATH, "workspaces")
DATA_PATH = os.path.join(os.path.dirname(nxc.__file__), "data")
