#!/bin/bash
echo "Generating documentation for GravityFlip..."
python -m pydoc -w src.gravity_flip
echo "Documentation generated: gravity_flip.html"

