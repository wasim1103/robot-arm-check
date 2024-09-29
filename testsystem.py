import ast
from pathlib import Path


class TestSystem:
    def __init__(self, rectangle):
        self.rectangle = rectangle

    def load_points(self, file_path):
        """Function to load points, handling both input and output files."""
        points = []  # List to hold points, including invalid ones
        path = Path(file_path)  # Create a Path object for the file

        # Read the entire content of the file
        lines = path.read_text().splitlines()  # Split content into lines

        # Check if the file contains a "Points" section
        start_index = 0  # Default start index for output files
        for i, line in enumerate(lines):
            if 'Points' in line:
                # If 'Points' is found, set the start index to the line after it
                start_index = i + 1
                break

        # Process lines from the determined start index
        for line in lines[start_index:]:
            line = line.strip()
            if line:  # Only process non-empty lines
                try:
                    # Safely evaluate the tuple
                    point = ast.literal_eval(line)
                except (SyntaxError, ValueError):
                    # If parsing fails, store the line as a string (invalid entry)
                    point = line
                points.append(point)
        return points

    def compare_points(self, expected_points, actual_points):
        """Compare expected and actual points and return results."""
        results = []
        min_length = min(len(expected_points), len(actual_points))

        # Compare points up to the length of the shorter list
        for i in range(min_length):
            expected = expected_points[i]
            actual = actual_points[i]
            error_message = None

            # Check if expected point is within the rectangle
            is_within_expected, min_bounds, max_bounds, expected_error = self.rectangle.is_within_rectangle(expected)
            if expected_error:
                error_message = f"Expected point {expected}: {expected_error}"
            elif not is_within_expected:
                error_message = f"Expected point {expected} is outside the rectangle with bounds: {min_bounds} to {max_bounds}."
            else:
                # Check if actual point is within the rectangle
                is_within_actual, _, _, actual_error = self.rectangle.is_within_rectangle(actual)
                if actual_error:
                    error_message = f"Actual point {actual}: {actual_error}"
                elif not is_within_actual:
                    error_message = f"Actual point {actual} is outside the rectangle with bounds: {min_bounds} to {max_bounds}."
                elif expected != actual:
                    error_message = f"Expected {expected}, but got {actual}."

            # Determine result and log output
            status = 'PASS' if error_message is None else 'FAIL'
            results.append((expected, actual, status, error_message))
            print(f"Test {i + 1}: {status} - {error_message or f'Expected: {expected}, Actual: {actual}'}")

        # Handle any remaining points in expected
        if len(expected_points) > min_length:
            for j in range(min_length, len(expected_points)):
                results.append((expected_points[j], None, "FAIL", "Expected point not found in actual points."))
                print(f"Test {j + 1}: FAIL - Expected point {expected}: Expected point not found in actual points.")

        # Handle any remaining points in actual
        if len(actual_points) > min_length:
            for j in range(min_length, len(actual_points)):
                results.append((None, actual_points[j], "FAIL", "Extra point found in actual points."))
                print(f"Test {j + 1}: FAIL - Extra point found in actual points: {actual}.")

        return results

    def log_results(self, results, results_file="test_results.txt"):
        """Log the test results to a text file with aligned columns."""
        with open(results_file, 'w') as file:
            file.write(f"{'Expected visited Points':<30}{'Actual visited Points':<30}{'Test Result(PASS/FAIL)':<50}\n")
            file.write("=" * 110 + "\n")

            for expected, actual, result, error_message in results:
                if result == 'PASS':
                    file.write(f"{str(expected):<30}{str(actual):<30}{result:<50}\n")
                else:
                    # Append the error message directly to the 'FAIL' result
                    file.write(f"{str(expected):<30}{str(actual):<30}{result} - {error_message:<50}\n")
