#!/bin/bash

# Jarvis Installation Script for macOS
# Run with: bash install_mac.sh

echo "========================================"
echo "Jarvis: Your AI Employee - macOS Setup"
echo "========================================"

# TODO: Check for Docker
echo ""
echo "Checking prerequisites..."

if ! command -v docker &> /dev/null; then
    echo "Docker not found. Please install Docker Desktop for Mac."
    exit 1
fi
echo "✓ Docker found"

# TODO: Check for Docker Compose
if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose not found. Please install Docker Compose."
    exit 1
fi
echo "✓ Docker Compose found"

# TODO: Check for Python
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Please install Python 3.10+"
    exit 1
fi
echo "✓ Python3 found"

# TODO: Create .env file
echo ""
echo "Setting up configuration..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "✓ Created .env file"
else
    echo "✓ .env file already exists"
fi

# TODO: Install dependencies
echo ""
echo "Installing Python dependencies..."
python3 -m pip install -r requirements.txt

# TODO: Start containers
echo ""
echo "Starting Docker containers..."
docker-compose up -d

echo ""
echo "========================================"
echo "Installation Complete!"
echo "========================================"
echo "Next steps:"
echo "1. Edit .env with your configuration"
echo "2. Run: docker-compose up"
echo "3. Visit: http://localhost:8000"
