# Directories
DIAGRAMS_SRC := diagrams
DIAGRAMS_OUT := docs/assets/diagrams

# Find all .dio source files recursively
DIO_FILES := $(shell find $(DIAGRAMS_SRC) -name '*.dio' 2>/dev/null)

# Generate corresponding SVG output paths (preserving directory structure)
SVG_FILES := $(patsubst $(DIAGRAMS_SRC)/%.dio,$(DIAGRAMS_OUT)/%.svg,$(DIO_FILES))

# Default target
.PHONY: all diagrams clean-diagrams api tree

all: diagrams

# Generate API documentation from OSC files
api:
	python3 scripts/process_osc_files.py

# Auto-generate navigation tree
tree:
	python3 scripts/auto_generate_tree.py

# Build all diagrams
diagrams: $(SVG_FILES)

# Rule to convert .dio to .svg
$(DIAGRAMS_OUT)/%.svg: $(DIAGRAMS_SRC)/%.dio
	@mkdir -p $(dir $@)
	drawio -x -f svg -o $@ $<

# Clean generated diagrams
clean-diagrams:
	rm -f $(SVG_FILES)
