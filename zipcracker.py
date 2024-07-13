import zipfile
import itertools
import string

def brute_force_unzip(zip_path, output_dir, min_length, max_length):
    try:
        zip_path = os.path.expanduser(zip_path)  # Expand the tilde to full path
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            for r in range(min_length, max_length + 1):
                for password in itertools.product(string.ascii_letters + string.digits, repeat=r):
                    password = ''.join(password)
                    try:
                        zip_ref.extractall(path=output_dir, pwd=password.encode('utf-8'))
                        print(f"Success! The password is: {password}")
                        return True
                    except (RuntimeError, zipfile.BadZipFile):
                        continue
                    except Exception as e:
                        print(f"An error occurred: {e}")
                        return False

        print("Password not found.")
        return False

    except FileNotFoundError:
        print(f"Error: ZIP file '{zip_path}' not found.")
        return False
    except zipfile.BadZipFile:
        print(f"Error: '{zip_path}' is not a valid ZIP file.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    zip_path = input("Enter the path to the ZIP file: ").strip()
    output_dir = input("Enter the output directory: ").strip()
    min_length = int(input("Enter the minimum password length: ").strip())
    max_length = int(input("Enter the maximum password length: ").strip())
    brute_force_unzip(zip_path, output_dir, min_length, max_length)

