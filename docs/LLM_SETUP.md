# Local LLM Setup

## Install Ollama

Install Ollama:
https://ollama.com

## Download Model

Example:

```
ollama pull mistral
```

## Start Service

```
ollama serve
```

## Test

```
curl http://localhost:11434/api/generate
```