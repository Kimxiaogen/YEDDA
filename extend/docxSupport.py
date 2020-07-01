import docx

def readdocx(filename):
    file = docx.Document(filename)
    text = ''
    for para in file.paragraphs:
        text += (para.text + '\n')
    return text