# 📒 altToNotes

[Alt(altalt.io)](https://altalt.io) 음성 노트, Alt 공유 링크, 일반 PDF를 Gemini 2.5 Flash로 페이지별 자동 해설하고, PDF와 노트를 나란히 볼 수 있는 뷰어입니다.

> **autonotes**([junnnnnw00/autonotes](https://github.com/junnnnnw00/autonotes))를 기반으로, Alt의 강의 음성 전사 데이터를 함께 활용하여 더 풍부한 해설 노트를 생성합니다.

> **🌐 웹 뷰어**: [altToNotes](https://github.com/junnnnnw00/altToNotes)

---

## 특징

| 기능 | 설명 |
|---|---|
| 🎙️ 음성 전사 활용 | Alt 로컬 DB 또는 공유 링크의 전사가 있으면 슬라이드와 시간 비례로 매핑 |
| 🔗 공유 링크 입력 | macOS/Alt 설치 없이 `https://altalt.io/note/...` 링크만으로 처리 |
| 📥 일반 PDF 가져오기 | 전사·요약이 없어도 로컬 PDF 또는 PDF URL에서 바로 생성 |
| 📄 페이지별 해설 | 슬라이드 이미지 + 제공된 강의 맥락(있다면) → Gemini 2.5 Flash 해설 |
| 🔄 자동 동기화 | Alt DB에서 직접 읽어 별도 export 불필요 |
| 🌐 GitHub Pages | `build_static.py` 한 번으로 정적 사이트 배포 |
| ⌨️ 단축키 | `[`/`]` 슬라이드 이동, `t` 목차, `Ctrl+\` 사이드바 |

---

## 1. 설치

```bash
git clone https://github.com/junnnnnw00/altToNotes.git
cd altToNotes
pip install -r requirements.txt
```

`.env` 파일을 생성하고 [Google AI Studio](https://aistudio.google.com/)에서 발급한 API 키를 입력합니다.

```
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

입력 방식은 3가지입니다.

- **Alt DB 모드**: macOS에 Alt(altalt.io)가 설치되어 있고 로컬 DB를 읽을 수 있을 때
- **공유 링크 모드**: Alt 공유 링크(`https://altalt.io/note/...`)만 있을 때
- **일반 PDF 모드**: Alt와 무관한 PDF 파일 또는 PDF URL만 있을 때

---

## 2. Alt DB 모드: 노트 목록 확인

```bash
python script.py --list
```

Alt DB에서 슬라이드가 연결된 노트를 자동으로 읽어 목록을 출력합니다.

```
 ID  날짜          폴더                  제목                                      전사  노트
----------------------------------------------------------------------------------------------------
  1  2026-04-22    CSED226/기말          1. Univariate Data Analysis Plotting...      ✓     -
  4  2026-04-23    CSED233/기말          1. B Tree                                    ✓     -
  ...
```

---

## 3. 노트 생성

### 3-1. Alt DB 모드

```bash
# 특정 노트 ID 처리
python script.py --note 1

# 여러 노트 처리
python script.py --note 1,4,5

# 모든 노트 처리
python script.py --all

# 2개 워커로 병렬 처리
python script.py --all -j 2

# 오류 슬라이드만 재처리
python script.py --note 1 --retry

# 특정 슬라이드만 재처리
python script.py --note 1 --slides 3,7,12
```

### 3-2. Alt 공유 링크 모드

```bash
# macOS / Alt 설치 없이 공유 링크로 바로 생성
python script.py --share-link https://altalt.io/note/9506f3f8-f7bb-4a85-bb88-fc51dc12c9a5

# 출력 폴더 지정
python script.py \
  --share-link https://altalt.io/note/9506f3f8-f7bb-4a85-bb88-fc51dc12c9a5 \
  --output-folder CSED232/기말
```

공유 페이지에 전사가 있으면 함께 활용하고, 없어도 슬라이드만으로 생성합니다.

### 3-3. 일반 PDF 모드

```bash
# 로컬 PDF 처리
python script.py --pdf ./slides.pdf

# 외부 PDF URL 처리
python script.py --pdf https://example.com/slides.pdf

# 출력 폴더 지정
python script.py --pdf ./slides.pdf --output-folder Imported/OS
```

일반 PDF는 Alt 전사나 요약이 없어도 그대로 노트를 생성합니다.

생성에 사용된 PDF는 출력 폴더에 복사되며, 같은 위치에 `.md` 노트 파일이 생성됩니다.

### 옵션

| 옵션 | 기본값 | 설명 |
|---|---|---|
| `--share-link URL` | — | Alt 공유 링크 직접 처리 (반복 사용 가능) |
| `--pdf PATH_OR_URL` | — | 일반 PDF 파일 또는 PDF URL 직접 처리 (반복 사용 가능) |
| `--output-folder PATH` | 입력별 기본 경로 | share-link/pdf 입력의 출력 폴더 지정 |
| `--delay N` | `2.0` | 슬라이드 처리 간 대기 시간(초) — Rate Limit 방지 |
| `-j N`, `--workers N` | `1` | 노트 단위 병렬 처리 워커 수 |
| `--retry` | — | 오류가 발생한 슬라이드만 재처리 |
| `--slides 3,7,12` | — | 특정 슬라이드 번호만 재처리 |
| `--save-warning-log` | — | MuPDF 경고를 `.mupdf_warnings.log`에 저장 |

---

## 4. 로컬 뷰어

```bash
python viewer.py
```

브라우저가 자동으로 열리고 PDF와 노트를 나란히 볼 수 있습니다.

### 단축키

| 키 | 동작 |
|---|---|
| `[` / `]` | 이전 / 다음 슬라이드 |
| `Ctrl + ←` / `→` | 이전 / 다음 슬라이드 (PDF 동기화) |
| `t` | 목차(TOC) 열기/닫기 |
| `p` | 인쇄 / PDF 저장 |
| `Ctrl + \` | 사이드바 접기/펼치기 |

---

## 5. 배포 (GitHub Pages)

```bash
python build_static.py
git add index.html pdfview.html files.json
git commit -m "chore: rebuild static site"
git push
```

---

## 출력 구조

```
{과목코드}/{하위폴더}/
  {슬라이드명}.pdf    ← Alt / 공유 링크 / 원본 PDF에서 복사
  {슬라이드명}.md     ← Gemini로 생성된 해설 노트
```

예시:
```
CSED233/기말/
  11_BTree.pdf
  11_BTree.md          ← B-Tree 강의 해설 (음성 전사 포함)
  12_Dictionary_hashing.pdf
  12_Dictionary_hashing.md
```

---

## 음성 전사 정렬 방식

Alt 로컬 DB 또는 공유 링크에 전사 데이터가 있으면, 밀리초 단위 타임스탬프를 이용해 전체 녹음 시간을 슬라이드 수로 나누고 각 슬라이드에 해당 구간의 음성을 비례 배분합니다. 교수님이 강조한 내용, 추가 설명, 예시 등이 해설 노트에 자동으로 포함됩니다.
