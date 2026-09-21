#!/usr/bin/env python3
"""
キーワードツールのエクスポートを 02_keywords.csv にマージし、需要規模を検証する。

使い方:
    python3 tools/merge_volume.py <エクスポートファイル> [--ctr 0.30]

対応フォーマット:
  - Googleキーワードプランナー CSV（UTF-16 TSV / UTF-8 CSV の両方）
  - ラッコキーワード / Ubersuggest / Ahrefs 等の CSV
  （「キーワード」列と「ボリューム」列を自動検出。見つからなければ列名を聞く）

出力:
  - research/02_keywords_actual.csv  実ボリュームを反映した新CSV
  - 標準出力に「需要規模フィジビリティ判定」
"""
import csv, sys, io, re, os

BASE = os.path.join(os.path.dirname(__file__), "..")
SRC  = os.path.join(BASE, "research", "02_keywords.csv")
DST  = os.path.join(BASE, "research", "02_keywords_actual.csv")

KW_COL_HINTS  = ["キーワード", "keyword", "検索キーワード", "query"]
VOL_COL_HINTS = ["月間平均検索ボリューム", "avg. monthly searches", "avg monthly searches",
                 "検索ボリューム", "volume", "search volume", "月間検索数", "searches"]


def read_any(path):
    """UTF-16/UTF-8、TSV/CSV を判別して行のリストを返す。"""
    raw = open(path, "rb").read()
    if raw[:2] in (b"\xff\xfe", b"\xfe\xff"):
        encodings = ("utf-16",)
    elif raw[:3] == b"\xef\xbb\xbf":
        encodings = ("utf-8-sig",)
    else:
        encodings = ("utf-8", "cp932")
    for enc in encodings:
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        sys.exit(f"文字コードを判別できません: {path}")

    lines = [l for l in text.splitlines() if l.strip()]
    # キーワードプランナーは先頭数行がメタ情報。「2列以上あり、かつキーワード列を含む」行をヘッダとみなす
    start = None
    for i, l in enumerate(lines[:15]):
        delim = "\t" if l.count("\t") > l.count(",") else ","
        cells = [c.strip().strip('"') for c in l.split(delim)]
        if len(cells) < 2:
            continue
        if any(any(h.lower() == c.lower() or h.lower() in c.lower() for h in KW_COL_HINTS) for c in cells):
            start = i
            break
    if start is None:
        sys.exit("ヘッダ行（キーワード列を含む行）が見つかりません。ファイル形式を確認してください。")
    body = "\n".join(lines[start:])
    delim = "\t" if body.count("\t") > body.count(",") else ","
    return list(csv.DictReader(io.StringIO(body), delimiter=delim))


def find_col(fieldnames, hints):
    for f in fieldnames:
        if f and any(h.lower() in f.lower() for h in hints):
            return f
    return None


def parse_vol(v):
    """'1,000' '100〜1000' '1K - 10K' 等を数値化（レンジは下限を採用＝保守的）。"""
    if v is None:
        return None
    s = str(v).strip().replace(",", "").replace("，", "")
    if not s or s in ("-", "—", "–"):
        return None
    s = re.sub(r"(\d)\s*[kK]\b", lambda m: m.group(1) + "000", s)
    nums = re.findall(r"\d+", s)
    if not nums:
        return None
    return int(nums[0])   # レンジ表記は下限を採用


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    export = sys.argv[1]
    ctr = 0.30
    if "--ctr" in sys.argv:
        ctr = float(sys.argv[sys.argv.index("--ctr") + 1])

    ex = read_any(export)
    if not ex:
        sys.exit("エクスポートファイルに行がありません。")
    kwc = find_col(ex[0].keys(), KW_COL_HINTS)
    volc = find_col(ex[0].keys(), VOL_COL_HINTS)
    if not kwc or not volc:
        print("列を自動検出できませんでした。検出された列名:", list(ex[0].keys()))
        sys.exit("→ KW_COL_HINTS / VOL_COL_HINTS に列名を追記してください。")
    print(f"検出: キーワード列='{kwc}' / ボリューム列='{volc}'  ({len(ex)}行)")

    vol = {}
    for r in ex:
        k = (r.get(kwc) or "").strip()
        v = parse_vol(r.get(volc))
        if k and v is not None:
            vol[k] = v

    rows = list(csv.DictReader(open(SRC)))
    hit = miss = 0
    for r in rows:
        k = r["keyword"].strip()
        if k in vol:
            r["est_volume"] = str(vol[k])
            r["note"] = "実測/" + r["note"]
            hit += 1
        else:
            r["note"] = "未取得(推定のまま)/" + r["note"]
            miss += 1

    with open(DST, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)

    print(f"\nマージ完了 → {DST}")
    print(f"  実測で上書き: {hit}語 / 未取得: {miss}語")

    # ---- 需要規模フィジビリティ判定 ----
    def vnum(r):
        try:
            return int(str(r["est_volume"]).replace(",", ""))
        except (ValueError, KeyError):
            return 0

    measured = [r for r in rows if r["note"].startswith("実測/")]
    if not measured:
        print("\n実測データが1件もマージされていません。キーワードの表記ゆれを確認してください。")
        return

    total = sum(vnum(r) for r in measured)
    top50 = [r for r in measured if r["priority_rank"].strip().isdigit()]
    top50_vol = sum(vnum(r) for r in top50)

    print("\n" + "=" * 62)
    print("  需要規模フィジビリティ判定")
    print("=" * 62)
    print(f"  実測できた {len(measured)}語 の合計月間検索ボリューム : {total:>10,}")
    print(f"  うち優先{len(top50)}語の合計                      : {top50_vol:>10,}")
    print(f"\n  仮定: 対象KWで平均CTR {ctr:.0%}（上位表示できた場合）")
    print(f"  → 優先{len(top50)}語だけで取れるセッション     : {top50_vol*ctr:>10,.0f} /月")
    print(f"  → 全{len(measured)}語を取り切った場合           : {total*ctr:>10,.0f} /月")
    target = 32000
    print(f"\n  目標セッション（docs/05_asp_portfolio.md）: {target:,} /月")
    ach = total * ctr
    if ach >= target:
        print(f"  ✅ 判定: 到達可能。全KW取り切りで目標の {ach/target*100:.0f}%")
    elif ach >= target * 0.5:
        print(f"  ⚠️  判定: 到達には不足。全取りで目標の {ach/target*100:.0f}%")
        print("     → クラスタの拡張（隣接テーマ）か、収益単価の引き上げが必要")
    else:
        print(f"  🔴 判定: 規模が足りない。全取りでも目標の {ach/target*100:.0f}%")
        print("     → 戦略の前提を見直すこと。以下のいずれかを選ぶ:")
        print("        (a) 対象クラスタを広げる（C6資格/C9異業種/C7地域）")
        print("        (b) 高単価案件の比率を上げ、必要セッションを下げる")
        print("        (c) 目標額または到達期間を見直す")

    print("\n  クラスタ別の実測ボリューム（降順）:")
    agg = {}
    for r in measured:
        agg.setdefault(r["cluster"], [0, 0])
        agg[r["cluster"]][0] += vnum(r)
        agg[r["cluster"]][1] += 1
    for c, (v, n) in sorted(agg.items(), key=lambda x: -x[1][0]):
        print(f"    {c:<34} {v:>9,}  ({n}語)")

    print("\n  実測で推定から大きくズレた語 トップ20（要注目）:")
    src = {r["keyword"]: r for r in csv.DictReader(open(SRC))}
    diffs = []
    for r in measured:
        try:
            old = int(str(src[r["keyword"]]["est_volume"]).replace(",", ""))
        except (ValueError, KeyError):
            continue
        new = vnum(r)
        if old:
            diffs.append((new / old, r["keyword"], old, new, r["priority_rank"]))
    for ratio, k, old, new, p in sorted(diffs, key=lambda x: -abs(x[0] - 1))[:20]:
        mark = "↑" if ratio > 1 else "↓"
        pr = f"優先{p}" if str(p).strip().isdigit() else "—"
        print(f"    {mark} {k:<34} 推定{old:>6,} → 実測{new:>7,}  ({pr})")


if __name__ == "__main__":
    main()
