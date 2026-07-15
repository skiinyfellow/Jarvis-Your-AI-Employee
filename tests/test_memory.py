from core.memory.memory_store import MemoryStore


def test_memory():
    memory = MemoryStore(
        ":memory:"
    )
    memory.save(
        "Jarvis initialized"
    )
    assert (
        "Jarvis initialized"
        in memory.get_all()
    )