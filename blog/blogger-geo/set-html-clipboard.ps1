param(
    [Parameter(Mandatory=$true)][string]$FilePath
)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Windows.Forms

$html = Get-Content -Raw -Encoding UTF8 $FilePath
$body = $html -replace '^<h1>.*?</h1>\r?\n', ''
$body = $body.TrimEnd("`r", "`n", " ")

# Escape ALL non-ASCII chars as numeric HTML entities (payload becomes pure ASCII)
$sb = New-Object System.Text.StringBuilder
foreach ($ch in $body.ToCharArray()) {
    if ([int]$ch -gt 126) { [void]$sb.Append('&#').Append([int]$ch).Append(';') }
    else { [void]$sb.Append($ch) }
}
$escaped = $sb.ToString()

$utf8 = New-Object System.Text.UTF8Encoding($false)
function ByteLen([string]$s) { return $utf8.GetByteCount($s) }

$frag = "<!--StartFragment-->" + $escaped + "<!--EndFragment-->"
$doc = "<!DOCTYPE HTML PUBLIC `"-//W3C//DTD HTML 4.0 Transitional//EN`">`r`n<HTML><BODY>`r`n" + $frag + "`r`n</BODY></HTML>"

$hdrTpl = "Version:0.9`r`nStartHTML:{0:D10}`r`nEndHTML:{1:D10}`r`nStartFragment:{2:D10}`r`nEndFragment:{3:D10}`r`n"

$header = [string]::Format($hdrTpl, 0, 0, 0, 0)
$startHtml = $utf8.GetByteCount($header)
$prefix = $doc.Substring(0, $doc.IndexOf($frag))
$startFragment = $startHtml + $utf8.GetByteCount($prefix)
$endFragment = $startFragment + $utf8.GetByteCount($frag)
$endHtml = $startHtml + $utf8.GetByteCount($doc)

$header = [string]::Format($hdrTpl, $startHtml, $endHtml, $startFragment, $endFragment)
$full = $header + $doc

$data = New-Object System.Windows.Forms.DataObject
$data.SetData('HTML Format', $full)   # STRING variant (works in Chromium; all-ASCII payload)
$data.SetData([System.Windows.Forms.DataFormats]::UnicodeText, $body)
[System.Windows.Forms.Clipboard]::SetDataObject($data, $true)

Write-Output ("body_chars=" + $body.Length + " escaped_chars=" + $escaped.Length + " full_len=" + $full.Length)
Write-Output ("startHtml=" + $startHtml + " startFragment=" + $startFragment + " endFragment=" + $endFragment + " endHtml=" + $endHtml)
Write-Output ("head=" + $escaped.Substring(0, 90))
