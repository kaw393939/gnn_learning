"""
GNN Educational System Integration Guide

This guide shows how to prepare and run the Educational Achievement and Recommendation System
with the Streamlit interface.
"""

import os
import sys

# Step 1: Rename the original script to gnn_education_system.py
# This is needed as the Streamlit app imports from this module

def prepare_system():
    """Prepare the GNN Educational System for use with Streamlit"""
    
    # Check if original script exists
    if not os.path.exists("paste.txt"):
        print("Error: Original script (paste.txt) not found!")
        return False
    
    # Rename to proper module name
    if not os.path.exists("gnn_education_system.py"):
        print("Converting original script to module...")
        
        with open("paste.txt", "r", encoding="utf-8") as source_file:
            content = source_file.read()
        
        # Save as Python module
        with open("gnn_education_system.py", "w", encoding="utf-8") as module_file:
            module_file.write(content)
        
        print("✅ Created gnn_education_system.py module")
    else:
        print("✅ gnn_education_system.py module already exists")
    
    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    print("✅ Ensured data directory exists")
    
    # Create empty config.yaml if it doesn't exist
    if not os.path.exists("config.yaml"):
        with open("config.yaml", "w", encoding="utf-8") as config_file:
            config_file.write("""
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
""")
        print("✅ Created default config.yaml")
    else:
        print("✅ config.yaml already exists")
    
    # Check if Streamlit is installed
    try:
        import streamlit
        print("✅ Streamlit is installed")
    except ImportError:
        print("⚠️ Streamlit is not installed. Install with: pip install streamlit")
        return False
    
    # Check required packages
    try:
        import torch
        import torch_geometric
        import numpy as np
        import pandas as pd
        import plotly
        import yaml
        print("✅ Required packages are installed")
    except ImportError as e:
        print(f"⚠️ Missing required package: {e}")
        print("Install with: pip install torch torch_geometric numpy pandas plotly pyyaml")
        return False
    
    return True

def run_app():
    """Run the Streamlit application"""
    if not os.path.exists("app.py"):
        print("Error: app.py not found!")
        return False
    
    print("\n" + "="*50)
    print("Starting Streamlit Application")
    print("="*50)
    print("\nTo access the application:")
    print("1. Wait for Streamlit to start")
    print("2. Open your browser to the URL shown in the terminal (usually http://localhost:8501)")
    print("3. Use the interface to interact with the Educational System")
    print("\nPress Ctrl+C to stop the application")
    print("="*50 + "\n")
    
    # Run Streamlit app
    os.system("streamlit run app.py")
    
    return True

if __name__ == "__main__":
    print("\nPreparing GNN Educational System for Streamlit...\n")
    
    if prepare_system():
        print("\n✅ System preparation complete. Ready to run Streamlit app.")
        
        run_app()
    else:
        print("\n❌ System preparation failed. Please check the errors above.")
        sys.exit(1)