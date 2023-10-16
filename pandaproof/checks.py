import pandas as pd

class DataQualityChecker:
    def __init__(self, data_frame):
        """
        Initialize the DataQualityChecker with a Pandas DataFrame.

        Parameters:
        - data_frame: The DataFrame to be checked.
        """
        self.data_frame = data_frame

    def check_data_schema(self, schema):
        """
        Check if the DataFrame matches the specified schema.

        Parameters:
        - schema: A dictionary specifying the expected schema with column names as keys and
                a dictionary with "type" (expected data type) and "required" (True or False) as values.

        Returns:
        - A list of issues found in the data, if any.
        """
        issues = []

        # Check if all expected columns are present
        missing_columns = set(schema.keys()) - set(self.data_frame.columns)
        if missing_columns:
            issues.append(f"Missing columns: {', '.join(missing_columns)}")

        # Check column data types and required fields
        for col, col_info in schema.items():
            expected_type = col_info.get("type")
            required = col_info.get("required", False)

            if col in self.data_frame.columns:
                actual_type = self.data_frame[col].dtype

                if expected_type is not None and actual_type != expected_type:
                    issues.append(f"Column '{col}' has an unexpected data type ({actual_type}), expected {expected_type}")

                if required:
                    if self.data_frame[col].isna().any():
                        issues.append(f"Column '{col}' has missing values, but it's required")
                    elif self.data_frame[col].count() == 0:
                        issues.append(f"Column '{col}' is required but has no data")

        return issues


    def check_unique_key(self, key_columns):
        """
        Check if the specified columns form a unique key in the DataFrame.

        Parameters:
        - key_columns: A list of column names that should form a unique key.

        Returns:
        - A list of issues found in the data, if any.
        """
        issues = []

        if not key_columns:
            return issues

        if not self.data_frame.duplicated(subset=key_columns, keep=False).empty:
            issues.append(f"The specified columns '{', '.join(key_columns)}' do not form a unique key.")

        return issues

    # Add more data quality checks as needed, e.g., outlier detection, date format checks, etc.
