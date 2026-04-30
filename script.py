import os

os.environ.setdefault("PYMUPDF_MESSAGE", f"path:{os.devnull}")

import argparse
import io
import json
import re
import shutil
import sqlite3
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import fitz  # PyMuPDF
from google import genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()
MODEL_ID = "gemini-2.5-flash"

_client = None
_client_lock = threading.Lock()

def get_client():
    global _client
    if _client is None:
        with _client_lock:
            if _client is None:
                api_key = os.getenv("GEMINI_API_KEY")
                if not api_key:
                    raise ValueError("API 키를 찾을 수 없습니다. .env 파일에 GEMINI_API_KEY를 설정해 주세요.")
                _client = genai.Client(api_key=api_key)
    return _client

ALT_DB = Path.home() / "Library/Application Support/alt/data/database/lecture_notes.db"
ROOT = Path(__file__).parent.resolve()

_mupdf_lock = threading.Lock()

COURSE_CONTEXTS = {
    "CSED101": "이 슬라이드는 프로그래밍과 문제해결 (CSED101) 강의 자료입니다. Python 기초 문법, 변수, 조건문, 반복문, 함수, 재귀 등 프로그래밍 입문 개념이 주로 다뤄집니다.",
    "CSED103": "이 슬라이드는 프로그래밍 입문 (CSED103) 강의 자료입니다. 파이썬 또는 C 언어 기반의 프로그래밍 기초 문법과 알고리즘 사고법이 주로 다뤄집니다.",
    "CSED105": "이 슬라이드는 인공지능 기초 (CSED105) 강의 자료입니다. AI의 역사, 탐색 알고리즘, 기계학습 기초 개념, 신경망 입문 등이 주로 다뤄집니다.",
    "CSED211": "이 슬라이드는 컴퓨터시스템개론 (CSED211) 강의 자료입니다. C 언어, 어셈블리, 프로세서 구조, 메모리 계층, 시스템 호출, 링킹 등 컴퓨터 시스템 전반이 주로 다뤄집니다.",
    "CSED212": "이 슬라이드는 프로그래밍 스튜디오 (CSED212) 강의 자료입니다. 실제 소프트웨어 개발 경험, 협업 도구(Git), 테스트, 코드 품질 등이 주로 다뤄집니다.",
    "CSED226": "이 슬라이드는 데이터분석 입문 (CSED226) 강의 자료입니다. NumPy, pandas, matplotlib, scikit-learn 등의 라이브러리와 머신러닝 기초 개념이 주로 다뤄집니다.",
    "CSED232": "이 슬라이드는 소프트웨어 작성 원리 (CSED232) 강의 자료입니다. C++ 기반의 객체지향 프로그래밍, 클래스, 상속, 다형성, 제네릭, 메모리 관리 등이 주로 다뤄집니다.",
    "CSED233": "이 슬라이드는 데이터구조 (CSED233) 강의 자료입니다. 배열, 연결 리스트, 스택, 큐, 트리, 힙, 해시 테이블, 그래프 등의 자료구조와 시간/공간 복잡도 분석이 주로 다뤄집니다.",
    "CSED261": "이 슬라이드는 전산수학 (CSED261) 강의 자료입니다. 이산수학, 논리, 집합, 수열, 그래프 이론, 조합론, 확률 기초 등 CS에 필요한 수학적 기반이 주로 다뤄집니다.",
    "CSED273": "이 슬라이드는 디지털시스템 설계 (CSED273) 강의 자료입니다. 불 대수, 논리 게이트, 조합 회로, 순차 회로, FSM, Verilog HDL 등 디지털 회로 설계가 주로 다뤄집니다.",
    "CSED312": "이 슬라이드는 운영체제 (CSED312) 강의 자료입니다. 프로세스/스레드, CPU 스케줄링, 동기화, 교착상태, 메모리 관리, 가상 메모리, 파일 시스템 등이 주로 다뤄집니다.",
    "CSED321": "이 슬라이드는 프로그래밍언어 (CSED321) 강의 자료입니다. 언어 패러다임(함수형, 논리형, 객체지향), 타입 시스템, 파싱, 인터프리터/컴파일러 개요 등이 주로 다뤄집니다.",
    "CSED331": "이 슬라이드는 알고리즘 (CSED331) 강의 자료입니다. 분할정복, 탐욕 알고리즘, 동적 프로그래밍, 그래프 알고리즘(BFS/DFS/최단경로/MST), NP-완전성 등이 주로 다뤄집니다.",
    "CSED332": "이 슬라이드는 소프트웨어 설계방법 (CSED332) 강의 자료입니다. 소프트웨어 설계 원칙(SOLID), 디자인 패턴, UML, 리팩터링, 테스트 주도 개발(TDD) 등이 주로 다뤄집니다.",
    "CSED341": "이 슬라이드는 오토마타 및 형식언어 (CSED341) 강의 자료입니다. DFA/NFA, 정규 언어, 문맥 자유 문법, 푸시다운 오토마타, 튜링 기계, 결정 불가능성 등이 주로 다뤄집니다.",
    "CSED342": "이 슬라이드는 인공지능 (CSED342) 강의 자료입니다. 탐색 알고리즘, 게임 트리, 제약 충족, 베이즈 네트워크, 강화학습 기초, 자연어 처리 개요 등이 주로 다뤄집니다.",
    "CSED343": "이 슬라이드는 기계학습을 위한 수학 (CSED343) 강의 자료입니다. 선형대수(행렬, 고유값), 미적분(편미분, 연쇄법칙), 확률/통계, 최적화 이론 등 ML에 필요한 수학이 주로 다뤄집니다.",
    "CSED352": "이 슬라이드는 데이터통신 (CSED352) 강의 자료입니다. OSI/TCP-IP 모델, 신호 인코딩, 오류 제어, MAC 프로토콜, 라우팅 등 네트워크 하위 계층이 주로 다뤄집니다.",
    "CSED353": "이 슬라이드는 컴퓨터네트워크 (CSED353) 강의 자료입니다. TCP/UDP, HTTP, DNS, 소켓 프로그래밍, 혼잡 제어, 보안 기초 등 네트워크 응용 계층이 주로 다뤄집니다.",
    "CSED355": "이 슬라이드는 전산신호처리 (CSED355) 강의 자료입니다. 푸리에 변환, 샘플링, 필터 설계, FFT, 이산 신호 시스템 등이 주로 다뤄집니다.",
    "CSED356": "이 슬라이드는 인간-컴퓨터 상호작용 (CSED356) 강의 자료입니다. HCI 원칙, 사용자 중심 설계, 프로토타이핑, 사용성 평가, 접근성 등이 주로 다뤄집니다.",
    "CSED357": "이 슬라이드는 데이터베이스시스템 (CSED357) 강의 자료입니다. 관계형 모델, SQL, ER 다이어그램, 정규화, 트랜잭션, 인덱스, 쿼리 최적화 등이 주로 다뤄집니다.",
    "CSED401": "이 슬라이드는 컴퓨터와 사회 (CSED401) 강의 자료입니다. AI 윤리, 개인정보, 지식재산권, 사이버 보안 사회적 영향, 기술과 사회의 관계 등이 주로 다뤄집니다.",
    "CSED415": "이 슬라이드는 컴퓨터보안 (CSED415) 강의 자료입니다. 암호화(대칭/비대칭), 네트워크 보안, 웹 취약점(XSS, SQLi), 악성코드, 보안 프로토콜(TLS) 등이 주로 다뤄집니다.",
    "CSED423": "이 슬라이드는 컴파일러 설계 (CSED423) 강의 자료입니다. 어휘 분석, 파싱(LL/LR), 의미 분석, 중간 코드 생성, 최적화, 코드 생성 등이 주로 다뤄집니다.",
    "CSED426": "이 슬라이드는 빅데이터 (CSED426) 강의 자료입니다. Hadoop, Spark, MapReduce, 분산 파일시스템, 스트림 처리, NoSQL 데이터베이스 등이 주로 다뤄집니다.",
    "CSED433": "이 슬라이드는 전산논리 (CSED433) 강의 자료입니다. 명제논리, 1차 논리, SAT 솔버, 자동 정리 증명, 논리 프로그래밍(Prolog) 등이 주로 다뤄집니다.",
    "CSED441": "이 슬라이드는 컴퓨터비전 개론 (CSED441) 강의 자료입니다. 이미지 처리, 에지 검출, 특징 추출, CNN 기반 인식, 객체 탐지, 세그멘테이션 등이 주로 다뤄집니다.",
    "CSED451": "이 슬라이드는 컴퓨터그래픽스 (CSED451) 강의 자료입니다. 렌더링 파이프라인, 래스터화, 광선 추적, 변환 행렬, 셰이더, OpenGL/WebGL 등이 주로 다뤄집니다.",
}


# ── Alt DB reading ─────────────────────────────────────────────────────────────

def resolve_folder_path(folder_id, folders: dict) -> Path:
    if folder_id is None or folder_id not in folders:
        return Path("기타")
    parts = []
    current_id = folder_id
    while current_id is not None:
        folder = folders[current_id]
        parts.append(folder["name"])
        current_id = folder["parent_id"]
    return Path(*reversed(parts))


def read_alt_notes() -> list[dict]:
    if not ALT_DB.exists():
        raise FileNotFoundError(f"Alt DB를 찾을 수 없습니다: {ALT_DB}\nAlt(altalt.io)가 설치되어 있는지 확인하세요.")

    try:
        conn = sqlite3.connect(f"file:{ALT_DB}?mode=ro", uri=True)
    except sqlite3.OperationalError as e:
        raise RuntimeError(f"Alt DB 연결 실패: {e}") from e

    with conn:
        conn.row_factory = sqlite3.Row

        folders = {}
        for row in conn.execute("SELECT id, name, parent_id FROM folders"):
            folders[row["id"]] = {"name": row["name"], "parent_id": row["parent_id"]}

        notes = []
        for note_row in conn.execute(
            "SELECT id, title, folder_id, lecture_date FROM lecture_notes ORDER BY id"
        ):
            note_id = note_row["id"]

            slides_path = None
            transcript_text = None

            for comp in conn.execute(
                "SELECT nc.component_type, nc.content_text, fm.file_path "
                "FROM note_components nc "
                "LEFT JOIN file_metadata fm ON nc.file_inode = fm.inode "
                "WHERE nc.note_id = ? ORDER BY nc.display_order",
                (note_id,),
            ):
                ctype = comp["component_type"]
                if ctype == "slides" and slides_path is None:
                    slides_path = comp["file_path"]
                elif ctype == "transcript" and transcript_text is None:
                    transcript_text = comp["content_text"]

            if slides_path is None:
                continue

            folder_path = resolve_folder_path(note_row["folder_id"], folders)
            notes.append({
                "id": note_id,
                "title": note_row["title"],
                "date": note_row["lecture_date"],
                "folder_path": folder_path,
                "slide_path": Path(slides_path),
                "transcript": transcript_text,
            })

    return notes


# ── Transcript parsing & alignment ────────────────────────────────────────────

def parse_transcript_segments(content_text) -> list[dict]:
    if not isinstance(content_text, str):
        return []
    try:
        chunks = json.loads(content_text)
    except (json.JSONDecodeError, TypeError):
        return []
    segments = []
    for chunk in chunks:
        for seg in chunk.get("segments", []):
            try:
                text = seg.get("text", "").strip()
                if text:
                    segments.append({"start": seg["start"], "end": seg["end"], "text": text})
            except (KeyError, TypeError):
                continue
    return segments


def align_transcript_to_slides(segments: list[dict], num_pages: int) -> list[str]:
    if not segments or num_pages == 0:
        return [""] * num_pages

    total_duration = max(s["end"] for s in segments)
    if total_duration == 0:
        return [""] * num_pages

    time_per_slide = total_duration / num_pages
    slide_texts = []
    for page in range(1, num_pages + 1):
        start_ms = (page - 1) * time_per_slide
        end_ms = page * time_per_slide
        is_last = page == num_pages
        page_segs = [
            s["text"] for s in segments
            if start_ms <= s["start"] and (is_last or s["start"] < end_ms)
        ]
        slide_texts.append(" ".join(page_segs))
    return slide_texts


# ── Prompt building ────────────────────────────────────────────────────────────

def get_course_context(folder_path: Path) -> str:
    for part in folder_path.parts:
        if part.upper() in COURSE_CONTEXTS:
            return COURSE_CONTEXTS[part.upper()]
    return "이 슬라이드는 대학교 전공 강의 자료입니다."


def build_prompt(course_context: str, slide_transcript: str) -> str:
    has_transcript = bool(slide_transcript.strip())
    transcript_section = (
        f"\n[강의 음성 전사 — 이 슬라이드 구간]\n{slide_transcript}\n"
        if has_transcript else ""
    )
    lecture_note_item = (
        "- **강의 내용**: 교수님이 음성으로 강조하신 내용이나 추가 설명을 포함\n"
        if has_transcript else ""
    )
    slide_ref = "와 위의 강의 음성 전사" if has_transcript else ""

    return f"""당신은 POSTECH 전공 튜터입니다.
{course_context}
{transcript_section}
첨부된 슬라이드 이미지{slide_ref}를 분석하여 다음 형식으로 마크다운 노트를 작성해 주세요:
- **핵심 개념**: 슬라이드의 주요 개념을 명확하게 설명
- **코드/수식 해설**: 코드는 코드 블록(```)을, 수식은 LaTeX($ 또는 $$)을 사용
- **구체적 예시**: 실제 동작 예시나 실생활 비유를 통해 이해를 도움
{lecture_note_item}- **시험 포인트**: 시험에 나올 만한 핵심 내용을 ⭐ 표시와 함께 강조

**[수식 작성 규칙 — 반드시 준수]**
1. 수식은 항상 `$...$`(인라인) 또는 `$$...$$`(블록)으로만 표기하세요.
2. 백틱(`) 코드 스팬 안에 수식 기호를 절대 넣지 마세요.
3. 수식을 코드 블록(```) 안에 넣지 마세요.
4. 수학 변수·기호는 `$...$` 수식으로 표기하세요.

불필요한 인사말 없이 바로 본론만 작성해 주세요."""


# ── Slide processing ───────────────────────────────────────────────────────────

def _parse_md_sections(md_text: str) -> tuple[str, dict[int, str]]:
    parts = re.split(r"\n(?=## Slide \d+\n)", md_text)
    header = parts[0] + "\n"
    sections: dict[int, str] = {}
    for part in parts[1:]:
        m = re.match(r"## Slide (\d+)\n", part)
        if m:
            sections[int(m.group(1))] = part
    return header, sections


def find_failed_slides(output_md: Path) -> set[int]:
    if not output_md.exists():
        return set()
    _, sections = _parse_md_sections(output_md.read_text(encoding="utf-8"))
    return {
        num for num, text in sections.items()
        if "*오류 발생으로 해설을 생성하지 못했습니다.*" in text
        or "*빈 슬라이드이거나 응답을 생성할 수 없었습니다.*" in text
    }


def _extract_page_warning(page_num: int) -> str | None:
    warnings_text = fitz.TOOLS.mupdf_warnings().strip()
    return f"[페이지 {page_num}] {warnings_text}" if warnings_text else None


def _process_slide(
    page: fitz.Page,
    prompt: str,
    page_num: int,
    delay: float,
    warning_logs: list[str] | None = None,
) -> str:
    try:
        with _mupdf_lock:
            fitz.TOOLS.reset_mupdf_warnings()
            pix = page.get_pixmap(dpi=150)
            warning = _extract_page_warning(page_num)

        if warning and warning_logs is not None:
            warning_logs.append(warning)

        img = Image.open(io.BytesIO(pix.tobytes("png")))
        response = get_client().models.generate_content(model=MODEL_ID, contents=[prompt, img])

        if response.text:
            content = response.text
        else:
            finish_reason = "unknown"
            if response.candidates:
                finish_reason = str(response.candidates[0].finish_reason)
            print(f"  [경고] 슬라이드 {page_num}: 빈 응답 (finish_reason={finish_reason})")
            content = "*빈 슬라이드이거나 응답을 생성할 수 없었습니다.*"

    except Exception as e:
        print(f"  [오류] 슬라이드 {page_num}: {e}")
        content = "*오류 발생으로 해설을 생성하지 못했습니다.*"
    finally:
        time.sleep(delay)

    return f"## Slide {page_num}\n\n{content}\n\n---\n\n"


def explain_pdf(
    note: dict,
    output_md: Path,
    delay: float = 2.0,
    target_slides: set[int] | None = None,
    save_warning_log: bool = False,
    label: str = "",
):
    pdf_path = note["slide_path"]
    tag = f"[{label or pdf_path.name}]"
    print(f"\n{tag} 분석을 시작합니다... ({pdf_path.name})")

    has_transcript = bool(note.get("transcript"))
    if has_transcript:
        print(f"{tag} 음성 전사 데이터 포함 ({len(note['transcript'])} chars)")
    else:
        print(f"{tag} 음성 전사 없음 — 슬라이드만으로 생성합니다.")

    warning_logs: list[str] = []
    course_context = get_course_context(note["folder_path"])

    segments = parse_transcript_segments(note["transcript"]) if has_transcript else []

    with fitz.open(str(pdf_path)) as doc:
        num_pages = len(doc)
        slide_transcripts = align_transcript_to_slides(segments, num_pages) if segments else [""] * num_pages

        if target_slides:
            if not output_md.exists():
                print(f"{tag} [오류] '{output_md}'이 없습니다. 먼저 전체 처리를 실행하세요.")
                return

            print(f"{tag} 슬라이드 {sorted(target_slides)} 재처리 중...")
            header, sections = _parse_md_sections(output_md.read_text(encoding="utf-8"))

            for num in sorted(target_slides):
                if num < 1 or num > num_pages:
                    print(f"{tag} [경고] 슬라이드 {num}은 범위를 벗어납니다 (총 {num_pages}장). 건너뜁니다.")
                    continue

                print(f"{tag} -> 슬라이드 {num}/{num_pages} 재처리 중...")
                prompt = build_prompt(course_context, slide_transcripts[num - 1])
                sections[num] = _process_slide(doc.load_page(num - 1), prompt, num, delay, warning_logs)

            full_notes = header + "".join(sections[n] for n in sorted(sections))
        else:
            course_code = next(
                (p.upper() for p in note["folder_path"].parts if p.upper() in COURSE_CONTEXTS),
                note["folder_path"].parts[0] if note["folder_path"].parts else "강의",
            )
            transcript_label = " (음성 전사 포함)" if has_transcript else ""
            full_notes = f"# {course_code} - {pdf_path.stem} 상세 해설 노트{transcript_label}\n\n"
            full_notes += f"> 이 노트는 Gemini 2.5 Flash를 이용해 자동 생성되었습니다."
            if has_transcript:
                full_notes += " Alt(altalt.io) 음성 전사 데이터를 함께 활용했습니다."
            full_notes += "\n\n---\n\n"

            for page_num in range(num_pages):
                print(f"{tag} -> 슬라이드 {page_num + 1}/{num_pages} 처리 중...")
                prompt = build_prompt(course_context, slide_transcripts[page_num])
                full_notes += _process_slide(doc.load_page(page_num), prompt, page_num + 1, delay, warning_logs)

    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_md.write_text(full_notes, encoding="utf-8")
    print(f"{tag} 완료 -> [{output_md}]")

    if save_warning_log and warning_logs:
        warning_path = output_md.with_suffix(".mupdf_warnings.log")
        warning_path.write_text("\n\n".join(warning_logs), encoding="utf-8")
        print(f"{tag} MuPDF 경고 로그 저장 -> [{warning_path}]")


# ── Output path resolution ─────────────────────────────────────────────────────

def get_output_paths(note: dict, output_root: Path = ROOT) -> tuple[Path, Path]:
    """(output_pdf_path, output_md_path) 반환."""
    stem = note["slide_path"].stem
    out_dir = output_root / note["folder_path"]
    return out_dir / f"{stem}.pdf", out_dir / f"{stem}.md"


def ensure_pdf_copied(note: dict, output_pdf: Path):
    """슬라이드 PDF를 출력 디렉토리에 복사합니다 (이미 있으면 스킵)."""
    if not output_pdf.exists():
        output_pdf.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(note["slide_path"], output_pdf)
        print(f"  PDF 복사: {output_pdf.relative_to(ROOT)}")


# ── CLI ────────────────────────────────────────────────────────────────────────

def configure_pymupdf(show_messages: bool = False):
    fitz.TOOLS.mupdf_display_errors(show_messages)
    fitz.TOOLS.mupdf_display_warnings(show_messages)


def cmd_list(notes: list[dict]):
    print(f"\n{'ID':>3}  {'날짜':<12}  {'폴더':<20}  {'제목':<40}  {'전사':>4}  {'노트':>4}")
    print("-" * 100)
    for note in notes:
        _, output_md = get_output_paths(note)
        has_transcript = "✓" if note["transcript"] else "-"
        has_notes = "✓" if output_md.exists() else "-"
        folder_str = str(note["folder_path"])
        print(f"{note['id']:>3}  {note['date']:<12}  {folder_str:<20}  {note['title'][:40]:<40}  {has_transcript:>4}  {has_notes:>4}")
    print(f"\n총 {len(notes)}개 노트  (전사: 음성 전사 있음, 노트: 이미 생성됨)")


def main():
    parser = argparse.ArgumentParser(
        description="Alt(altalt.io) 음성 노트 + 강의 슬라이드를 Gemini AI로 페이지별 해설 노트 생성",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
사용 예시:
  python script.py --list                        # 처리 가능한 노트 목록
  python script.py --note 1                      # 노트 ID 1 처리
  python script.py --note 1,2,3                  # 여러 노트 처리
  python script.py --all                         # 모든 노트 처리
  python script.py --note 1 --retry              # 오류 슬라이드 재처리
  python script.py --note 1 --slides 3,7         # 특정 슬라이드만 처리
  python script.py --all -j 2                    # 병렬 처리
        """,
    )
    parser.add_argument("--list", action="store_true", help="처리 가능한 Alt 노트 목록 출력")
    parser.add_argument("--note", help="처리할 노트 ID (쉼표 구분, 예: 1,2,3)")
    parser.add_argument("--all", action="store_true", help="슬라이드가 있는 모든 노트 처리")
    parser.add_argument("--delay", type=float, default=2.0, help="슬라이드 처리 간 대기 시간(초), 기본값: 2.0")
    parser.add_argument("--retry", action="store_true", help="오류가 발생한 슬라이드만 재처리")
    parser.add_argument("--slides", help="재처리할 슬라이드 번호 (쉼표 구분, 예: 3,7,12)")
    parser.add_argument("--workers", "-j", type=int, default=1, metavar="N", help="병렬 처리 워커 수 (기본값: 1)")
    parser.add_argument("--show-mupdf-messages", action="store_true", help="MuPDF 내부 경고를 콘솔에 표시")
    parser.add_argument("--save-warning-log", action="store_true", help="MuPDF 경고를 .mupdf_warnings.log 파일로 저장")

    args = parser.parse_args()
    configure_pymupdf(show_messages=args.show_mupdf_messages)

    notes = read_alt_notes()

    if args.list or (not args.note and not args.all):
        cmd_list(notes)
        return

    # Select notes to process
    notes_by_id = {n["id"]: n for n in notes}
    if args.all:
        selected = notes
    else:
        try:
            ids = [int(x.strip()) for x in args.note.split(",")]
        except ValueError:
            print("[오류] --note 인자는 쉼표로 구분된 숫자여야 합니다. 예: 1,2,3")
            sys.exit(1)
        selected = []
        for nid in ids:
            if nid not in notes_by_id:
                print(f"[경고] 노트 ID {nid}를 찾을 수 없습니다. 건너뜁니다.")
            else:
                selected.append(notes_by_id[nid])

    if not selected:
        print("처리할 노트가 없습니다.")
        sys.exit(1)

    manual_slides: set[int] = set()
    if args.slides:
        try:
            manual_slides = {int(s.strip()) for s in args.slides.split(",")}
        except ValueError:
            print("[오류] --slides 인자는 쉼표로 구분된 숫자여야 합니다. 예: 3,7,12")
            sys.exit(1)

    workers = min(args.workers, len(selected))
    print(f"총 {len(selected)}개 노트를 처리합니다." + (f" (워커 {workers}개 병렬)" if workers > 1 else ""))

    def process_one(idx_note):
        idx, note = idx_note
        label = f"{idx}/{len(selected)} {note['slide_path'].stem}"
        output_pdf, output_md = get_output_paths(note)

        ensure_pdf_copied(note, output_pdf)

        target_slides: set[int] | None = None
        if args.retry or manual_slides:
            target_slides = manual_slides.copy()
            if args.retry:
                failed = find_failed_slides(output_md)
                if failed:
                    print(f"[{label}] 오류 슬라이드 감지: {sorted(failed)}")
                target_slides |= failed
            if not target_slides:
                print(f"[{label}] 재처리할 슬라이드 없음, 건너뜁니다.")
                return

        explain_pdf(
            note=note,
            output_md=output_md,
            delay=args.delay,
            target_slides=target_slides,
            save_warning_log=args.save_warning_log,
            label=label,
        )

    if workers <= 1:
        for item in enumerate(selected, 1):
            process_one(item)
    else:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(process_one, item): item for item in enumerate(selected, 1)}
            for future in as_completed(futures):
                exc = future.exception()
                if exc:
                    _, note = futures[future]
                    print(f"[오류] {note['title']}: {exc}")

    print("\n모든 작업이 완료되었습니다!")


if __name__ == "__main__":
    main()
