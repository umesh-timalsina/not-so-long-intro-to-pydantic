LATEX_COMPILER			?= latexmk
HTML_CONVERTER 			?= pdf2htmlEX
SOURCEDIR				= ./post
BUILDDIR 				= post
ROOTNAME 				= post

help:
	@$(LATEX_COMPILER) --help

.PHONY: help Makefile

clean:
	git clean -x -f
	rm -rf _minted-post

html:
	@$(LATEX_COMPILER) -pdf -jobname="$(BUILDDIR)/$(ROOTNAME)" -shell-escape "$(SOURCEDIR)/$(ROOTNAME)"
	@$(HTML_CONVERTER) --zoom 1.5 "$(BUILDDIR)/$(ROOTNAME).pdf"
	mv "$(ROOTNAME).html" "$(BUILDDIR)"


