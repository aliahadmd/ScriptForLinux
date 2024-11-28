import os
import glob
from pdf2image import convert_from_path

def convert_pdfs_to_jpeg(input_dir='.', output_dir=None, dpi=200):
    """
    Convert all PDF files in the specified directory to JPEG images.
    
    Args:
    input_dir (str): Directory containing PDF files to convert. Defaults to current directory.
    output_dir (str): Directory to save converted images. Defaults to a 'converted_images' subdirectory.
    dpi (int): Resolution of the output images. Higher values mean higher quality but larger file size.
    """
    # Set default output directory if not specified
    if output_dir is None:
        output_dir = os.path.join(input_dir, 'converted_images')
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Find all PDF files in the input directory
    pdf_files = glob.glob(os.path.join(input_dir, '*.pdf'))
    
    # Convert each PDF file
    for pdf_path in pdf_files:
        try:
            # Extract the base filename without extension
            base_filename = os.path.splitext(os.path.basename(pdf_path))[0]
            
            # Convert PDF to images
            images = convert_from_path(pdf_path, dpi=dpi)
            
            # Save each page as a separate JPEG
            for i, image in enumerate(images):
                # If there are multiple pages, add page number to filename
                if len(images) > 1:
                    output_filename = f"{base_filename}_page{i+1}.jpg"
                else:
                    output_filename = f"{base_filename}.jpg"
                
                # Full path for the output image
                output_path = os.path.join(output_dir, output_filename)
                
                # Save the image
                image.save(output_path, 'JPEG')
                print(f"Converted: {pdf_path} -> {output_path}")
        
        except Exception as e:
            print(f"Error converting {pdf_path}: {e}")

def main():
    # Example usage
    convert_pdfs_to_jpeg()
    
    # You can also specify custom input and output directories
    # convert_pdfs_to_jpeg(input_dir='/path/to/pdf/directory', 
    #                      output_dir='/path/to/output/directory', 
    #                      dpi=300)

if __name__ == "__main__":
    main()

# Prerequisites:
# 1. Install required libraries:
#    pip install pdf2image Pillow
#
# 2. Install poppler (system-specific):
#    - On Ubuntu/Debian: sudo apt-get install poppler-utils
#    - On macOS (with Homebrew): brew install poppler
#    - On Windows: Download poppler and add to PATH