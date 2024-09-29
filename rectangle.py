from pathlib import Path
import sys


class Rectangle:
    """Class to represent the rectangle work area and check point validity."""

    def __init__(self, bottom_left, top_left, bottom_right, top_right):
        self.bottom_left = bottom_left
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.top_right = top_right

    @staticmethod
    def validate_coordinates(coordinates):
        """Ensure each point has both x and y coordinates."""
        if not all(isinstance(point, tuple) and len(point) == 2 for point in coordinates):
            raise ValueError("All points must be tuples with exactly two values (x, y).")

    def create_rectangle_from_file(file_path):
        """Function to create a Rectangle from the input file."""
        path = Path(file_path)  # Create a Path object for the file

        # Read the entire content of the file
        content = path.read_text()

        if 'Rectangle' in content:
            lines = content.splitlines()  # Split content into lines    

            # Search for 'Rectangle' in the lines
            for i, line in enumerate(lines):
                if 'Rectangle' in line:
                    # Ensure there's a next line for coordinates
                    if i + 1 < len(lines):
                        try:
                            # Extract and evaluate the coordinates
                            rectangle_coords = eval(lines[i + 1].strip())
                            # Validate the coordinates length
                            if len(rectangle_coords) != 4:
                                raise ValueError("Rectangle must have exactly four coordinate points.")

                            return Rectangle(
                                bottom_left=rectangle_coords[0],
                                top_left=rectangle_coords[1],
                                bottom_right=rectangle_coords[2],
                                top_right=rectangle_coords[3]
                            )
                        except (SyntaxError, ValueError) as e:
                            print(f"Error: {str(e) if isinstance(e, ValueError) else 'Rectangle co-ordinate x or y is missing. Please check the input file.'}")
                            sys.exit(1)

        print("Error: Rectangle definition not found in the file.")
        sys.exit(1)         
       
    def is_within_rectangle(self, point):
        """Check if the point is within the axis-aligned rectangle bounds."""
        # Validate that point has exactly two values
        if not isinstance(point, (tuple, list)) or len(point) != 2:
            return False, None, None, "Invalid Point Format."

        x, y = point      
    
        # Extract the x and y coordinates of the rectangle corners
        x_min = min(self.bottom_left[0], self.bottom_right[0])  # -4
        #print(f"I am x min {x_min}")
        x_max = max(self.bottom_left[0], self.bottom_right[0])  # 160
        #print(f"I am x min {x_max}")
        y_min = min(self.bottom_left[1], self.top_left[1])      # -150
        #print(f"I am x min {y_min}")
        y_max = max(self.bottom_left[1], self.top_left[1])      # 150
        #print(f"I am x min {y_max}")

        # Check if the point lies within the bounds
        is_within = x_min <= x <= x_max and y_min <= y <= y_max
        return is_within, (x_min, y_min), (x_max, y_max), None
