#!/bin/zsh
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_DIR"

if [[ -n "$(git status --porcelain)" ]]; then
  echo "로컬 변경 사항이 있어 자동 업데이트를 중단합니다."
  echo "먼저 커밋하거나 정리한 뒤 다시 실행하세요."
  echo
  git status --short
  exit 1
fi

git fetch origin
git pull --ff-only origin main
/usr/bin/python3 build_viewer_app.py

echo
echo "업데이트가 완료되었습니다."
echo "앱은 dist/AltToNotes Viewer.app 에 있습니다."
