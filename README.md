# Filament Documentation Combiner

This project is a tool designed to combine the various markdown files from the Filament documentation into a single markdown file. This consolidation facilitates the use of the documentation as a single file knowledge source for ChatGPT's Assistants/GPTs, making it easier to integrate and reference within AI-based tools and applications.

## Purpose

The primary purpose of this tool is to streamline the process of referencing and utilizing Filament documentation by compiling it into a single, searchable, and manageable file. This is especially useful for integrating the documentation into AI-powered assistance platforms like ChatGPT, where having a single source file can significantly enhance the efficiency of information retrieval and processing.

## Features

-   **Recursive File Traversal**: Efficiently traverses the Filament documentation directory to locate all markdown files.
-   **Intelligent Sorting**: Sorts files based on 'book' and 'chapter' to maintain the logical structure of the documentation.
-   **Front Matter Modification**: Injects a `file:` tag into the header of each file for easy identification.
-   **Content Cleaning**: Strips out specific lines that are not needed in the combined documentation (e.g., component imports).

## How to Use

> [!NOTE]
> The paths are currently hardcoded, I will be changing this to be more flexible in the future.

1. Clone the repository to your local machine.
2. The script currently looks for the filament repo to be `../filament` relative to the script.
3. Run the script to combine the documentation files into a single markdown file.

```bash
python main.py
```
