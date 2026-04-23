# Faucetearner: Async XRP Claimer Tool

## 🚀 Getting Started

Follow these steps to get the Faucetearner CLI up and running on your system.

### Prerequisites

- **Python 3.8+**
- **pip** (Python package installer)

### Installation & Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AndrewCrescencio/OFaucetEarner.git
   cd Faucetearner
   ```

2. **Create a virtual environment (recommended):**

   **Git Bash:**

   ```bash
   python -m venv .venv
   source .venv/Scripts/activate
   ```

   **PowerShell:**

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create your `.env` file:**
   In the project root, add only your user numeric cookie value:

   ```dotenv
   COOKIE="132164123123"
   ```

   The script automatically builds this header internally:
   `reg=1; login=1; user=<COOKIE>`

   `COOKIE` must contain digits only.

5. **Run the script:**
   Execute the script from the root directory. The app will automatically read `COOKIE` from `.env`.

   ```bash
   python -m src.main
   ```

   **Optional (override `.env` via argument):**

   ```bash
   python -m src.main "132164123123"
   ```

6. **Stopping the script:**
   Press `CTRL+C` at any time to gracefully stop the application.

## ⚠️ Disclaimer

This tool is designed to automate the process of claiming tokens on Faucetearner.org. It is intended for educational purposes and personal use only. The developers are not responsible for any actions taken on your account. Please use this tool responsibly and in accordance with the website's terms of service.

## ⚖️ License

See [LICENSE](LICENSE) file for more information about the software license.
