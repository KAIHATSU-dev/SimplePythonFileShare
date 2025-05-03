NOTE: THIS WAS GENERATED THROUGH GITHUB-COPILOT, THE CODE wAS WRITTEN BY ME,
BUT I USED COPILOT TO ADD RELEVANT COMMENTS AND THE README.

# SimplePythonFileShare

A simple Python script to share files from a directory on your local network via HTTP, with a QR code for easy access from mobile devices.

## Features

- Serves files from a specified directory over HTTP
- Generates a QR code for quick access
- Configurable directory and port
- Security warning for local network use only

## Requirements

- Python 3.7+
- See `requirements.txt` for Python dependencies

## Installation

1. Clone this repository or download the files.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the server from the command line:

```bash
python -m main.app --dir <directory_to_share> --port <port_number>
```

- `--dir` (optional): Directory to share (default: your OneDrive folder)
- `--port` (optional): Port to use (default: 8010)

Example:

```bash
python -m main.app --dir C:\Users\dev20\Documents --port 9000
```

Scan the generated QR code or open the displayed URL in your browser to access the shared files.

## Security Warning

**Do not use this server on untrusted or public networks. Anyone on your local network can access the shared files.**

## License

MIT License
