class Transcriptor {
  toRna(dna) {
    let rna = '';
    for (const c of dna) {
      switch (c) {
        case 'A':
          rna += 'U';
          break;
        case 'C':
          rna += 'G';
          break;
        case 'G':
          rna += 'C';
          break;
        case 'T':
          rna += 'A';
          break;
        default:
          throw new Error('Invalid input DNA.');
      }
    }
    return rna;
  }
}

export default Transcriptor;
