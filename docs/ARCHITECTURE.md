# Jarvis Architecture

## System Overview

Jarvis is composed of several interconnected systems:

```
┌─────────────────────────────────────────────────────────┐
│                    Jarvis Core Engine                    │
│                   (OpenJarvis)                           │
└─────────────────────────────────────────────────────────┘
         ↓              ↓              ↓              ↓
    ┌────────┐      ┌────────┐    ┌────────┐    ┌────────┐
    │ Hermes │      │Haystack│    │ Memory │    │ Modules│
    │(Tasks) │      │ (RAG)  │    │(Context)    │ (Biz)  │
    └────────┘      └────────┘    └────────┘    └────────┘
         ↓              ↓              ↓              ↓
    ┌─────────────────────────────────────────────────────┐
    │            Storage & Integration Layer              │
    │  PostgreSQL  Redis  Qdrant  Telegram  Obsidian     │
    └─────────────────────────────────────────────────────┘
```

## Core Components

### OpenJarvis
Main AI orchestration engine coordinating all systems.

### Hermes
Workflow and task management system.

### Haystack
Retrieval-Augmented Generation for document intelligence.

### Memory
Persistent context and historical tracking.

### Modules
Custom business logic modules (e.g., Coffee Shop).

## Data Flow

1. User input via Telegram or Dashboard
2. Processed by OpenJarvis
3. Routed to appropriate module (Hermes, Haystack, etc.)
4. Results stored in Memory and Database
5. Response sent back to user

## TODO

- [ ] Add sequence diagrams
- [ ] Document API endpoints
- [ ] Create deployment guide
- [ ] Add performance metrics
