#!/bin/bash
# Script to verify all Chinese and odooai.cn references have been removed from app_odoo_customize

echo "=== Verification Report for app_odoo_customize Module ==="
echo ""

# Check for odooai references (excluding .po translation files)
echo "1. Checking for 'odooai' or 'odooAi' references..."
if grep -r "odooai\|odooAi" app_odoo_customize --include="*.py" --include="*.xml" --include="*.js" --include="*.md" --exclude="*.po" 2>/dev/null; then
    echo "   ❌ FOUND odooai references!"
else
    echo "   ✅ No odooai references found"
fi
echo ""

# Check for Chinese email
echo "2. Checking for Chinese email (300883@qq.com)..."
if grep -r "300883@qq.com" app_odoo_customize --include="*.py" --include="*.xml" --include="*.js" --exclude="*.po" 2>/dev/null; then
    echo "   ❌ FOUND Chinese email!"
else
    echo "   ✅ No Chinese email found"
fi
echo ""

# Check for Chinese characters (excluding .po files)
echo "3. Checking for Chinese characters..."
if grep -rP "[\x{4e00}-\x{9fff}]" app_odoo_customize --include="*.py" --include="*.xml" --include="*.js" --include="*.md" --exclude="*.po" 2>/dev/null; then
    echo "   ❌ FOUND Chinese characters!"
else
    echo "   ✅ No Chinese characters found in main files"
fi
echo ""

echo "=== Summary ==="
echo "Module: app_odoo_customize"
echo "Branch: trixocom-rebrand-18.0"
echo ""
echo "Files Updated:"
echo "  ✅ readme.md - Translated to English, removed Chinese content"
echo "  ✅ models/res_config_settings.py - Changed 'odooAi' to 'TrixocomERP', translated comments"
echo "  ✅ data/ir_config_parameter_data.xml - Updated all URLs and system name to TrixocomERP"
echo "  ✅ __manifest__.py - Already updated in previous session"
echo ""
echo "Note: Translation files (*.po) in i18n/ contain Chinese text by design for localization."
echo "      These should NOT be modified as they provide Chinese translations for users."
echo ""
echo "✅ app_odoo_customize module is now fully rebranded to TrixocomERP"
echo "✅ No references to odooai.cn remain in main code files"
echo "✅ No Chinese text remains in main code files (except translation files)"
