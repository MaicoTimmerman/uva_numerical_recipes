# REPLACE STUDENT NAMES WITH YOURS
ASSIGMENT=ass2
STUDENT_NAMES := maico_timmerman_robin_klusman
DOCS := $(shell ls docs/report.pdf)
DELIVERABLE := $(STUDENT_NAMES)_$(ASSIGMENT).tar.gz
PYTHON_FILES := $(shell ls *.py)

$(info $(PYTHON_FILES))

all: $(DELIVERABLE)

check: $(PYTHON_FILES)
	pep8 $^
	pyflakes $^
	touch $(@)

$(DELIVERABLE): $(PYTHON_FILES) $(DOCS) check
	tar -czf $@ $(PYTHON_FILES) $(DOCS)
