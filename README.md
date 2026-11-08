# OpenCV Hello World

Loads and displays two sample images with OpenCV.

## Setup

From this project folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install opencv-python
```

In Cursor / VS Code, select the interpreter at `.venv/bin/python`  
(`Cmd+Shift+P` → **Python: Select Interpreter**).

## Run

```bash
source .venv/bin/activate
python hello-world.py
```

Two windows open (dog and cat). Press any key to close them.

Run the script from the project root so the `images/` paths resolve correctly.
