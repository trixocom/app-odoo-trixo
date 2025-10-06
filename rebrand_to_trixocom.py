#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to rebrand Odoo modules from odooAi to TrixocomERP
Removes Chinese characters and updates all references
"""

import os
import re
import sys
from pathlib import Path

# Replacement mappings
REPLACEMENTS = {
    # Domain replacements
    r'odooai\.cn': 'trixocom.com',
    r'www\.odooai\.cn': 'www.trixocom.com',
    r'https://www\.odooai\.cn': 'https://www.trixocom.com',
    r'http://www\.odooai\.cn': 'https://www.trixocom.com',
    r'demo\.odooapp\.cn': 'demo.trixocom.com',
    
    # Brand name replacements
    r'odooAi': 'TrixocomERP',
    r'OdooAi': 'TrixocomERP',
    r'odooai': 'trixocom',
    r'Odooai': 'Trixocom',
    r'ODOOAI': 'TRIXOCOM',
    
    # Email replacements
    r'300883@qq\.com': 'info@trixocom.com',
    
    # Company name replacements
    r'欧度智能': 'TrixocomERP',
    r'广州欧度智能科技有限公司': 'TrixocomERP',
}

# Common Chinese phrases to English translations
CHINESE_TO_ENGLISH = {
    # Module descriptions
    '应用': 'Application',
    '模块': 'Module',
    '增强': 'Enhancement',
    '优化': 'Optimization',
    '提速': 'Speed Boost',
    '自定义': 'Customize',
    '管理': 'Management',
    '批量': 'Batch',
    '快速': 'Quick',
    '高级': 'Advanced',
    '多层级': 'Multi-level',
    '树状': 'Tree',
    '导航': 'Navigator',
    '选择器': 'Selector',
    '产品': 'Product',
    '销售': 'Sales',
    '采购': 'Purchase',
    '库存': 'Inventory',
    '财务': 'Finance',
    '会计': 'Accounting',
    '人力资源': 'Human Resources',
    '制造': 'Manufacturing',
    '项目': 'Project',
    '联系人': 'Contacts',
    '客户': 'Customer',
    '供应商': 'Vendor',
}

def has_chinese(text):
    """Check if text contains Chinese characters"""
    return bool(re.search(r'[\u4e00-\u9fff]+', text))

def remove_chinese_comments(content):
    """Remove lines that are purely Chinese comments"""
    lines = content.split('\n')
    cleaned_lines = []
    
    for line in lines:
        # Skip lines that are purely Chinese comments
        if line.strip().startswith('#') and has_chinese(line):
            # Check if it's a comment line with only Chinese
            comment_content = line.split('#', 1)[1] if '#' in line else line
            if has_chinese(comment_content) and not re.search(r'[a-zA-Z]', comment_content):
                continue
        cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)

def translate_common_chinese(content):
    """Translate common Chinese phrases to English"""
    for chinese, english in CHINESE_TO_ENGLISH.items():
        content = content.replace(chinese, english)
    return content

def apply_replacements(content):
    """Apply all regex replacements to content"""
    for pattern, replacement in REPLACEMENTS.items():
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
    return content

def process_file(file_path):
    """Process a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply replacements
        content = apply_replacements(content)
        
        # Translate common Chinese phrases
        content = translate_common_chinese(content)
        
        # Remove Chinese-only comment lines
        if file_path.suffix in ['.py', '.js']:
            content = remove_chinese_comments(content)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Updated: {file_path}")
            return True
        
        return False
        
    except Exception as e:
        print(f"✗ Error processing {file_path}: {str(e)}")
        return False

def process_directory(directory):
    """Process all relevant files in directory"""
    # File extensions to process
    extensions = ['.py', '.xml', '.md', '.txt', '.po', '.pot', '.js', '.rst', '.csv']
    
    directory = Path(directory)
    files_processed = 0
    files_updated = 0
    
    print(f"\nScanning directory: {directory}")
    print("=" * 80)
    
    for ext in extensions:
        for file_path in directory.rglob(f"*{ext}"):
            # Skip __pycache__ and .git directories
            if '__pycache__' in str(file_path) or '.git' in str(file_path):
                continue
                
            files_processed += 1
            if process_file(file_path):
                files_updated += 1
    
    print("=" * 80)
    print(f"\nSummary:")
    print(f"  Files processed: {files_processed}")
    print(f"  Files updated: {files_updated}")
    print(f"  Files unchanged: {files_processed - files_updated}")

def main():
    """Main function"""
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = '.'
    
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory")
        sys.exit(1)
    
    print("=" * 80)
    print("TrixocomERP Rebranding Script")
    print("=" * 80)
    print("\nThis script will:")
    print("  1. Replace all odooAi references with TrixocomERP")
    print("  2. Replace odooai.cn domain with trixocom.com")
    print("  3. Translate common Chinese phrases to English")
    print("  4. Remove Chinese-only comment lines")
    print("\nPress Ctrl+C to cancel, or Enter to continue...")
    
    try:
        input()
    except KeyboardInterrupt:
        print("\n\nCancelled by user")
        sys.exit(0)
    
    process_directory(directory)
    
    print("\n" + "=" * 80)
    print("Rebranding complete!")
    print("=" * 80)
    print("\nNext steps:")
    print("  1. Review the changes with: git diff")
    print("  2. Test the modules to ensure they work correctly")
    print("  3. Commit the changes: git add . && git commit -m 'Rebrand to TrixocomERP'")

if __name__ == '__main__':
    main()
