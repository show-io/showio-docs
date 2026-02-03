# Directories
DIAGRAMS_SRC := diagrams
DIAGRAMS_OUT := docs/assets/diagrams

# Find all .dio source files
DIO_FILES := $(wildcard $(DIAGRAMS_SRC)/*.dio)

# Generate corresponding SVG output paths
SVG_FILES := $(patsubst $(DIAGRAMS_SRC)/%.dio,$(DIAGRAMS_OUT)/%.svg,$(DIO_FILES))

# Default target
.PHONY: all diagrams clean-diagrams

all: diagrams

# Build all diagrams
diagrams: $(SVG_FILES)

# Rule to convert .dio to .svg
$(DIAGRAMS_OUT)/%.svg: $(DIAGRAMS_SRC)/%.dio | $(DIAGRAMS_OUT)
	drawio -x -f svg -o $@ $<

# Create output directory if it doesn't exist
$(DIAGRAMS_OUT):
	mkdir -p $(DIAGRAMS_OUT)

# Clean generated diagrams
clean-diagrams:
	rm -f $(SVG_FILES)