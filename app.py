from flask import Flask, render_template, request, jsonify
import numpy as np
import json

app = Flask(__name__)

class ReceptiveFieldCalculator:
    """Calculate receptive field for neural network layers"""
    
    def __init__(self):
        self.layers = []
        self.receptive_fields = []
        
    def add_conv_layer(self, kernel_size, stride=1, padding=0):
        """Add a convolutional layer"""
        layer = {
            'type': 'conv',
            'kernel_size': kernel_size,
            'stride': stride,
            'padding': padding
        }
        self.layers.append(layer)
        self._calculate_receptive_fields()
        return layer
    
    def add_pool_layer(self, kernel_size, stride=None, padding=0):
        """Add a pooling layer (max or average)"""
        if stride is None:
            stride = kernel_size  # Default stride equals kernel size
            
        layer = {
            'type': 'pool',
            'kernel_size': kernel_size,
            'stride': stride,
            'padding': padding
        }
        self.layers.append(layer)
        self._calculate_receptive_fields()
        return layer
    
    def _calculate_receptive_fields(self):
        """Calculate receptive field for each layer"""
        self.receptive_fields = []
        
        # Starting receptive field
        n_in = 1  # Input receptive field size
        j_in = 1  # Input jump
        r_in = 0.5  # Input center
        
        for i, layer in enumerate(self.layers):
            k = layer['kernel_size']
            s = layer['stride']
            p = layer['padding']
            
            # Calculate output receptive field parameters
            n_out = (n_in - 1) * s + k
            j_out = j_in * s
            r_out = r_in + (k - 1) / 2 - p * j_in
            
            # Store receptive field info
            rf_info = {
                'layer_index': i,
                'layer_type': layer['type'],
                'layer_params': layer,
                'receptive_field_size': n_out,
                'jump': j_out,
                'center': r_out,
                'input_size': n_in,
                'output_size': n_out
            }
            self.receptive_fields.append(rf_info)
            
            # Update for next layer
            n_in = n_out
            j_in = j_out
            r_in = r_out
    
    def get_summary(self):
        """Get summary of all layers and their receptive fields"""
        return {
            'layers': self.layers,
            'receptive_fields': self.receptive_fields,
            'total_layers': len(self.layers)
        }
    
    def clear_layers(self):
        """Clear all layers"""
        self.layers = []
        self.receptive_fields = []

# Global calculator instance
calculator = ReceptiveFieldCalculator()

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/add_layer', methods=['POST'])
def add_layer():
    """API endpoint to add a layer"""
    try:
        data = request.get_json()
        layer_type = data.get('type')
        
        if layer_type == 'conv':
            layer = calculator.add_conv_layer(
                kernel_size=data.get('kernel_size', 3),
                stride=data.get('stride', 1),
                padding=data.get('padding', 0)
            )
        elif layer_type == 'pool':
            layer = calculator.add_pool_layer(
                kernel_size=data.get('kernel_size', 2),
                stride=data.get('stride', None),
                padding=data.get('padding', 0)
            )
        else:
            return jsonify({'error': 'Invalid layer type'}), 400
        
        return jsonify({
            'success': True,
            'layer': layer,
            'summary': calculator.get_summary()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/clear_layers', methods=['POST'])
def clear_layers():
    """API endpoint to clear all layers"""
    try:
        calculator.clear_layers()
        return jsonify({
            'success': True,
            'message': 'All layers cleared'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/get_summary')
def get_summary():
    """API endpoint to get current summary"""
    return jsonify(calculator.get_summary())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
