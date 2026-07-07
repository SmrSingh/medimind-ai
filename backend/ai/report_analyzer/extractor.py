import re

from ai.report_analyzer.parser import MedicalReportParser


class MedicalParameterExtractor:

    def __init__(self):

        self.reference_pattern = re.compile(
            r"^\d+(\.\d+)?\s*[-–]\s*\d+(\.\d+)?$"
        )

    def extract(self, text: str):
        lines = [line.strip() for line in text.splitlines() if line.strip()]

        parameters = []

        i = 0
        while i < len(lines) - 3:
            parameter = lines[i]

            # Skip section headers
            if parameter.upper() in {
                "HAEMATOLOGY",
                "RBC INDICES",
                "PLATELETS INDICES",
                "DIFFERENTIAL LEUCOCYTE COUNT",
                "ABSOLUTE LEUCOCYTE COUNT",
                "INTERPRETATION",
                "TEST DESCRIPTION",
                "RESULT",
                "REF. RANGE",
                "UNIT",
            }:
                i += 1
                continue

            value = lines[i + 1]
            third = lines[i + 2]
            fourth = lines[i + 3]

            # Pattern 1:
            # Parameter
            # Value
            # Reference
            # Unit
            if (
                self._is_number(value)
                and self._is_reference_range(third)
                and self._is_unit(fourth)
            ):
                parameters.append(
                    {
                        "parameter": parameter,
                        "value": float(value),
                        "reference_range": third,
                        "unit": fourth,
                    }
                )
                i += 4
                continue

            # Pattern 3:
            # Parameter
            # Value
            # Unit
            # (Missing Reference Range)
            if (
                self._is_number(value)
                and self._is_unit(third)
                and not self._is_reference_range(fourth)
            ):
                parameters.append(
                    {
                        "parameter": parameter,
                        "value": float(value),
                        "unit": third,
                        "reference_range": None,
                    }
                )
                i += 3
                continue

            # Pattern 2:
            # Parameter
            # Value
            # Unit
            # Reference
            if (
                self._is_number(value)
                and self._is_unit(third)
                and self._is_reference_range(fourth)
            ):
                parameters.append(
                    {
                        "parameter": parameter,
                        "value": float(value),
                        "reference_range": fourth,
                        "unit": third,
                    }
                )
                i += 4
                continue

            i += 1

        return parameters

    def _is_number(self, value):

        try:
            float(value)
            return True
        except ValueError:
            return False
    def _is_reference_range(self, value):
        return bool(self.reference_pattern.match(value))


    def _is_unit(self, value):
        units = {
        "g/dL", "mg/dL", "U/L", "IU/L", "mmol/L",
        "%", "/cumm", "fL", "pg", "mEq/L",
        "ng/mL", "µIU/mL", "mIU/L"
        }

        return (
        value in units
        or "/" in value
        or value.endswith("L")
        or value.endswith("%")
        )
    from ai.report_analyzer.parser import MedicalReportParser


if __name__ == "__main__":

    parser = MedicalReportParser(
        "datasets/reports/lft/Sample_LFT_Report.pdf"
    )

    text = parser.extract_text()

    extractor = MedicalParameterExtractor()

    parameters = extractor.extract(text)

    for parameter in parameters:
        print(parameter)