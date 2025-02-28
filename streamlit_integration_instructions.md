# GNN Educational System

A Graph Neural Network (GNN) based system for educational achievement tracking and personalized learning recommendations with a Streamlit interface.

## Overview

This system uses Graph Neural Networks to model relationships between:
- Educational concepts
- Assessment questions
- Learning resources
- Learner profiles and performance

The GNN analyzes these connections to provide personalized recommendations, identify knowledge gaps, and track educational achievement.

## Setup and Installation

### Prerequisites

- Python 3.7+
- PyTorch
- PyTorch Geometric
- Streamlit
- NumPy
- Pandas
- Plotly
- PyYAML

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/gnn-educational-system.git
cd gnn-educational-system
```

2. Install required packages:
```bash
pip install torch torch_geometric streamlit numpy pandas plotly pyyaml
```

## Usage

### Quick Start

1. Prepare your GNN model code in a Python file (e.g., `gnn_model.py`)

2. Run the integration script:
```bash
python integration_guide.py gnn_model.py
```

The script will:
- Copy your GNN model to the module name required by the app
- Create necessary directories and config files
- Check for required dependencies
- Launch the Streamlit app

3. Access the app in your browser (typically at http://localhost:8501)

### Manual Setup

If you prefer to set up the system manually:

1. Ensure your GNN model is saved as `gnn_education_system.py`
2. Create a `data` directory
3. Create a `config.yaml` file with appropriate settings
4. Launch the app directly:
```bash
streamlit run app.py
```

## Configuration

The system is configured through `config.yaml`:

```yaml
knowledge_graph:
  concepts_file: "data/concepts.json"
  questions_file: "data/questions.json"
  resources_file: "data/resources.json"
  learners_file: "data/learners.json"
  cache_dir: "data/cache"
  max_cache_size_mb: 100

gnn:
  model_type: "hetero_gat"
  hidden_channels: 64
  num_layers: 2
  num_heads: 4
  dropout: 0.2
  learning_rate: 0.001
  weight_decay: 5e-4
  batch_size: 32
  patience: 10
  validation_ratio: 0.2
```

## Data Structure

### Required JSON Files

- `concepts.json`: Educational concepts and their relationships
- `questions.json`: Assessment questions linked to concepts
- `resources.json`: Learning materials and their associated concepts
- `learners.json`: Learner profiles and their interaction history

Example concept format:
```json
{
  "concepts": [
    {
      "id": "c001",
      "name": "Addition",
      "description": "Basic mathematical operation of adding numbers",
      "difficulty": 1,
      "prerequisites": []
    },
    {
      "id": "c002",
      "name": "Subtraction",
      "description": "Basic mathematical operation of subtracting numbers",
      "difficulty": 1,
      "prerequisites": ["c001"]
    }
  ]
}
```

## Features

- **Concept Mapping**: Visualize relationships between educational concepts
- **Knowledge Assessment**: Evaluate learner understanding of specific concepts
- **Personalized Recommendations**: Suggest resources based on learner needs
- **Learning Path Generation**: Create optimized paths through educational content
- **Performance Analytics**: Track and visualize learner progress

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.