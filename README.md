# Pesmarica rsk

Napisana v LaTeX



Latex deps:
* textlive-songs
* texlive-roboto
* (textlive-synctex for phpstorm) 



## Kako compilat vse?


* pdflatex
* https://tex.stackexchange.com/questions/122023/songs-package-index-generation


how to:
1. Run `pdflatex`
2. Run `texlua tools/songidx.lua out/titleidx.sxd out/titleidx.sbx`
3. Run `pdflatex` again

``