import fitz


def extract_from_pdf(path, text_file):
    document = fitz.open(path)

    with open(text_file, "w", encoding="utf-8") as text_file:
        for page_num in range(document.page_count):
            page = document.load_page(page_num)
            text = page.get_text()

            text_file.write(text)

    document.close()


pdf_path = "path/to/document"
file_name = "output.txt"

extract_from_pdf(pdf_path, file_name)
