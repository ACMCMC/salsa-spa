# SALSA: Spanish Automatic Language Skill Analyzer

SALSA is a Python library for Spanish text analysis and automatic CEFR grading, powered by the official Plan Curricular del Instituto Cervantes (PCIC).

By leveraging the PCIC—the internationally recognized curriculum for Spanish as a foreign language—SALSA provides accurate, curriculum-aligned grading and vocabulary analysis. SALSA generates a comprehensive report that reflects the standards trusted by educators and institutions worldwide in the context of the CEFR (Common European Framework of Reference for Languages).

Authors:
- Jesus Vazquez-Capel (<jesus.vazquezcapel@estudiante.uam.es>)  
  ORCID: [0009-0003-2668-9491](https://orcid.org/0009-0003-2668-9491)
- Aldan Creo (<os@acmc.fyi>)  
  ORCID: [0000-0002-7401-5198](https://orcid.org/0000-0002-7401-5198)
- Damaris Mayans (<dmayans@colby.edu>)  
  ORCID: [0000-0002-6785-9392](https://orcid.org/0000-0002-6785-9392)

## Installation

You can install SALSA via pip:

```sh
pip install salsa-spa
```

## CLI Usage

You can use the CLI to automatically grade Spanish texts and output CEFR probabilities and stats as JSON:

```sh
salsa_spa grade-text --text "bailar con el presidente" --output result.json
```

```sh
salsa_spa grade-file --filepath input.txt --output result.json
```

If you omit `--output`, results will be printed to the console.
