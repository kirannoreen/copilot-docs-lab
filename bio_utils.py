# bio_utils.py
"""A collection of utility functions for biological sequence analysis.
"""
def gc_content(seq: str) -> float:
    """
    Return GC percentage for a DNA sequence (0-100).
    """
    seq = seq.upper()
    if not seq:
        return 0.0
    gc = sum(1 for b in seq if b in "GC")
    return round(100 * gc / len(seq), 2)
