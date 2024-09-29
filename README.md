# Robot Arm System Test Automation

## Description
This project is a test automation solution for verifying the behavior of a robot arm within a rectangular working area. The robot moves around the area, visiting points from an input file, and the system compares these points with actual visited points from an output file. The system logs results with statuses like `PASS` or `FAIL`, including error messages for failed tests.

## Features
- Reads rectangle and points values from an input file.
- Verifies whether both expected and actual points are within the rectangular working area.
- Checks if the robot's actual visited points match the expected points.
- Compares expected and actual points sequentially.
- Logs results in a `test_results.txt` file, specifying whether each test `PASS`ed or `FAIL`ed.
- Handles invalid point entries and custom error messages.

## Files Structure
├── main.py               # Main script to run the test automation
├── test_system.py        # Contains the TestSystem class logic
├── rectangle.py          # Contains the Rectangle class logic
├── utils.py              # Utility functions for file validation
├── system_input_file.txt # Input file containing rectangle and points data
├── system_output_file.txt# Output file containing actual visited points
├── test_results.txt      # Log file with test results in the current project folder
└── config.txt            # Configuration file for input/output paths

## Usage
1. Edit the config.txt file to set the paths for your input and output files:
    input_file=path/to/system_input_file.txt
    output_file=path/to/system_output_file.txt

2. Run the main Python script:
    python main.py

3. After running the script, check the test_results.txt file for test results, including PASS or FAIL statuses.        
