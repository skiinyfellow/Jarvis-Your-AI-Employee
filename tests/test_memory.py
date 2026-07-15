from core.memory.memory_store import MemoryStore
import pytest
import os
import tempfile


def test_memory_save_and_retrieve():
    """Test saving and retrieving memories."""
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
        db_path = f.name
    
    try:
        memory = MemoryStore(db_path)
        
        # Test save
        assert memory.save("Test memory 1") is True
        assert memory.save("Test memory 2") is True
        
        # Test retrieve
        memories = memory.get_all()
        assert len(memories) == 2
        assert "Test memory 1" in memories
        assert "Test memory 2" in memories
        
        memory.close()
    finally:
        if os.path.exists(db_path):
            os.unlink(db_path)


def test_memory_invalid_input():
    """Test memory with invalid input."""
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
        db_path = f.name
    
    try:
        memory = MemoryStore(db_path)
        
        # Test invalid inputs
        assert memory.save("") is False
        assert memory.save(None) is False
        assert memory.save(123) is False
        
        memory.close()
    finally:
        if os.path.exists(db_path):
            os.unlink(db_path)


def test_memory_in_memory_database():
    """Test in-memory database (for testing)."""
    memory = MemoryStore(":memory:")
    
    memory.save("Jarvis initialized")
    assert "Jarvis initialized" in memory.get_all()
    
    memory.close()


def test_memory_clear():
    """Test clearing memory."""
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
        db_path = f.name
    
    try:
        memory = MemoryStore(db_path)
        
        memory.save("Memory 1")
        memory.save("Memory 2")
        assert len(memory.get_all()) == 2
        
        assert memory.clear() is True
        assert len(memory.get_all()) == 0
        
        memory.close()
    finally:
        if os.path.exists(db_path):
            os.unlink(db_path)
