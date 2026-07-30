#!/bin/zsh
set -euo pipefail

repository_root="$(cd "$(dirname "$0")/.." && pwd)"
diagram_root="$repository_root/docs/workflows/p5-archive-browser"
guide_markdown="$repository_root/P5_ARCHIVE_BROWSER_ILLUSTRATED_WORKFLOW_GUIDE.md"
guide_pdf="$repository_root/P5_ARCHIVE_BROWSER_ILLUSTRATED_WORKFLOW_GUIDE.pdf"
pdf_python="${PDF_PYTHON:-python3}"

diagrams=(
  "catalog-ingest"
  "search-and-retrieve"
  "folder-restore"
)

for diagram in "${diagrams[@]}"; do
  npx -y @mermaid-js/mermaid-cli \
    --input "$diagram_root/$diagram.mmd" \
    --output "$diagram_root/$diagram.svg" \
    --backgroundColor transparent \
    --width 1600

  npx -y @mermaid-js/mermaid-cli \
    --input "$diagram_root/$diagram.mmd" \
    --output "$diagram_root/$diagram.png" \
    --backgroundColor white \
    --width 1800 \
    --scale 2
done

if ! "$pdf_python" -c "import reportlab" >/dev/null 2>&1; then
  echo "PDF generation requires Python 3 with ReportLab." >&2
  echo "Install ReportLab or set PDF_PYTHON to an environment that provides it." >&2
  exit 1
fi

"$pdf_python" "$repository_root/script/build_p5_archive_browser_illustrated_pdf.py" \
  --input "$guide_markdown" \
  --output "$guide_pdf"

echo "Rendered ${#diagrams[@]} workflow illustrations and $guide_pdf"
