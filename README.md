# Neural Network Receptive Field Calculator

A simple Flask web application that helps you understand how different layers in a Convolutional Neural Network (CNN) affect the receptive field.

## What is a Receptive Field?

The receptive field is the area of the input that affects a particular neuron in a neural network. For CNNs, understanding receptive fields is crucial because:

- **Convolutional layers** increase the receptive field based on kernel size and stride
- **Pooling layers** can dramatically increase the receptive field
- The receptive field determines how much context a neuron "sees" from the input

## Features

- Add convolutional layers with customizable kernel size, stride, and padding
- Add max pooling layers with automatic stride calculation
- Real-time calculation of receptive field parameters
- Visual representation of how each layer affects the receptive field
- Simple, intuitive web interface

## How to Run

### Prerequisites
- Python 3.13+
- UV package manager

### Installation & Setup

1. **Install dependencies using UV:**
   ```bash
   uv sync
   ```

2. **Run the Flask application:**
   ```bash
   uv run python app.py
   ```

3. **Open your browser and go to:**
   ```
   http://localhost:5000
   ```

## How to Use

1. **Add a Convolutional Layer:**
   - Select "Convolutional Layer" from the dropdown
   - Set kernel size (e.g., 3 for 3x3 convolution)
   - Set stride (usually 1 for convolution)
   - Set padding (0 for no padding, 1 for same padding with 3x3 kernel)
   - Click "Add Layer"

2. **Add a Pooling Layer:**
   - Select "Max Pooling Layer" from the dropdown
   - Set kernel size (e.g., 2 for 2x2 pooling)
   - Leave stride empty to use kernel size as stride
   - Set padding (usually 0 for pooling)
   - Click "Add Layer"

3. **View Results:**
   - Each layer shows its parameters and receptive field information
   - **RF Size**: The size of the receptive field at that layer
   - **Jump**: How much the receptive field moves between adjacent neurons
   - **Center**: The center position of the receptive field

## Example Network

Try building this simple network to see how receptive fields grow:

1. **Conv Layer**: Kernel=3, Stride=1, Padding=1
2. **Pool Layer**: Kernel=2, Stride=2, Padding=0
3. **Conv Layer**: Kernel=3, Stride=1, Padding=1

You'll see how the receptive field grows from 1 → 3 → 6 → 10 pixels!

## Technical Details

The application uses the standard receptive field calculation formulas:

- **Output Receptive Field**: `n_out = (n_in - 1) * stride + kernel_size`
- **Output Jump**: `j_out = j_in * stride`
- **Output Center**: `r_out = r_in + (kernel_size - 1)/2 - padding * j_in`

Where:
- `n_in/n_out`: Input/output receptive field size
- `j_in/j_out`: Input/output jump
- `r_in/r_out`: Input/output center position

## Files Structure

- `app.py` - Main Flask application with receptive field calculation logic
- `templates/index.html` - Web interface
- `pyproject.toml` - Project dependencies and configuration
- `README.md` - This file

## Learning Resources

- [Understanding Receptive Fields in CNNs](https://distill.pub/2019/computing-receptive-fields/)
- [Receptive Field Calculator](https://fomoro.com/research/article/receptive-field-calculator)
- [CNN Receptive Field Mathematics](https://medium.com/mlreview/a-guide-to-receptive-field-arithmetic-for-convolutions-aa0b32364e71)
