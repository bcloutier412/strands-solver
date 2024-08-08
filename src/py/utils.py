import os

def convert_row_col_to_id(row, col):
  return (row * 6) + col

def is_in_matrix_bound(row, col, HEIGHT, WIDTH):
  if (row < 0 or row >= HEIGHT) or (col < 0 or col >= WIDTH):
    return False
  return True

def get_relative_file_path(path_from_file_location):
  # Get the directory where the script is located
  script_dir = os.path.dirname(os.path.abspath(__file__))

  # Build the path relative to the script's directory
  file_path = os.path.join(script_dir, path_from_file_location)

  return file_path