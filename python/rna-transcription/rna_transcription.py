"""RNA transcription"""

def to_rna(dna_strand):
    """Convert a DNA strand into an RNA strand"""

    # Create an empty array to hold the converted RNA string
    rna_string = []

    # Use a dictionary to map DNA bases to RNA bases
    bases = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }

    # Iterate through each base in the DNA strand
    for base in dna_strand:
        # Check that the current base is a real DNA base
        if base in bases:
            # Get the associated RNA base and append to the RNA string
            rna_string.append(bases[base])
        else:
            raise ValueError('Invalid DNA base: ' + base)

    return ''.join(rna_string)
