import PyPDF2
import argparse
import os

def create_booklet(input_pdf, output_pdf):
    # Vérifier si le fichier d'entrée existe
    if not os.path.isfile(input_pdf):
        print(f"Error: The file '{input_pdf}' does not exist.")
        return

    # Si le fichier existe, continuer avec la création du livret (à compléter)
    print(f"File '{input_pdf}' exists. Proceeding with booklet creation...")

    try:
        with open(input_pdf, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            print(f"File '{input_pdf}' successfully opened. Number of pages: {len(reader.pages)}")
            # Placeholder pour le reste de la fonction à ajouter plus tard
    except Exception as e:
        print(f"Error opening file: {e}")

    writer = PyPDF2.PdfWriter()

    try:
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)
        print(f"Booklet created successfully: {output_pdf}")
    
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    parser = argparse.ArgumentParser(description='Create a booklet from a PDF file.')
    parser.add_argument('input_pdf', nargs='?', help='Path to the input PDF file.')
    parser.add_argument('output_pdf', nargs='?', help='Name of the output PDF file.')

    args = parser.parse_args()

    if not args.input_pdf:
        args.input_pdf = input('Enter the path to the input PDF file: ')
    if not args.output_pdf:
        args.output_pdf = input('Enter the name of the output PDF file: ')

    # Vérifier si le fichier d'entrée existe
    if not os.path.isfile(args.input_pdf):
        print(f"Error: The file '{args.input_pdf}' does not exist.")
        return

    create_booklet(args.input_pdf, args.output_pdf)

if __name__ == '__main__':
    main()