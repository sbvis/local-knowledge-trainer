# Cytosplore EvoViewer — end-user workflows

Source: https://viewer.cytosplore.org/documentation/evoviewer
Source type: Published EvoViewer user tutorial, checked 2026-11-15.
These instructions describe the published tutorial. Control placement may change between releases.

## Select cell types in EvoViewer

To select one or several cell types in the hierarchy:

1. Click a cell-type rectangle in the hierarchy to select that cell type. The selected cells appear highlighted in the scatterplot.
2. Hold Shift and click further cell-type rectangles to select more than one cell type.
3. Hold Ctrl and click a cell-type rectangle to zoom into that branch of the hierarchy. Hold Ctrl and click a parent rectangle to zoom out.

## Identify marker genes in EvoViewer

To identify marker genes for a specific cell population in EvoViewer:

1. Select the cell type by clicking its rectangle in the cell-type hierarchy. Shift-click to select multiple types if needed.
2. Click **Update** to calculate gene and cell-type characteristics for the selected cells.
3. In the gene table, select the **Species Appearance** column header to rank genes by their cross-species relevance.
4. Adjust the **Top N** field to change the gene-ranking threshold.
5. Select a gene from the left table to explore its expression; the scatterplot, right-hand table, and phylogenetic tree update together.

## Find cell abundance in EvoViewer

To compare cell abundance across species in EvoViewer:

1. Choose the relevant cell type in the hierarchy, then click **Update** to compute its characteristics.
2. Use the species table's abundance columns to inspect **Absolute** cell counts or **Relative** abundance.
3. Click a species-table column header to sort species by abundance.
4. Expand a column or hover over a table cell to read its numerical value.

## Explore gene expression across species

To explore expression of a selected marker gene:

1. Select the gene in the left-hand gene table.
2. Examine the right-hand species table and the scatterplot; the scatterplot displays cells colored by expression of that gene.
3. Select a species in the right-hand table to inspect its expression pattern.
4. Use **Revert** to restore the original species selection, or **Deselect** to clear the selected gene.

## Zoom into the cell type hierarchy in EvoViewer

To zoom into part of the cell-type hierarchy:

1. Hold Ctrl and click a cell-type rectangle to zoom into that branch.
2. Hold Ctrl and click a parent cell-type rectangle to zoom back out.

## Export table data in EvoViewer

To export gene and species tables as CSV files:

1. Click the export icon in the table view.
2. Click **Save Right Species Selection Table** to save species details as CSV.
3. Click **Save Left Gene Table** to save gene details as CSV.
