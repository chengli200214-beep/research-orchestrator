param(
  [Parameter(Mandatory = $true)]
  [string]$Repo,

  [ValidateSet("public", "private", "internal")]
  [string]$Visibility = "public",

  [string]$Remote = "origin",

  [string]$CommitMessage = "feat: prepare research-orchestrator for release",

  [switch]$DryRun
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot

function Write-Step {
  param([string]$Message)
  Write-Output "[publish] $Message"
}

function Test-GitIdentity {
  $name = git config user.name 2>$null
  $email = git config user.email 2>$null
  return -not [string]::IsNullOrWhiteSpace($name) -and -not [string]::IsNullOrWhiteSpace($email)
}

function Invoke-OrPrint {
  param([string]$Command)

  if ($DryRun) {
    Write-Output $Command
    return
  }

  Write-Step $Command
  Invoke-Expression $Command
}

Push-Location $repoRoot
try {
  if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "git is not installed."
  }

  if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    throw "GitHub CLI (gh) is not installed."
  }

  $isRepo = $false
  cmd /c "git rev-parse --is-inside-work-tree >nul 2>nul"
  if ($LASTEXITCODE -eq 0) {
    $isRepo = $true
  }

  if (-not $isRepo) {
    Invoke-OrPrint "git init -b main"
  }

  Invoke-OrPrint "git add ."

  $hasCommit = $false
  if ($DryRun) {
    if (-not (Test-GitIdentity)) {
      Write-Output "git config --global user.name `"Your Name`""
      Write-Output "git config --global user.email `"you@example.com`""
    }
    Write-Output "git commit -m `"$CommitMessage`""
    Invoke-OrPrint "gh repo create $Repo --$Visibility --source . --remote $Remote --push"
  } else {
    cmd /c "git rev-parse --verify HEAD >nul 2>nul"
    if ($LASTEXITCODE -eq 0) {
      $hasCommit = $true
    }

    if (-not (Test-GitIdentity)) {
      throw "Git user.name and user.email are not configured. Configure them before publishing."
    }
    git diff --cached --quiet
    if ($LASTEXITCODE -ne 0) {
      Write-Step "git commit -m `"$CommitMessage`""
      git commit -m $CommitMessage
    } elseif (-not $hasCommit) {
      throw "No staged content found for the first commit."
    } else {
      Write-Step "No new staged changes to commit."
    }

    gh auth status *> $null
    if ($LASTEXITCODE -ne 0) {
      throw "gh is not authenticated. Run 'gh auth login' first."
    }

    $hasRemote = $false
    git remote | Select-String -SimpleMatch $Remote *> $null
    if ($LASTEXITCODE -eq 0) {
      $hasRemote = $true
    }

    if (-not $hasRemote) {
      Invoke-OrPrint "gh repo create $Repo --$Visibility --source . --remote $Remote --push"
    } else {
      Invoke-OrPrint "git push -u $Remote main"
    }
  }
}
finally {
  Pop-Location
}
