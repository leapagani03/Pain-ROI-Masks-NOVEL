"""
Script to resample pain-related ROI masks.
Author: Lea Pagani
Part of: Pain-ROI-Masks-NOVEL
"""
import os
import nibabel as nib
import numpy as np
from nilearn.image import resample_to_img

roi_dir = "/Path/to/your/ROI/files"
ref_con = "/Path/to your/1stLevel/contrast/image/con_0001.nii"

masks = [
    "PainCore_HO_plusPAG.nii",
    "PainAffective_HO.nii",
]

ref_img = nib.load(ref_con)

for m in masks:
    src = os.path.join(roi_dir, m)
    print(f"\nResampling {m} ...")

    img = nib.load(src)
    data = img.get_fdata()

    # ensure binary
    bin_data = (data > 0).astype("uint8")
    bin_img = nib.Nifti1Image(bin_data, img.affine, img.header)

    # resample to contrast space
    resampled = resample_to_img(
        bin_img, ref_img,
        interpolation="nearest"
    )

    # re-binarize after resampling
    res_bin = (resampled.get_fdata() > 0.5).astype("uint8")
    out = nib.Nifti1Image(res_bin, ref_img.affine, ref_img.header)

    out_path = os.path.join(roi_dir, m.replace(".nii", "_InContrastSpace.nii"))
    out.to_filename(out_path)

    print("   -> Saved:", out_path)
    print("   -> Shape:", out.shape)
    print("   -> Voxels in mask:", int(res_bin.sum()))
