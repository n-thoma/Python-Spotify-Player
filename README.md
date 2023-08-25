# Python-Spotify Player

[![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/downloads/)

A simple Python script to control playback and play specific songs on your Spotify account using the Spotify Web API.

**ONLY WORKS IF YOU HAVE SPOTIFY PREMIUM!!**

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Introduction

The Python-Spotify Player is a Python script that leverages the Spotify Web API to control playback and play specific songs on your Spotify account. It utilizes the `spotipy` library for authentication and interaction with the Spotify API. With this script, you can easily play your favorite songs without leaving the terminal.

---

## Features

- Authenticate with your Spotify account.
- Play specific songs by name.
- Control playback, including play, pause, skip, and more.

---

## Getting Started

### Prerequisites

Before using the Python-Spotify Player, ensure you have the following installed:

- Python 3.11 or higher: [Download Python](https://www.python.org/downloads/)
- Required Python libraries: `requests` and `spotipy`

You can install the required libraries using the following command:

```bash
pip install requests spotipy
```

### Installation

1. Clone this repository to your local machine using:

    ```bash
    git clone https://github.com/n-thoma/Python-Spotify-Player.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Python-Spotify-Player
    ```

3. Edit the `config.py` file with your Spotify client ID and secret.

4. Set up your Spotify for Developers App:

	1. Head over to [Spotify Developer](https://developer.spotify.com/).
	
	2. Click on your profile and select [Dashboard](https://developer.spotify.com/dashboard)
	
	3. Click on [Create App](https://developer.spotify.com/dashboard/create)
	
	4. When creating the App, **make sure the Redirect URI matches the REDIRECT_URI in spotify.py**
	
	5. Create the App and Save.

5. Run the script:

    ```bash
    python spotify.py
    ```

---

## Usage

1. Run the script using the installation instructions.
2. The script will prompt you to authorize your Spotify account.
	- You shouldn't have to authorize yourself again unless you change `SCOPE`.
3. Follow the on-screen instructions to input the authorization code.
4. Use the script to play specific songs or control playback.
	- Do this by calling `play_song(token, "SONG NAME")`

---

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for improvements or new features.

---

## Acknowledgments

- [spotipy](https://github.com/plamere/spotipy) library by Paul Lamere for Spotify API interaction.
- The script was inspired by the need for a simple command-line Spotify player.

---

**n-thoma(https://github.com/n-thoma)**
