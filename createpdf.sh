# Load variables
set -a
source .env
set +a

# Name of html file
HTMLFILE="coverletter.html"

# Name of final PDF file
PDFFILE="coverletter.pdf"

# Replace variables in html file
(envsubst < $HTMLFILE) > print.html

# Run Python to insert content
source ./.venv/bin/activate
python3 main.py

# Create PDF
weasyprint print.html $PDFFILE

# Clean up
# rm print.html

# Open PDF with the system's standard pdf viewer
open $PDFFILE
