Set x = CreateObject("WScript.Shell")
Dim i
i = 0
Do While i < 10
	WScript.Sleep 1000
	x.SendKeys "{CAPSLOCK}"  
	x.SendKeys "{NUMLOCK}"  
	x.SendKeys "I am a Virus"  
	x.SendKeys "{SCROLLLOCK}" 
	i = i + 1
Loop