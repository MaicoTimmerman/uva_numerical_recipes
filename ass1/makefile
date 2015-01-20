# REPLACE STUDENT NAMES WITH YOURS
STUDENT_NAMES := maico_timmerman_robin_klusman
DOCS := $(shell ls docs/report.pdf)
DELIVERABLE := $(STUDENT_NAMES).tar.gz
PYTHON_FILES := assignment1.py

all: $(DELIVERABLE)

check: $(PYTHON_FILES)
	pep8 $^
	pyflakes $^
	touch $(@)

$(DELIVERABLE): $(PYTHON_FILES) $(DOCS) check
	tar -czf $@ $(PYTHON_FILES) $(DOCS)
