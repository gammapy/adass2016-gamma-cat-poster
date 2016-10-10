TARGET=P6.7
LATEX=latex
BIBTEX=bibtex

all: $(TARGET).pdf

$(TARGET).pdf: *.tex figures/* $(TARGET).bib

%.pdf: %.tex
	$(LATEX) $<
	$(BIBTEX) $*
	$(LATEX) $<
	$(LATEX) $<
	dvipdf $(TARGET)

make clean:
	- rm -f $(TARGET).pdf $(TARGET).aux $(TARGET).log $(TARGET).bbl $(TARGET).fff
	- rm -f *.aux */*.aux */*/*.aux

tarball:
	- tar -cvzf $(TARGET).tar.gz \
	$(TARGET).tex \
	$(TARGET).bib \
	$(TARGET).bbl \
	figures/lightcurve.eps \
	asp2014.sty asp2014.bst \
	Makefile
