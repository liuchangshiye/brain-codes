## Readme 

**Data Processing**

1. Extract images

Please refer to the `extract_image.py`. There are many nii files for each patient. So we need to find the correct one. The logic is that in general, the nill file with the largest file size is the correct one, except the files in ` pid_to_file`. The `pid_to_file` is the pairship corrected by Zhulei.  So we first find the largest nii file and check whether it exists in the `pid_to_file` to find the correct nii files.

For CSF images, the window level (window_center in the window_image function) and window width are 20 and 10. For WM & GM, the window level and window width are 40 and 80. When we use function `window_image` to process the images, also need to rescale the image values to [0,255].

When you process different kinds of data (prospective or another type), you need to comment two of the 993,994,995 lines and one of 997,998 lines based on the name of the folders.

When extracting ground truth, need to note that for CSF, we only extract CSF pixels and for GM & WM, we only extract GM & WM pixels. The logic that first saves the ground truth as jpg files and then converts it to png files is from the codes of Zhulei. I just follow his logic.

If you want to use synthstrip to process the data, only extract the ground truth in this step.

2. Extract effective pixels with Synthstrip tool

Run `synthstrip_dict.py` to obtain the nii dict and run `correct_image_CSF_Brain.py` to correct the nii files (which is also mentioned in the first step).

Then run the `synthstrip/mri_synthstrip_nii.py`  to get the processed images.



Warning: For the patient 019 369 550 960 PRECISE_008, the data format is not brain images, For PRECISE_082, there is CSF, WM & GM ground truth, so I removed these patients. Also need to remove patient PRECISE_126 because there is no data.

Warning: There are some problems when processing the patients '2191_273', '2191_738', 'PRECISE_019_C', '2191_496', '2191_1290', '2191_800', '2191_1100', '2191_1288', '2191_1024', '2191_006', '2191_1080', '2191_1504', '2191_972', '2191_890', '2191_1384', '2191_018', '2191_070', '2191_976', '2191_992', '2191_1444'. I also removed these patients.

