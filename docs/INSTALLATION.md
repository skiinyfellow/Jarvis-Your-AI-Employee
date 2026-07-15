# Installation Guide

## Prerequisites

- Docker & Docker Compose
- Python 3.10+
- 4GB RAM minimum
- 10GB free disk space

## Quick Start

### Windows

```powershell
.\install\install_windows.ps1
```

### Linux

```bash
bash install/install_linux.sh
```

### macOS

```bash
bash install/install_mac.sh
```

## Manual Setup

### 1. Clone Repository

```bash
git clone https://github.com/skiinyfellow/Jarvis-Your-AI-Employee.git
cd Jarvis-Your-AI-Employee
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env with your settings
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Services

```bash
docker-compose up -d
```

### 5. Verify Installation

```bash
# Check services
docker-compose ps

# Check logs
docker-compose logs -f openjarvis
```

## Configuration

See `.env.example` for all available options.

## TODO

- [ ] Add health checks
- [ ] Create migration system
- [ ] Setup monitoring
- [ ] Add backup system
