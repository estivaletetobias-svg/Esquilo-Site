import os
import re

def fix_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 0. Basic Interaction and Title Fixes
    content = content.replace('user-select: none !important; -webkit-user-select: none !important; ', '')
    content = content.replace('overscroll-behavior: none; ', '')
    content = re.sub(r'<h1 style="font-size:\s*[^"]+">', '<h1>', content)

    # 1. Update CSS
    css_updates = """
        .tech-table { width: 100%; border-collapse: collapse; color: #FFF; }
        .tech-table th, .tech-table td { padding: 1rem; text-align: left; border-bottom: 1px solid var(--border); }
        .tech-table th { font-size: 0.65rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 1px; white-space: nowrap; }
        .tech-table td { font-size: 0.9rem; font-weight: 600; }
        .highlight { color: var(--primary); }
        .sec-header h1 { overflow-wrap: break-word; word-wrap: break-word; hyphens: auto; }

        /* Table Container for Mobile Scroll */
        .table-wrapper { width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch; margin-top: 1rem; border: 1px solid var(--border); border-radius: 12px; background: rgba(0,0,0,0.1); }
        .table-wrapper table { min-width: 600px; }
        .table-wrapper::-webkit-scrollbar { height: 4px; }
        .table-wrapper::-webkit-scrollbar-thumb { background: var(--border); border-radius: 10px; }

        .workout-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; }
        .workout-item { padding: 1rem; border-radius: 12px; background: rgba(0,0,0,0.2); border: 1px solid var(--border); }
        .workout-item h4 { color: var(--primary); margin-bottom: 0.5rem; font-size: 0.9rem; text-transform: uppercase; border-left: 2px solid var(--primary); padding-left: 0.8rem; }
        .exercise-list { list-style: none; }
        .exercise-list li { margin-bottom: 0.8rem; font-size: 0.9rem; color: #FFF; display: flex; justify-content: space-between; align-items: flex-start; gap: 1rem; border-bottom: 1px solid rgba(255,255,255,0.03); padding-bottom: 0.5rem; }
        .exercise-list li span { color: var(--text-secondary); font-size: 0.75rem; font-weight: 700; text-align: right; flex-shrink: 1; word-break: break-word; }
    """
    
    # Replace old tech-table CSS
    content = re.sub(r'\.tech-table\s*\{[^}]+\}.*?\.exercise-list\s*li\s*span\s*\{[^}]+\}', css_updates.strip(), content, flags=re.DOTALL)

    # Update Media Query
    media_query_fix = """
        @media (max-width: 1024px) {
            .sidebar { transform: translateX(-100%); transition: 0.3s; }
            .sidebar.open { transform: translateX(0); }
            .main-content { margin-left: 0; min-width: 0; width: 100%; }
            .content-section { padding: 6rem 1rem 4rem 1rem; width: 100%; max-width: 100vw; }
            .mob-menu { display: flex; }
            .sec-header h1 { font-size: 1.8rem; }
            .data-card { padding: 1.2rem; width: 100%; }
            .tech-table th, .tech-table td { padding: 0.8rem; }
            .exercise-list li { flex-direction: column; gap: 0.2rem; }
            .exercise-list li span { text-align: left; margin-left: 0; font-size: 0.7rem; }
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
