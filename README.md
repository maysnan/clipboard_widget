# Clipboard App

This is a simple clipboard app that allows you to store and quickly copy two values.

## Setup Instructions

### 1. Install Homebrew (if not already installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
2. Install pyenv and pyenv-virtualenv
bashCopybrew install pyenv
brew install pyenv-virtualenv
3. Add pyenv and pyenv-virtualenv to your shell
For Zsh (default on newer macOS):
bashCopyecho 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
For Bash:
bashCopyecho 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
Restart your terminal or run source ~/.zshrc (for Zsh) or source ~/.bash_profile (for Bash).
4. Install Python and create a virtual environment
bashCopypyenv install 3.9.7
pyenv virtualenv 3.9.7 clipboard-app-env
5. Activate the virtual environment
bashCopypyenv activate clipboard-app-env
6. Install dependencies
bashCopypip install -r requirements.txt
Running the App
To run the app, make sure you're in the project directory and your virtual environment is activated, then run:
bashCopypython clipboard_app.py
Usage

Edit the text fields to set your desired values.
Click the "Copy" button next to a field to copy its content to the clipboard.
The app will minimize to the system tray when closed. Right-click the tray icon to show the app again or quit.

Deactivating the Virtual Environment
When you're done using the app, you can deactivate the virtual environment:

pyenv deactivate

This README.md file provides a step-by-step guide for your colleagues to set up the environment, including installing pyenv and the pyenv-virtualenv extension. It also includes instructions for running the app and basic usage information.

