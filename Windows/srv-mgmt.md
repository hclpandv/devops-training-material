[<<Back](index.md)
## Services

```powershell
# List all services
Get-Service
# Only running
Get-Service | where {$_.status -eq "Running"}
```
