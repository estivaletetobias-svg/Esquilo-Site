import os
import re

def fix_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update CSS
    css_updates = """
        .tech-table { width: 100%; border-collapse: collapse; color: #FFF; }
        .tech-table th, .tech-table td { padding: 1rem; text-align: left; border-bottom: 1px solid var(--border); min-width: 120px; }
        .tech-table th { font-size: 0.65rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 1px; white-space: nowrap; }
        .tech-table td { font-size: 0.9rem; font-weight: 600; }
        .highlight { color: var(--primary); }

        /* Table Container for Mobile Scroll */
        .table-wrapper { width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch; margin-top: 1rem; border: 1px solid var(--border); border-radius: 12px; background: rgba(0,0,0,0.1); }
        .table-wrapper::-webkit-scrollbar { height: 4px; }
        .table-wrapper::-webkit-scrollbar-thumb { background: var(--border); border-radius: 10px; }
    """
    
    # Replace old tech-table CSS
    content = re.sub(r'\.tech-table\s*\{[^}]+\}.*?\.highlight\s*\{[^}]+\}', css_updates.strip(), content, flags=re.DOTALL)

    # Update Media Query
    media_query_fix = """
        @media (max-width: 1024px) {
            .sidebar { transform: translateX(-100%); transition: 0.3s; }
            .sidebar.open { transform: translateX(0); }
            .main-content { margin-left: 0; }
            .content-section { padding: 6rem 1rem 4rem 1rem; }
            .mob-menu { display: flex; }
            .sec-header h1 { font-size: 2.2rem; }
            .data-card { padding: 1.5rem; }
            .tech-table th, .tech-table td { padding: 0.8rem; }
        }
    """
    content = re.sub(r'@media\s*\(max-width:\s*1024px\)\s*\{.*?\}\s*\}', media_query_fix.strip() + "\n", content, flags=re.DOTALL)

    # 2. Wrap Tables
    # Find all <table> tags and wrap them in <div class="table-wrapper"> if not already wrapped
    def wrap_table(match):
        table_html = match.group(0)
        # Check if already wrapped (crude check)
        if 'table-wrapper' in content[match.start()-50:match.start()]:
            return table_html
        return f'<div class="table-wrapper">{table_html}</div>'

    content = re.sub(r'<table[^>]*>.*?</table>', wrap_table, content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

directory = '/Users/tobiasestivalete/Downloads/Esquilo - Site'
for filename in os.listdir(directory):
    if filename.startswith('protocolo-') and filename.endswith('.html'):
        print(f"Fixing {filename}...")
        fix_html(os.path.join(directory, filename))
