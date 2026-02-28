"""
Script to build pain-related ROI masks.
Author: Lea Pagani
Part of: Pain-ROI-Masks-NOVEL
"""

import os
import numpy as np
import nibabel as nib

roi_dir = "/Path/to/your/ROI/files"

# ---- define which single-ROIs go in each composite mask ----
mask_defs = {
    # 1) Core nociceptive pain matrix
    "PainCore_HO_plusPAG.nii.gz": [
        "Somatosensory_HO.nii.gz",
        "Insula_HO_bilateral.nii.gz",
        "ACC_HO.nii.gz",
        "Thalamus_HO_bilateral.nii.gz",
        "PAG_AAN_inHO.nii.gz",
    ],

    # 2) Affective / cognitive / emotional pain network
    "PainAffective_HO.nii.gz": [
        "Insula_HO_bilateral.nii.gz",
        "ACC_HO.nii.gz",
        "PCC_HO.nii.gz",
        "PFC_HO.nii.gz",
        "vmPFC_HO.nii.gz",
        "dlPFC_HO.nii.gz",
        "Striatum_HO_bilateral.nii.gz",
        "Hippocampus_HO_bilateral.nii.gz",
        "Amygdala_HO_bilateral.nii",   
        "PAG_AAN_inHO.nii.gz",
    ],

    # 3) Global pain-related mask = union of all ROIs
    "PainGlobal_AllROIs.nii.gz": [
        "Somatosensory_HO.nii.gz",
        "Insula_HO_bilateral.nii.gz",
        "ACC_HO.nii.gz",
        "PCC_HO.nii.gz",
        "Thalamus_HO_bilateral.nii.gz",
        "PFC_HO.nii.gz",
        "vmPFC_HO.nii.gz",
        "dlPFC_HO.nii.gz",
        "Striatum_HO_bilateral.nii.gz",
        "Hippocampus_HO_bilateral.nii.gz",
        "Amygdala_HO_bilateral.nii",
        "PAG_AAN_inHO.nii.gz",
    ],
}

# ---- helper to build each mask ----
def build_mask(mask_name, roi_files):
    roi_paths = [os.path.join(roi_dir, f) for f in roi_files]

    # use first ROI as reference
    ref_img = nib.load(roi_paths[0])
    combined = np.zeros(ref_img.shape, dtype="uint8")

    for p in roi_paths:
        img = nib.load(p)
        data = img.get_fdata()
        mask = (data > 0).astype("uint8")
        combined = np.clip(combined + mask, 0, 1)

    out_path = os.path.join(roi_dir, mask_name)
    out_img = nib.Nifti1Image(combined, ref_img.affine, ref_img.header)
    nib.save(out_img, out_path)

    print(f"Saved {mask_name}  |  nonzero voxels: {int(combined.sum())}")


if __name__ == "__main__":
    for mname, rois in mask_defs.items():
        print("\nBuilding", mname)
        build_mask(mname, rois)
