SRC = presentation.tex
PDF = presentation.pdf
AUX = presentation.aux
TEXC := xelatex
TEXC_OPTS += -shell-escape
TEXMFHOME = $(shell kpsewhich -var-value=TEXMFHOME)
INSTALL_DIR = $(TEXMFHOME)/tex/latex/utopia

.PHONY: clean install

all: $(PDF)

$(AUX):
	$(TEXC) $(TEXC_OPTS) $(SRC)

$(PDF): beamerthemeutopia.sty $(AUX) $(SRC)
	$(TEXC) $(TEXC_OPTS) $(SRC)

clean:
	@rm -f $(PDF)
	@git clean -xf

install:
	mkdir -p $(INSTALL_DIR)
	cp *.sty $(INSTALL_DIR)
