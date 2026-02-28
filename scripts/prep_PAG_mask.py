"""
Script to build PAG ROI mask.
Author: Lea Pagani
Part of: Pain-ROI-Masks-NOVEL
"""

import os
import numpy as np
import nibabel as nib
from nilearn.image import resample_to_img

# --- PATHS (EDIT TO MATCH YOUR FOLDERS) ---
roi_dir = "/Path/To/Your/ROI/files"

aan_dir = (
    "/Path/to/your/AAN/Atlas/doi_10_5061_dryad_zw3r228d2__v20230718"
)

pag_src = os.path.join(aan_dir, "AAN_PAG_MNI152_1mm_v2p0.nii")
pag_out = os.path.join(roi_dir, "PAG_AAN_inHO.nii.gz")

# Reference: one HO ROI 
ref_img = nib.load(os.path.join(roi_dir, "Insula_HO_bilateral.nii.gz"))

# 1) Load PAG ROI from AAN
pag_img = nib.load(pag_src)
pag_data = pag_img.get_fdata()

# 2) Binarise 
pag_bin = (pag_data > 0).astype("uint8")
pag_bin_img = nib.Nifti1Image(pag_bin, pag_img.affine, pag_img.header)

# 3) Resample PAG into HO grid
pag_resampled = resample_to_img(pag_bin_img, ref_img, interpolation="nearest")
pag_res_data = (pag_resampled.get_fdata() > 0.5).astype("uint8")

pag_res_img = nib.Nifti1Image(pag_res_data, ref_img.affine, ref_img.header)
pag_res_img.to_filename(pag_out)

print("Saved cleaned, resampled PAG mask to:", pag_out)
print("Shape:", pag_res_img.shape)
print("Nonzero voxels:", int(pag_res_data.sum()))
