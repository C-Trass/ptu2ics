# ptu2ics



ptu2ics is a Python toolkit for converting PicoQuant PTU
files into Image Cytometry Standard (ICS) format for downstream time-correlated
single-photon counting (TCSPC) and fluorescence lifetime analysis.

The package is designed for workflows where lifetime-resolved data are
generated or processed outside PicoQuant hardware or software, but need
to be re-encoded into PTU format for compatibility with existing FLIM
and TCSPC analysis pipelines.ptu2ics focuses on transparent, 
eproducible data conversion rather than black-box file translation.

---

## Features

- Reading of PicoQuant PTU-compatible data structures

- Conversion to Image Cytometry Standard (ICS) files data structures

- Preservation of photon timing, metadata, and acquisition parameters

- Support for lifetime-resolved and time-tagged imaging data

- Designed to integrate with FLIM and TCSPC analysis workflows

---

## Installation

Clone the repository and install dependencies:

```bash

git clone https://github.com/C-Trass/ics2ptu.git

cd ics2ptu

pip install -r requirements.txt

```

---


## Who is this for?

ptu2ics is intended for:


- FLIM users comparing lifetime data across experiments or conditions
- Researchers interested in lifetime-based classification or matching
- Users working with heterogeneous or low-photon FLIM datasets
- Scientists who want quantitative alternatives to intensity-based comparisons

---

## Citation

If you use FLIMatch in academic work, please cite:

Dr Conor A. Treacy, FLIMatch: Lifetime-based matching and comparison of

fluorescence lifetime imaging data, Biomedical Optics Express, forthcoming.


A DOI will be added here once the associated methods paper is published. Until then, you may cite this 
repository directly using the GitHub URL and the software version.

---


## License

This project is released under the MIT License.

You are free to use, modify, and distribute the code with attribution.


---


## Contact

Maintained by Conor Treacy

📫 Contact: \[LinkedIn](https://www.linkedin.com/in/conor-treacy-phd-2aa7406a/) | \[Email](mailto:conor.Treacy@brunel.ac.uk)

_From photons to plots._

