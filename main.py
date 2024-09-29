from utils import read_config,check_file_exists_and_valid
from testsystem import TestSystem
from rectangle import Rectangle


def main():
    # Load config
    config = read_config()
    #print(config)
    
    # Check Input & Output file Exists and Valid
    check_file_exists_and_valid(config['input_file'])
    check_file_exists_and_valid(config['output_file'])

    # Create rectangle from input file
    rectangle = Rectangle.create_rectangle_from_file(config['input_file'])
    #print(f"Rectangle Co-ordinates from Input File: bottom_left={rectangle.bottom_left}, top_left={rectangle.top_left}, "f"bottom_right={rectangle.bottom_right}, top_right={rectangle.top_right}\n")

    # Initialize the test system
    test_system = TestSystem(rectangle)    
    
    # Load expected and actual points
    expected_points = test_system.load_points(config['input_file'])
    #print(f"Points from Input File: {expected_points}\n")
    
    actual_points = test_system.load_points(config['output_file'])
    #print(f"Points from output File: {actual_points}\n")
    
    # Compare points and log results
    results = test_system.compare_points(expected_points, actual_points)    
    test_system.log_results(results)


if __name__ == "__main__":
    main()
