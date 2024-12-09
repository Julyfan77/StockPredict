# Variables
VENV = notebook_env
REQUIREMENTS = requirements.txt
NOTEBOOK = train_noacculmulate.ipynb
OUTPUT_DIR = output
EXECUTED_NOTEBOOK = $(OUTPUT_DIR)/executed_notebook.ipynb

# Default target
all: install run

# Install dependencies
install:
	@echo "Setting up the virtual environment and installing dependencies..."
	python3 -m venv $(VENV)  # Create virtual environment
	./$(VENV)/bin/pip install --upgrade pip  # Upgrade pip
	./$(VENV)/bin/pip install -r $(REQUIREMENTS)  # Install dependencies

# Run the notebook
run: $(EXECUTED_NOTEBOOK)

$(EXECUTED_NOTEBOOK): $(NOTEBOOK)
	@echo "Executing the notebook..."
	mkdir -p $(OUTPUT_DIR)
	./$(VENV)/bin/jupyter nbconvert --to notebook --execute $(NOTEBOOK) --output $(EXECUTED_NOTEBOOK)

# Clean up generated files and environment
clean:
	@echo "Cleaning up..."
	rm -rf $(VENV) $(OUTPUT_DIR)

# Phony targets
.PHONY: all install run clean
