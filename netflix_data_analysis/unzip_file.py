import os
import zipfile


def unzip_and_rename(zip_path, extract_to='.', new_filename='Netflix_shows_movies.csv'):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    # Automatically rename the first extracted .csv file
    for file in os.listdir(extract_to):
        if file.endswith(".csv") and file != new_filename:
            original_path = os.path.join(extract_to, file)
            target_path = os.path.join(extract_to, new_filename)

            # If target file exists, remove it to allow overwrite
            if os.path.exists(target_path):
                os.remove(target_path)

            os.rename(original_path, target_path)
            break
