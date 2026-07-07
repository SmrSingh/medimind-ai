from enum import Enum


class ReportType(str, Enum):
    CBC = "Complete Blood Count"
    LFT = "Liver Function Test"
    KFT = "Kidney Function Test"
    LIPID = "Lipid Profile"
    THYROID = "Thyroid Profile"
    DIABETES = "Diabetes"
    VITAMIN = "Vitamin Profile"
    UNKNOWN = "Unknown"