LATEXMK=latexmk -dvi- -pdf -interaction=nonstopmode -latexoption="-shell-escape"
TARGET=bopc_report.pdf
STYS = $(sort $(wildcard *.sty))
SRCES = $(sort $(wildcard *.tex))
FIGS = $(wildcard figs/*)

all: $(TARGET) 

%.pdf: %.tex $(STYS) $(SRCES) $(FIGS)
	$(LATEXMK) $<

clean:
	rm -f *.aux *.dvi *.fdb_latexmk *.fls *.log *.out *.out.ps *.toc *.pdf *.bbl *.blg *.bbl *.bcf *.run.xml
