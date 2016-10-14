TARGET=P6-7
LATEX=latex
BIBTEX=bibtex

all: $(TARGET).pdf

$(TARGET).pdf: *.tex $(TARGET).bib

%.pdf: %.tex
	$(LATEX) $<
	$(BIBTEX) $*
	$(LATEX) $<
	$(LATEX) $<
	dvipdfm $(TARGET)

make clean:
	- rm -f $(TARGET).pdf $(TARGET).aux $(TARGET).log $(TARGET).bbl $(TARGET).fff
	- rm -f *.aux */*.aux */*/*.aux

tarball:
	- tar -cvzf $(TARGET).tar.gz \
	copyrightForm_P6-7_deil.pdf \
	$(TARGET).tex \
	$(TARGET).bib \
	$(TARGET).bbl \
	allsky.eps \
	asp2014.sty asp2014.bst \
	Makefile
