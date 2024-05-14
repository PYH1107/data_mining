import fitz  # PyMuPDF
import json

def pdf_to_jsonl(pdf_path, jsonl_path):
    # 打開PDF文件
    pdf_document = fitz.open("C:\\Users\\ASUS\\Documents\\github\\data_mining\\textbook.pdf")

    # 初始化一個空的列表來儲存頁面數據
    pages_data = []

    # 遍歷每一頁
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        page_text = page.get_text("text")

        # 創建一個字典來儲存頁面數據
        page_data = {
            "page_number": page_num + 1,
            "text": page_text
        }
        pages_data.append(page_data)

    # 將數據寫入JSONL文件
    with open(jsonl_path, 'w', encoding='utf-8') as jsonl_file:
        for page_data in pages_data:
            jsonl_file.write(json.dumps(page_data) + "\n")

    print(f"PDF content has been converted to {jsonl_path}")

# 調用函數
pdf_to_jsonl("input.pdf", "output.jsonl")