# Neural Network Receptive Field & Parameter Calculator

A comprehensive Flask web application that helps you understand how different layers in a Convolutional Neural Network (CNN) affect both the receptive field and parameter count.

## What is a Receptive Field?

The receptive field is the area of the input that affects a particular neuron in a neural network. For CNNs, understanding receptive fields is crucial because:

- **Convolutional layers** increase the receptive field based on kernel size and stride
- **Pooling layers** can dramatically increase the receptive field
- The receptive field determines how much context a neuron "sees" from the input

## What are Parameters?

Parameters are the learnable weights and biases in your neural network:

- **Weights**: The kernel values that get learned during training
- **Biases**: Additional learnable parameters for each output channel
- **Total Parameters**: Sum of all weights and biases across the network

## Features

- **Receptive Field Analysis**:
  - Add convolutional layers with customizable kernel size, stride, and padding
  - Add max pooling layers with automatic stride calculation
  - Real-time calculation of receptive field parameters
  - Visual representation of how each layer affects the receptive field

- **Parameter Counting**:
  - Automatic calculation of weights and biases for each layer
  - Total network parameter count
  - Formula display showing how parameters are calculated
  - Support for different input channel configurations (RGB, grayscale, etc.)

- **Network Design**:
  - Set input channels (1 for grayscale, 3 for RGB, 4 for RGBA)
  - Configure output channels for convolutional layers
  - Real-time network summary with key statistics

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

### 1. Configure Input Channels
- Select the number of input channels (1 for grayscale, 3 for RGB, 4 for RGBA)
- This affects parameter calculations for the first layer

### 2. Add Convolutional Layers
- Select "Convolutional Layer" from the dropdown
- Set kernel size (e.g., 3 for 3x3 convolution)
- Set stride (usually 1 for convolution)
- Set padding (0 for no padding, 1 for same padding with 3x3 kernel)
- Set output channels (leave empty to keep same number)
- Click "Add Layer"

### 3. Add Pooling Layers
- Select "Max Pooling Layer" from the dropdown
- Set kernel size (e.g., 2 for 2x2 pooling)
- Leave stride empty to use kernel size as stride
- Set padding (usually 0 for pooling)
- Click "Add Layer"

### 4. View Results
Each layer shows comprehensive information:

**Receptive Field Information:**
- **RF Size**: The size of the receptive field at that layer
- **Jump**: How much the receptive field moves between adjacent neurons
- **Center**: The center position of the receptive field

**Parameter Information:**
- **Weights**: Number of learnable weights
- **Biases**: Number of learnable biases
- **Total**: Total parameters for this layer
- **Formula**: Mathematical formula showing how parameters are calculated

**Network Summary:**
- Total number of layers
- Total network parameters
- Final receptive field size
- Output channels

## Example Networks

### Simple CNN
1. **Conv Layer**: Kernel=3, Stride=1, Padding=1, Channels=3→16 → RF: 3, Params: 448
2. **Pool Layer**: Kernel=2, Stride=2, Padding=0 → RF: 6, Params: 0
3. **Conv Layer**: Kernel=3, Stride=1, Padding=1, Channels=16→32 → RF: 8, Params: 4,640

**Total Parameters**: 5,088

### VGG-like Structure
1. **Conv**: K=3, S=1, P=1, C=3→64 → RF: 3, Params: 1,792
2. **Conv**: K=3, S=1, P=1, C=64→64 → RF: 5, Params: 36,928
3. **Pool**: K=2, S=2, P=0 → RF: 10, Params: 0
4. **Conv**: K=3, S=1, P=1, C=64→128 → RF: 12, Params: 73,856

**Total Parameters**: 112,576

## Parameter Calculation Formulas

### Convolutional Layer
- **Weights**: `kernel_size² × in_channels × out_channels`
- **Biases**: `out_channels`
- **Total**: `weights + biases`

### Pooling Layer
- **Weights**: 0 (no learnable parameters)
- **Biases**: 0 (no learnable parameters)
- **Total**: 0

## Technical Details

The application uses standard formulas for both receptive fields and parameters:

**Receptive Field:**
- **Output RF**: `n_out = (n_in - 1) * stride + kernel_size`
- **Output Jump**: `j_out = j_in * stride`
- **Output Center**: `r_out = r_in + (kernel_size - 1)/2 - padding * j_in`

**Parameters:**
- **Conv Weights**: `K² × C_in × C_out`
- **Conv Biases**: `C_out`
- **Pool Parameters**: 0

Where:
- `K`: Kernel size
- `C_in/C_out`: Input/output channels
- `n_in/n_out`: Input/output receptive field size
- `j_in/j_out`: Input/output jump
- `r_in/r_out`: Input/output center position

## Files Structure

- `app.py` - Main Flask application with receptive field and parameter calculation logic
- `templates/index.html` - Enhanced web interface with parameter display
- `pyproject.toml` - Project dependencies and configuration
- `README.md` - This comprehensive documentation

## Learning Resources

- [Understanding Receptive Fields in CNNs](https://distill.pub/2019/computing-receptive-fields/)
- [Receptive Field Calculator](https://fomoro.com/research/article/receptive-field-calculator)
- [CNN Receptive Field Mathematics](https://medium.com/mlreview/a-guide-to-receptive-field-arithmetic-for-convolutions-aa0b32364e71)
- [Parameter Counting in CNNs](https://towardsdatascience.com/understanding-and-calculating-the-number-of-parameters-in-convolution-neural-networks-cnns-fc88790d02d3)
