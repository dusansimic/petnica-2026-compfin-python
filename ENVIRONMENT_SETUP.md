# Environment Setup

## Python Installation

Python 3.11 or newer.

### Windows
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run installer, **check "Add Python to PATH"**
3. Click "Install Now"
4. Verify: open Command Prompt, run `python --version`

If that reports `'python' is not recognized...` (or opens the Microsoft Store),
use the `py` launcher instead — it ships with the installer and works even when
Python is not on PATH:

```bat
py --version
```

Everywhere below that a Windows command starts with `python` or `pip`, the `py`
form is given as the alternative. Use one or the other consistently.

### macOS
```bash
# Using Homebrew (install from https://brew.sh if needed)
brew install python3

# Verify
python3 --version
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Verify
python3 --version
```

Fedora:
```bash
sudo dnf install python3 python3-pip
```

## VS Code Installation

All downloads come from
[code.visualstudio.com/download](https://code.visualstudio.com/download).

### Windows
1. Download the **Windows** installer (`VSCodeUserSetup-x64-*.exe`)
2. Run it and follow the prompts
3. Keep "Add to PATH" checked so the `code` command works in a terminal

### macOS
Requires macOS 12.0 or newer. Under the **Mac** button the page lists three
`.dmg` builds:

| Build | Chip | File |
|---|---|---|
| **Universal** | both — safe default | `VSCode-darwin-universal.dmg` |
| **Apple silicon** | M1 / M2 / M3 / M4 | `VSCode-darwin-arm64.dmg` |
| **Intel chip** | pre-2020 Intel Macs | `VSCode-darwin-x64.dmg` |

Universal packs both architectures — bigger download, runs natively everywhere.
The chip-specific builds are smaller. Apple silicon builds do **not** run on
Intel Macs; an Intel build does run on Apple silicon, but through Rosetta 2
translation instead of natively.

Check your chip:  → About This Mac, or run `uname -m` (`arm64` = Apple
silicon, `x86_64` = Intel).

1. Download the `.dmg` for your chip
2. Double-click it to mount the disk image
3. Drag **Visual Studio Code.app** into the `Applications` folder
4. Eject the disk image, then launch VS Code from `Applications`
5. `Cmd+Shift+P` → "Shell Command: Install 'code' command in PATH"

The **CLI** entries on the download page are the headless `code` tool for
tunnels and remote work, not the editor — skip them.

### Linux
Pick the file matching your distribution:

- **Ubuntu / Debian / Mint** — `.deb`
- **Fedora / RHEL / openSUSE** — `.rpm`
- **anything else** — `.tar.gz`

Double-click the downloaded `.deb` or `.rpm` to install it through the desktop's
graphical installer.

The `.tar.gz` build needs no installation — unpack it and run the binary:

```bash
tar -xzf code-stable-x64-*.tar.gz
cd VSCode-linux-x64
./code
```

### VS Code Extensions

Install from the Extensions tab (`Ctrl+Shift+X`, `Cmd+Shift+X` on macOS), or from
a terminal:

```bash
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension mechatroner.rainbow-csv
```

- `ms-python.python` — Python support (running, debugging, interpreter selection)
- `ms-python.vscode-pylance` — autocomplete and type checking
- `mechatroner.rainbow-csv` — colored columns when viewing CSV files

## Virtual Environment (recommended)

Keeps project packages separate from the system Python. On Debian/Ubuntu and
Fedora a plain `pip install` into the system Python fails with
`error: externally-managed-environment` — a virtual environment avoids that.

```bash
# Create (run once, in the project directory)
python -m venv .venv        # Windows
py -m venv .venv            # Windows, if python is not found
python3 -m venv .venv       # macOS / Linux

# Activate (every new terminal)
.venv\Scripts\activate      # Windows (Command Prompt)
source .venv/bin/activate   # macOS / Linux
```

In VS Code: `Ctrl+Shift+P` → "Python: Select Interpreter" → pick the one in
`.venv`.

## Python Packages

```bash
# Windows
pip install "pandas>=2,<3" matplotlib requests yfinance openpyxl

# Windows, if pip is not found
py -m pip install "pandas>=2,<3" matplotlib requests yfinance openpyxl

# macOS / Linux
pip3 install "pandas>=2,<3" matplotlib requests yfinance openpyxl
```

The quotes matter — without them the shell interprets `<` and `>` as
redirection.

To pin the exact version used in the course:

```bash
pip install pandas==2.3.3
# or, on Windows without pip on PATH:
py -m pip install pandas==2.3.3
```

Newer pandas releases add features but can also introduce breaking changes, so
course examples are written against pandas 2.

- `pandas` — tabular data
- `matplotlib` — plots
- `requests` — HTTP requests
- `yfinance` — market data from Yahoo Finance
- `openpyxl` — reading and writing `.xlsx` files (used by pandas)

Verify installation:

```bash
python -c "import pandas, matplotlib, requests, yfinance, openpyxl; print(pandas.__version__)"

# Windows, if python is not found
py -c "import pandas, matplotlib, requests, yfinance, openpyxl; print(pandas.__version__)"
```

Prints the pandas version if everything is installed.
