# PortableEXE 'No AI' - Unicode Cleaner

**Author:** [Tamino1230](https://github.com/Tamino1230)  
**Online Version:** [tamino1230.github.io/unicode-ai](https://tamino1230.github.io/unicode-ai) (Does the same and works with commands!)

A portable Python script to remove invisible, untypable, or problematic Unicode characters (often found in AI-generated text or causing display issues) from text strings or files.

## Features

*   **Clean Text & Files:** Remove unwanted Unicode characters directly from text input or from entire files.
*   **Default Character List:** Includes a comprehensive list of common zero-width characters, control characters, and other Unicode artifacts.
*   **Customizable Character List:** Use a `.portable` file in the script's directory to specify a custom, comma-separated list of characters (or their Unicode escapes like `\u200b`) to remove.
*   **Detailed Summary:** Reports which characters were removed and how many instances of each.
*   **Encoding Handling:** Attempts to read files as UTF-8, with a fallback to Latin-1. Writes cleaned files in UTF-8.
*   **No External Dependencies:** Runs with a standard Python installation.

## Why use this?

Certain Unicode characters can be problematic:
*   They might be invisible, making text selection and editing difficult.
*   They can break scripts or data parsing processes.
*   They are sometimes unintentionally introduced by AI tools or copy-pasting from various sources.
This script helps ensure your text is clean and consists only of human-readable and standard characters.

## Installation

1.  Ensure you have Python installed on your system.
2.  Download `portable_version.py` to your desired directory.
3.  No further installation or dependencies are required.

## Windows Setup Utility (`setup.bat`)

For Windows users, a `setup.bat` script is provided to install `unicode-ai.exe` (compiled version of the script) as a command-line tool. This allows you to run `unicode-ai` commands directly from any command prompt.

**Note:** The `setup.bat` script requires **administrative privileges** to run. Please right-click on `setup.bat` and select "Run as administrator".

### How to Use `setup.bat`

1.  Navigate to the directory containing `setup.bat`.
2.  Right-click `setup.bat` and choose "Run as administrator".
3.  A menu will appear with the following options:

    *   **`1. Install backup command`**:
        *   Copies `unicode-ai.exe` from the `exe` subdirectory to `%LOCALAPPDATA%\\unicode-ai-setup\\`.
        *   Adds this directory to your user PATH environment variable, allowing you to run `unicode-ai.exe` by typing `unicode-ai` in any command prompt.
        *   **Important:** You may need to restart your command prompt or your system for the PATH changes to take effect.
        *   After installation, you can use commands like `unicode-ai help`, `unicode-ai clean "text"`, etc.

    *   **`2. Uninstall backup command`**:
        *   Removes `unicode-ai.exe` from `%LOCALAPPDATA%\\unicode-ai-setup\\`.
        *   **Note:** This option currently *does not* automatically remove the directory from your PATH. This needs to be done manually if desired (System Properties -> Environment Variables).

    *   **`3. Check if installed`**:
        *   Verifies if `unicode-ai.exe` exists in the installation directory.
        *   Checks if the installation directory is present in your PATH.

    *   **`4. Exit`**:
        *   Closes the setup utility.

## Usage

Run the script from your terminal:

```bash
unicode-ai <command> [args]
```

### Available Commands:

*   **`help`**:
    Displays the help message with all available commands and their descriptions.
    ```bash
    unicode-ai help
    ```

*   **`--version`** or **`--v`**:
    Shows the current version of the application.
    ```bash
    unicode-ai --version
    ```

*   **`clean <text>`**:
    Removes unwanted Unicode characters from the provided text string.
    ```bash
    unicode-ai clean "This is some text ​with invisible chars."
    ```
    (This will also output a summary of removed characters.)

*   **`clean --file <path_to_file>`**:
    Cleans the specified file in-place. The original file will be overwritten with the cleaned content.
    ```bash
    unicode-ai clean --file "my_document.txt"
    ```
    (A summary of removed characters will be printed.)

*   **`clean --file <path_to_file> --usefile`** (or **`--portable`**):
    Cleans the specified file in-place, using a custom list of characters to remove from a `.portable` file located in the same directory as the script.
    ```bash
    unicode-ai clean --file "my_document.txt" --usefile
    ```

*   **`char`**:
    Shows the current default list of characters that the script is configured to remove.
    ```bash
    unicode-ai char
    ```

### The `.portable` File

If you need to customize the list of characters to be removed, create a file named `.portable` in the same directory as `portable_version.py`.

*   **Format:** A plain text file with characters separated by commas.
*   **Content:** You can list literal characters or their Unicode escape sequences (e.g., `\u200b`, `\uFEFF`).
*   **Example `.portable` content:**
    ```
    ​,‌,﻿,X
    ```
    (This would remove Zero Width Space, Zero Width Non-Joiner, Zero Width No-Break Space, and the literal character 'X'.)

When using the `clean --file <path> --usefile` command, the script will use this list instead of its default one.

## Contributing

Feel free to open issues or pull requests on the [GitHub repository](https://github.com/Tamino1230/anti-ai-portable-version) (please update if this is different!).

## License

(Please add your license information here if applicable)
