# TrixocomERP Rebranding Guide

This guide explains how to complete the rebranding from odooAi to TrixocomERP.

## What Has Been Done

✅ Main README.md updated - Chinese content removed, all references updated
✅ app_odoo_customize/__manifest__.py updated - Main module rebranded
✅ Automated rebranding script created (rebrand_to_trixocom.py)

## Next Steps

### 1. Clone the Repository Locally

```bash
git clone https://github.com/trixocom/app-odoo-trixo.git
cd app-odoo-trixo
git checkout trixocom-rebrand
```

### 2. Run the Rebranding Script

This script will automatically process all files in the repository:

```bash
python3 rebrand_to_trixocom.py .
```

The script will:
- Replace all `odooai.cn` with `trixocom.com`
- Replace all `odooAi` variations with `TrixocomERP`
- Translate common Chinese phrases to English
- Remove Chinese-only comment lines
- Update email addresses from 300883@qq.com to info@trixocom.com

### 3. Review the Changes

```bash
git diff
```

Review the changes to ensure everything looks correct. The script processes:
- Python files (.py)
- XML files (.xml)
- Markdown files (.md)
- Text files (.txt)
- Translation files (.po, .pot)
- JavaScript files (.js)
- CSV files (.csv)

### 4. Manual Review Needed

After running the script, you should manually check:

1. **Banner images** in `static/description/` folders
   - Look for images with Chinese text or odooAi branding
   - Replace with TrixocomERP branding

2. **Translation files** in `i18n/` folders
   - The script handles some translations, but context-specific translations may need manual review

3. **README files** in individual modules
   - Check module-specific README files for Chinese content

4. **Data files** with hardcoded text
   - Review XML data files for Chinese strings

5. **Website/Portal templates**
   - Check for any hardcoded company information

### 5. Test the Modules

Before committing, it's recommended to:

1. Install the modules in a test Odoo instance
2. Verify that all strings appear correctly in English
3. Check that links work (especially documentation links)
4. Ensure no Chinese characters appear in the UI

### 6. Commit and Push

```bash
git add .
git commit -m "Complete rebranding from odooAi to TrixocomERP

- Removed all Chinese content
- Replaced odooai.cn with trixocom.com
- Updated all brand references to TrixocomERP
- Translated common phrases to English
- Updated contact information"

git push origin trixocom-rebrand
```

### 7. Create a Pull Request

Create a pull request from `trixocom-rebrand` to `18.0` branch for final review.

## Common Replacements Made

| Original | Replacement |
|----------|-------------|
| odooai.cn | trixocom.com |
| www.odooai.cn | www.trixocom.com |
| demo.odooapp.cn | demo.trixocom.com |
| odooAi | TrixocomERP |
| 欧度智能 | TrixocomERP |
| 300883@qq.com | info@trixocom.com |

## Files Modified by Script

The script processes all files in:
- All module directories (app_*)
- Root level files
- Documentation files
- Translation files

## Known Limitations

The script does NOT:
- Modify binary files (images, PDFs)
- Translate complex Chinese sentences (only common phrases)
- Modify files in `.git` or `__pycache__` directories

These need to be handled manually if needed.

## Troubleshooting

### Script fails with encoding error
Ensure you're using Python 3 and the files are UTF-8 encoded:
```bash
python3 --version  # Should be 3.6+
```

### Some Chinese characters remain
The script only translates common phrases. For complex Chinese text:
1. Identify the file
2. Manually translate or remove the content
3. Consider using a translation service for complex text

### Links are broken
Update any hardcoded links in:
- res_config_settings views
- user menu templates
- documentation references

## Support

For questions or issues:
- Email: info@trixocom.com
- Website: https://www.trixocom.com

---

**Note**: Always backup your repository before running mass replacements!
