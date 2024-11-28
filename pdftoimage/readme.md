A Python script that converts all PDF files in a directory to JPEG images using the `pdf2image` library.



Explaining the script and its usage:

This Python script does the following:

1. It uses the `pdf2image` library to convert PDF files to JPEG images.
2. By default, it:
   - Looks for PDF files in the current directory
   - Creates a 'converted_images' subdirectory to store the output
   - Converts each PDF to JPEG at 200 DPI resolution

Prerequisites:
1. You'll need to install the required Python libraries:
   ```
   pip install pdf2image Pillow
   ```

2. Install poppler for your operating system:
   - Ubuntu/Debian: `sudo apt-get install poppler-utils`
   - macOS (with Homebrew): `brew install poppler`
   - Windows: Download poppler and add it to your system PATH

Customization Options:
- You can specify a custom input directory
- You can specify a custom output directory
- You can adjust the DPI (resolution) of the output images

Example usage in the script shows:
- Simple usage: `convert_pdfs_to_jpeg()` (uses current directory)
- Custom usage: `convert_pdfs_to_jpeg(input_dir='/path/to/pdfs', output_dir='/path/to/output', dpi=300)`

Features:
- Handles multiple-page PDFs (each page saved as a separate JPEG)
- Prints conversion progress and any errors
- Creates output directory if it doesn't exist

Would you like me to explain anything further about the script?