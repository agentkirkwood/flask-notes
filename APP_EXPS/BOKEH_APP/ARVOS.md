# ARVOS - A RNA-seq Visualization and Organization System

**Version:** 0.1.1  
**Authors:** William Montgomery, Gareth Halladay, Amber Scott, Anela Tosevska, Frank Burkholder, Adam Richards, Andrew Gaines  
**License:** MIT License  
**Copyright:** This document has been placed in the public domain.

## Introduction

RNA-Seq technologies have revolutionized the biological sciences. One challenging aspect of these data is that there is so much information contained within a given experiment that results sections do little more than scratch the surface. Results change with time, because models get changed or updated and things like annotations are continually changing.

## Purpose

The first objective here is to create an interactive results summary environment. All versions of the results can be displayed and iterative updates should be made easy. The backbone of this objective is Flask and AWS.

This ties into the second objective where we want to create an environment that **encourages** the comparison of models. Scikit-learn has become one of the easiest toolkits to carry out predictive analytics and it is at the center of our solution for this objective.

## Features

- **Interactive heatmaps** for differential expression analysis
- **Gene set visualization** for enrichment analysis
- **BLAST mapping** integration
- **Gene Ontology queries**
- **Model comparison** environment using scikit-learn
- **Iterative results updates** with version control

## Software Stack

- [PostgreSQL](https://www.postgresql.org) - Database management
- [SQLAlchemy](http://www.sqlalchemy.org) - Python SQL toolkit
- [htsint](http://ajrichards.github.io/htsint) - High-Throughput Sequencing INTegrate
- [DESeq2](http://bioconductor.org/packages/release/bioc/html/DESeq2.html) - Differential expression analysis
- [scikit-learn](http://scikit-learn.org/stable) - Machine learning toolkit
- [Flask](http://flask.pocoo.org) - Web framework
- [Bokeh](https://bokeh.org) - Interactive visualization library (see [bokeh.md](bokeh.md) for details)

## About htsint

`htsint` (High-Throughput Sequencing INTegrate) is a Python package used to create gene sets for the study of high-throughput sequencing data. The goal is to create functional modules through the integration of heterogeneous types of data. These functional modules are primarily based on the Gene Ontology, but as the package matures, additional sources of data will be incorporated. The functional modules produced can be subsequently tested for significance in terms of differential expression in RNA-Seq or microarray studies using gene set enrichment analysis.

## Running the Application

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask app:
```bash
python app.py
```

3. Navigate to `http://localhost:8000` in your browser

## Useful References

- **RNA-Seq Analysis:** [https://www.ncbi.nlm.nih.gov/pubmed/26399714](https://www.ncbi.nlm.nih.gov/pubmed/26399714)
- **Differential Expression:** [http://www.biorxiv.org/content/early/2016/12/02/091280.article-info](http://www.biorxiv.org/content/early/2016/12/02/091280.article-info)
- **Pieris Supplement:** [https://ajrichards.github.io/public/pieris-supplement/index.html](https://ajrichards.github.io/public/pieris-supplement/index.html)
- **AAD Analysis:** [https://ajrichards.github.io/public/aad/index.html](https://ajrichards.github.io/public/aad/index.html)

## Documentation

Full documentation is pending. For now, refer to the individual component documentation:
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Bokeh Documentation](https://docs.bokeh.org/)
- [htsint Documentation](http://ajrichards.github.io/htsint)
