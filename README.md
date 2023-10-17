![Logo]([http://shorturl.at/foER2])

# PandaProof

The **PandaProof** is a Python package designed to help you perform data quality checks on Pandas DataFrames. You can use it to validate whether your data adheres to a specified schema, check for missing values, ensure correct data types, and more.

## Installation

To use PandaProof locally, follow these steps:

1. Clone or download the repository to your local machine.

2. Open a terminal or command prompt and navigate to the project's root directory (where you've cloned or downloaded PandaProof).

3. Install the package in editable mode using `pip`:

```bash
git clone https://github.com/Ahmed-Jabrane/PandaProof.git
cd PandaProof
pip install -e .
```

## Usage

Here's an example of how to use the pandaproof class:

```python
import pandas as pd
from pandaproof import DataQualityChecker

data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'City': ['New York', 'San Francisco', 'Los Angeles']
})

# Define a schema for the test DataFrame
test_schema = {
    'Name': {'type': str, 'required': True},
    'Age': {'type': int, 'required': True},
    'City': {'type': str, 'required': False}
}

# Initialize DataQualityChecker with the sample DataFrame
checker = DataQualityChecker(data)

# Check if the sample data matches the specified schema
issues = checker.check_data_schema(test_schema)

if issues:
    for issue in issues:
        print(issue)
else:
    print("Data matches the expected schema.")
```

## Features

| Status          | Feature                        | Description                                         | Use Case                                                         |
| ----------------| -------------------------------| ---------------------------------------------------|------------------------------------------------------------------|
| ✅               | Schema Validation              | Check if DataFrame matches an expected schema.     | Ensuring data conforms to a predefined structure.               |
| ✅               | Data Type Validation           | Ensure columns have expected data types.           | Verifying data consistency and correctness.                     |
| ✅               | Required Fields                | Detect missing values in required columns.        | Ensuring essential data is not missing.                         |
| ✅               | Unique Key Validation          | Check if specified columns form a unique key.      | Maintaining data integrity with unique identifiers.             |
| ⌛               | Custom Validation Functions    | Custom checks on data within columns.             | Implementing domain-specific data validation.                   |
| ⌛               | Value Range Validation         | Validate values within specified ranges.          | Enforcing data constraints and limits.                         |
| ⌛               | Data Format Checks             | Validate data format using regular expressions.   | Ensuring data adheres to specific formats (e.g., dates, emails).|

## Contributing

Contributions, bug reports, and feature requests are welcome! Please open an issue on the GitHub repository if you encounter any problems or have ideas for improvements.

## License

This package is licensed under the MIT License. See the LICENSE file for details.

Happy data quality checking!


