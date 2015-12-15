push: skript.pdf
	git commit -a -m "autocommit"
	git push origin master

%.pdf: %.tex
	pdflatex -shell-escape -file-line-error -interaction=nonstopmode \
		-output-directory="$(@D)" -halt-on-error $< *.tex
