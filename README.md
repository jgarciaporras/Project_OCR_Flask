# Project_OCR_Flask

OCR Medical Reports

- YOLO model using YOLOv5

### 1.	Problem identification:


Doctors must go through hundreds of reports every day and this could cause inaccuracies and bottlenecks which in turn might be translated into a reduction in productivity, consequently, this could prove to be detrimental to a patient's health. Therefore, a more streamlined approach is required to process the medical reports and make insightful inferences out of them


### 2.	Precedent solutions
EMRs or Electronic Medical Reports are a digital version of the medical reports used in a clinician's office. They help in tracking a patient’s medical data over time, identify which patients are due for a checkup, and monitor and help improve the quality of care.

However, each report in this system must be manually added by a user. Along with this, each report must be printed out and delivered by mail to the required specialists. This can be incredibly time-consuming and very prone to errors. A better solution is required to make this process more efficient.

### 3. Solution
#### 3.1 OCR for Medical Reports Workflow
1.	Detect the regions and do the annotations
3.	Perform augmentations (Grayscale, Saturation, Noise)
4.	Pass the dataset through YOLO v5 and take the regions within the bounding boxes
5.	Preprocessing techniques were applied on images before using Tesseract
6.	Images were passed over Tesseract and the output is saved as a CSV file





Deployment in localhost:


https://user-images.githubusercontent.com/90323558/164146267-f9e44e1b-0b94-449f-bf21-62956ce52940.mp4

