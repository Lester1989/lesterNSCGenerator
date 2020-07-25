# =================================================================
# FORMATTING METHODS
# =================================================================

def Table(col, data, language='LATEX'):
    result = ''
    if language == 'LATEX':
        result += r'\begin{tabular}{|' + ''.join(['l|' for i in range(col)]) + '}\n\\hline '
        colIdx = 0
        for field in data[:-1]:
            result += field if len(field) < 7 else f'\\small{{{field}}}'
            if colIdx < col - 1:
                result += '&'
                colIdx += 1
            else:
                result += Newline(language) + r'\hline '
                colIdx = 0
        result += (data[-1] if len(data[-1]) < 7 else f'\\small{{{data[-1]}}}') + Newline(language) + r'\hline ' + '\n'
        result += r'\end{tabular}' + Newline(language)
    elif language == 'HTML':
        result += '<table cellspacing="10">  <tr>'
        colIdx = 0
        for field in data[:-1]:
            result += f' <td>{field}</td> '
            if colIdx < col - 1:
                colIdx += 1
            else:
                result += '</tr>\n  <tr>'
                colIdx = 0
        result += f' <td>{data[-1]}</td> '
        result += '</tr>\n</table>\n'
    elif language == 'Plain':

        colIdx = 0
        for field in data[:-1]:
            result += f' {field: <16} '
            if colIdx < col - 1:
                colIdx += 1
            else:
                result += '\n'
                colIdx = 0
        result += f' {data[-1]: <16} \n'
        pass
    return result


def Header(Name, Nachname, language='LATEX',level=2):
    if language == 'LATEX':
        return f'\\{["chapter","section","subsection","subsubsection","paragraph","subparagraph"][level]}*{{{Name} {Nachname}}}\n'
    elif language == 'HTML':
        return f'<h{level}>{Name} {Nachname}</h{level}>\n'
    elif language == 'Plain':
        return f'{"".join(["#" for i in range(level+1)])} {Name} {Nachname} {"".join(["#" for i in range(level+1)])}\n'
    else:
        return ''


def Bold(text, language='LATEX'):
    if language == 'LATEX':
        return f'\\textbf{{{text}}}'
    elif language == 'HTML':
        return f'<b>{text}</b>'
    elif language == 'Plain':
        return text.upper()
    else:
        return ''


def Newline(language='LATEX'):
    if language == 'LATEX':
        return r'\\'+'\n'
    elif language == 'HTML':
        return r'<br>'+'\n'
    elif language == 'Plain':
        return '\n'
    else:
        return ''


def StartCapital(text):
    return text[0].upper()+text[1:]


def ListLines(lines, language='LATEX'):
    if language == 'LATEX':
        result = r'\begin{itemize}' + '\n'
        for line in lines:
            result += f'\\item {line}\n'
        result += r'\end{itemize}' + '\n'
        return result
    elif language == 'HTML':
        result = '<ul>\n'
        for line in lines:
            result += f'<li> {line}</li>\n'
        result += '</ul>\n'
        return result
    elif language == 'Plain':
        result = ''
        for line in lines:
            result += f' * {line}\n'
        return result
    else:
        return ''