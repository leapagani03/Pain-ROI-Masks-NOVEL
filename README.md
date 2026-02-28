# Pain-ROI-Masks-NOVEL
This repository documents the creation of pain-related ROI masks used for small volume correction in second-level SPM25 (25.01.02) analyses. 
These masks were created for an fMRI study investigating the modulatory effects of novelty on fear extinction (PI: Judith Schomaker). These masks were created for exploratory purposes and were used to examine whether shock intensity manipulation (control, low-intensity shock, high-intensity shock) elicited different activation within pain-related and affective/threat-related neural networks.  

# Atlases 
Regions were defined using the Harvard–Oxford cortical and subcortical probabilistic atlases (maxprob-thr-25-1mm).
These atlas files were obtained via Neurovault (Gorgolewski et al., 2015).
The Periacqueductal Gray (PAG) was defined using the Ascending Arousal Network (AAN) Atlas, https://doi.org/10.5061/dryad.zw3r228d2). 

# Pain Masks
Three masks were generated: 
- PainCore
- PainAffective
- PainGlobal (combined)

The PainCore mask includes: 
- Somatosensory Cortex
- Bilateral Insula
- ACC
- Thalamus
- PAG
and represents the core nociceptive/salience-related network

The PainAffecive mask includes: 
- Insula
- ACC
- PCC
- PFC
- vmPFC
- dlPFC
- Striatum
- Hippocampus
- amygdala
- PAG
and represents an extended affective-cognitive threat-related network

The PainGlobal mask was built from the union of both masks

# PAG processing 
The Harvard–Oxford atlas does not contain a dedicated PAG mask. Therefore, PAG was obtained from the AAN atlas. This repository contains a .py script that processes the PAG mask as follows: 
1. Loads the PAG mask from the AAN atlas (MNI152, 1mm space)
2. Binarizes the mask (> 0 → 1)
3. Resamples the mask to match the Harvard–Oxford grid (182 × 218 × 182)
4. Uses nearest-neighbour interpolation
5. Re-binarizes the mask after interpolation
6. Saves the resampled mask using the Harvard–Oxford affine matrix and header

# Resampling to Functional Contrast Space 
Final network masks were resampled to match first-level SPM contrast images.
Functional contrast properties:
Image dimensions: 57 × 70 × 56
Voxel size: 2.75 × 2.75 × 3.03 mm
Nearest-neighbour interpolation was used to preserve the binary mask structure.

# Mask Output 
Two versions of the masks are provided 
1. HO-Space Masks
Masks defined in HO grid space (MNI152, 1mm resolution, 182 x 218 x 182)
These masks represent the anatomically defined network regions prior to functional resampling

2. Contrast-SPace MAsks
Masks resampled to match first-level SPM contrast images
- 57 × 70 × 56 voxels
- 2.75 × 2.75 × 3.03 mm voxel size
These were used in second-level SPM analyses (SVC, pFWE<.05). Nearest-neighbour interpolation was used to preserve binary structure.

# Intended Use
These masks were used to
- Explore shock intensity effects:
- Assess engagement of pain-related and threat (affective)-related neural systems
- Exploratorily accompany whole-brain analyses

# Note
- The HO and AAN atlas files are not present in this repository
- Users should thus obtain:
  * Harvard–Oxford cortical and subcortical maxprob-thr25-1mm atlases (via Neurovault; Gorgolewski et al., 2015)
  * AAN atlas (Dryad DOI above) 

# References 
Ascending Arousal Network Atlas dataset: https://doi.org/10.5061/dryad.zw3r228d2
Gorgolewski, K. J., et al. (2015). NeuroVault.org: a web-based repository for collecting and sharing unthresholded statistical maps of the human brain. Frontiers in Neuroinformatics, 9, 8. https://doi.org/10.3389/fninf.2015.00008
