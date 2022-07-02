script_path=$PWD

export SONGIDX_LOCALE=sl_SI.UTF-8

echo "locale set to ${SONGIDX_LOCALE}"

echo "[generatePdf.sh] changing to source directory"
cd ../src || exit 2

mkdir -p ../out || exit 3

echo "[generatePdf.sh] Compiling list of songs"
pdflatex -file-line-error -interaction=nonstopmode -synctex=1  -output-format=pdf -output-directory=../out main.tex

echo "[generatePdf.sh] Building index"
texlua $script_path/songidx.lua -l sl_SI.UTF-8 ../out/titleidx.sxd ../out/titleidx.sbx || exit 5
echo "[generatePdf.sh] Generating pdf file"

pdflatex -file-line-error -interaction=nonstopmode -synctex=1  -output-format=pdf -output-directory=../out main.tex
echo "[generatePdf.sh] Pdf generated at ../out/main.pdf"