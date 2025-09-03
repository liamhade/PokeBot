# PokeBot

## Target Bot

I'm having issues creating the Target bot. It seems like Target doesn't let me sign-in using the chromedriver, need to think of some workarounds.

## Creation Notes

Need to be transferred over from the other project.

I had issues on my new Lenovo computer with running scripts from Powershell, so I had to change the execution policy. The following lines show what steps I took:
```
PS C:\Windows\system32> Get-ExecutionPolicy
Restricted
PS C:\Windows\system32> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
...
PS C:\Windows\system32> Get-ExecutionPolicy
RemoteSigned
```