import os
import sys


def locate_folder(folder_name, search_path):
    """
    Locate a folder with the specified name starting from a given directory.

    Args:
        folder_name (str): Name of the folder to find.
        search_path (str): Directory to start the search.

    Returns:
        str: Full path to the folder if found, else None.
    """
    for root, dirs, _ in os.walk(search_path):
        if folder_name in dirs:
            return os.path.join(root, folder_name)
    return None


def run_commands(folder_path):
    """
    Placeholder function for running commands in the located folder.
    """
    print(f"Running commands in: {folder_path}")
    # Add custom logic here.


def search_docker_folder(base_path):
    """
    Search for the 'docker' folder in the given base path.

    Args:
        base_path (str): Base path to search for the 'docker' folder.

    Returns:
        str: Full path to the 'docker' folder if found, else None.
    """
    docker_folder = locate_folder("docker", base_path)
    return docker_folder


def main():
    folder_name = "zeuz123"  # Folder name to search for

    # Prompt user for the directory to search
    search_path = input("Enter the directory to search: ").strip() + ":\\"  # Append '\\' for Windows style

    # Normalize the directory path for cross-platform compatibility
    search_path = os.path.expanduser(search_path)
    search_path = os.path.abspath(search_path)

    # Validate the directory
    if not os.path.isdir(search_path):
        print(f"Error: The directory '{search_path}' does not exist or is invalid.")
        sys.exit(1)

    # Search for the folder
    print(f"Searching for folder '{folder_name}' in '{search_path}'...")
    folder_path = locate_folder(folder_name, search_path)

    if folder_path:
        print(f"{folder_name} folder found: {folder_path}")

        # Now search for the "docker" folder within the found folder path
        docker_folder_path = search_docker_folder(folder_path)

        if docker_folder_path:
            print(f"Docker folder found: {docker_folder_path}")
            run_commands(docker_folder_path)
        else:
            print("Docker folder not found within the folder.")
            sys.exit(1)
    else:
        print(f"Folder '{folder_name}' not found in '{search_path}'.")
        sys.exit(1)


if __name__ == "__main__":
    main()
