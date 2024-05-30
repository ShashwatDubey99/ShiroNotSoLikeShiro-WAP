# Text-to-Image Frontend for Stable Diffusion

This project is a Flask-based web frontend for generating images from text using the Stable Diffusion model. Users can input their text prompts and configure various options via checkboxes to customize the generated images.

## Features

- **Text Input:** Enter text prompts to describe the desired image.
- **Checkbox Options:** Customize image generation parameters.
- **Image Preview:** View generated images directly on the web page.
- **Download Images:** Save the generated images to your local machine.

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/text2img-stable-diffusion.git](https://github.com/ShashwatDubey99/ShiroNotSoLikeShiro-WAP
    cd text2img-stable-diffusion
    ```

2. **Set up a virtual environment:**
    Start Your ComfyUI And The The webui.py file



## Configuration

Create a `.env` file in the project root and add the necessary environment variables. Example:
```env
SECRET_KEY=your_secret_key
STABLE_DIFFUSION_MODEL_PATH=/path/to/stable-diffusion
