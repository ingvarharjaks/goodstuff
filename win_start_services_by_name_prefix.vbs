strComputer = "."
Set objWMIService = GetObject("winmgmts:" & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colListOfServices = objWMIService.ExecQuery ("Select * from Win32_Service where Name LIKE 'custom_%'")
For Each objService in colListOfServices
    objService.StartService()
Next

