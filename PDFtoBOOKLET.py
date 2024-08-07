import PyPDF2

def create_booklet(input_pdf, output_pdf):
    reader = PyPDF2.PdfReader(input_pdf)
    writer = PyPDF2.PdfWriter()
    
    num_pages = len(reader.pages)
    
    # Calculer le nombre total de feuilles nécessaires pour le livret
    num_sheets = (num_pages + 3) // 4  # Arrondir au supérieur

    # Réorganiser les pages pour le livret
    for sheet in range(num_sheets):
        # Pages pour le recto et le verso de la feuille
        page_1 = reader.pages[num_pages - 1 - (sheet * 2)]
        page_2 = reader.pages[sheet * 2] if (sheet * 2) < num_pages else None
        page_3 = reader.pages[sheet * 2 + 1] if (sheet * 2 + 1) < num_pages else None
        page_4 = reader.pages[num_pages - 2 - (sheet * 2)] if (num_pages - 2 - (sheet * 2)) >= 0 else None
        
        # Ajouter les pages dans le bon ordre pour le livret
        if page_4 is not None:
            writer.add_page(page_4)  # Page D
        if page_1 is not None:
            writer.add_page(page_1)  # Page A
        if page_2 is not None:
            writer.add_page(page_2)  # Page B
        if page_3 is not None:
            writer.add_page(page_3)  # Page C

    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)

create_booklet('input.pdf', 'output_booklet.pdf')