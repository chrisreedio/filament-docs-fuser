import os
import re

def extract_book_and_chapter(file_path):
    # This function assumes the file_path is in the format 'packages/[book]/docs/[chapter]-[rest_of_filename].md'
    parts = file_path.split('/')
    book = parts[-3]  # The 'book' is the third last element in the path
    
    # Attempt to extract the chapter number
    try:
        chapter = int(parts[-1].split('-')[0])  # The 'chapter' is the first part of the filename before '-'
    except ValueError:
        # If not a number, assign a high number to sort it last
        chapter = float('inf')
        
    return book, chapter

def combine_markdown_files(directory):
    """
    Combines all markdown (.md) files within the given directory into a single markdown file.
    Files are sorted by 'book' then by 'chapter'.
    The header of each file is updated with a 'file:' tag showing the relative path excluding 'packages/'.
    """
    # Create a list to store the files with extracted 'book' and 'chapter'
    book_chapter_files = []

    # Regex pattern to match the front matter header of a markdown file
    front_matter_pattern = re.compile(r'^---\ntitle: (.+)\n---', re.MULTILINE)

    # Walk through the directory to find all .md files
    for subdir, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".md"):
                file_path = os.path.join(subdir, filename)
                book, chapter = extract_book_and_chapter(file_path)
                book_chapter_files.append((book, chapter, file_path))

    # Sort the files by 'book' then by 'chapter' number, handling non-numeric chapters
    book_chapter_files.sort(key=lambda x: (x[0], float(x[1]) if isinstance(x[1], str) else x[1]))


    # Open the combined markdown file to write
    combined_markdown_path = 'filament_documentation.md'
    with open(combined_markdown_path, 'w') as combined_file:
        for book, chapter, filepath in book_chapter_files:
            with open(filepath, 'r') as f:
                file_content = f.read()
                # Strip specific import lines
                file_content = re.sub(r'import .+ from "@components/.+\.astro"\n', '', file_content)
                file_content = re.sub(r'<AutoScreenshot[^>]+>', '', file_content)
                # Inject 'file:' tag with the relative path, excluding 'packages/'
                relative_path = os.path.relpath(filepath, directory)
                file_content = front_matter_pattern.sub(
                    rf'---\ntitle: \1\nfile: {relative_path}\n---', file_content)
                # Write the updated content to the combined file
                combined_file.write(file_content + '\n\n')

    return combined_markdown_path


# Directory containing markdown files
directory = '../filament'

# Call the function to combine markdown files
combine_markdown_files(directory)
