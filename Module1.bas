Attribute VB_Name = "Module1"

Sub dataprocess()
Dim i As Integer

Worksheets("finance").Cells(1, 2) = "book value per share"
Worksheets("finance").Cells(1, 3) = "P/E ratio"
Worksheets("finance").Cells(1, 4) = "P/B ratio"
Worksheets("finance").Cells(1, 5) = "PEG"
Worksheets("finance").Cells(1, 6) = "dividend yield"
Worksheets("finance").Cells(1, 7) = "cash/net income"
Worksheets("finance").Cells(1, 8) = "ROE"
Worksheets("finance").Cells(1, 9) = "ROA"
Worksheets("finance").Cells(1, 10) = "ROE change"
Worksheets("finance").Cells(1, 11) = "ROA change"
Worksheets("finance").Cells(1, 12) = "EPS increase"
Worksheets("finance").Cells(1, 13) = "net income increase"
Worksheets("finance").Cells(1, 14) = "EBITDA increase"
Worksheets("finance").Cells(1, 15) = "net income increase"
Worksheets("finance").Cells(1, 16) = "net income ratio"
Worksheets("finance").Cells(1, 17) = "net income ratio change"
Worksheets("finance").Cells(1, 18) = "reinvestment rate"
Worksheets("finance").Cells(1, 19) = "debt ratio"
Worksheets("finance").Cells(1, 20) = "fixed asset ratio"

For i = 1 To 9
Worksheets("finance").Cells(1 + i, 1) = 2013 + i
Next




End Sub
