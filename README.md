
# PandaProof

The **PandaProof** is a Python package designed to help you perform data quality checks on Pandas DataFrames. You can use it to validate whether your data adheres to a specified schema, check for missing values, ensure correct data types, and more.

## Installation

You can install the package using pip:

```bash
pip install pandaproof
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

| Feature                        | Status             |
| -------------------------------| -------------------|
| Schema Validation              | Implemented        |
| Data Type Validation           | Implemented        |
| Required Fields                | Implemented        |
| Unique Key Validation          | Implemented        |
| Custom Validation Functions    | Not Implemented    |
| Value Range Validation         | Not Implemented    |
| Data Format Checks             | Not Implemented    |

## Contributing

Contributions, bug reports, and feature requests are welcome! Please open an issue on the GitHub repository if you encounter any problems or have ideas for improvements.

## License

This package is licensed under the MIT License. See the LICENSE file for details.

Happy data quality checking!


