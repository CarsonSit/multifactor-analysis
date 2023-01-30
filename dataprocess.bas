Attribute VB_Name = "Module1"


Sub dataprocess()

Sheets.Add.Name = "finance"

Dim i As Integer

For i = 1 To 10
Worksheets("finance").Cells(1 + i, 1) = 2012 + i
Next

For i = 1 To 10
Worksheets("Sheet 1").Cells(16, 15 + i).Copy Worksheets("finance").Cells(1 + i, 2)
Next
Worksheets("Sheet 1").Cells(16, 1).Copy Worksheets("finance").Cells(1, 2)

For i = 1 To 10
Worksheets("Sheet 1").Cells(24, 15 + i).Copy Worksheets("finance").Cells(1 + i, 3)
Next
Worksheets("Sheet 1").Cells(24, 1).Copy Worksheets("finance").Cells(1, 3)

For i = 1 To 10
Worksheets("Sheet 1").Cells(26, 15 + i).Copy Worksheets("finance").Cells(1 + i, 4)
Next
Worksheets("Sheet 1").Cells(26, 1).Copy Worksheets("finance").Cells(1, 4)

For i = 1 To 10
Worksheets("Sheet 1").Cells(28, 15 + i).Copy Worksheets("finance").Cells(1 + i, 5)
Next
Worksheets("Sheet 1").Cells(28, 1).Copy Worksheets("finance").Cells(1, 5)

For i = 1 To 10
Worksheets("Sheet 1").Cells(32, 15 + i).Copy Worksheets("finance").Cells(1 + i, 6)
Next
Worksheets("Sheet 1").Cells(32, 1).Copy Worksheets("finance").Cells(1, 6)

For i = 1 To 10
Worksheets("Sheet 1").Cells(38, 15 + i).Copy Worksheets("finance").Cells(1 + i, 7)
Next
Worksheets("Sheet 1").Cells(38, 1).Copy Worksheets("finance").Cells(1, 7)

For i = 1 To 10
Worksheets("Sheet 1").Cells(48, 15 + i).Copy Worksheets("finance").Cells(1 + i, 8)
Next
Worksheets("Sheet 1").Cells(48, 1).Copy Worksheets("finance").Cells(1, 8)

For i = 1 To 10
Worksheets("Sheet 1").Cells(61, 15 + i).Copy Worksheets("finance").Cells(1 + i, 9)
Next
Worksheets("Sheet 1").Cells(61, 1).Copy Worksheets("finance").Cells(1, 9)

For i = 1 To 10
Worksheets("Sheet 1").Cells(66, 15 + i).Copy Worksheets("finance").Cells(1 + i, 10)
Next
Worksheets("Sheet 1").Cells(66, 1).Copy Worksheets("finance").Cells(1, 10)

For i = 1 To 10
Worksheets("Sheet 1").Cells(90, 15 + i).Copy Worksheets("finance").Cells(1 + i, 11)
Next
Worksheets("Sheet 1").Cells(90, 1).Copy Worksheets("finance").Cells(1, 11)






End Sub
