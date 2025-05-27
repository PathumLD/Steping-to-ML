try:
    import non_existent_module
except ImportError as ie:
    raise RuntimeError("Failed to load required module") from ie