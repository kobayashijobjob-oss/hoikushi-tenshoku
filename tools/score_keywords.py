#!/usr/bin/env python3
"""
docs/07_kw_selection_doctrine.md の優先度スコアを全キーワードに適用して並べ直す。

使い方:
    python3 tools/score_keywords.py              # 実測CSVがあれば自動で使う
    python3 tools/score_keywords.py --top 80     # 上位N件を表示（既定50）
    python3 tools/score_keywords.py --cluster C11  # クラスタで絞る

出力:
    research/02_keywords_scored.csv  （score列・new_rank列を追加）
"""
import csv, math, os, sys

BASE = os.path.join(os.path.dirname(__file__), "..")
ACTUAL = os.path.join(BASE, "research", "02_keywords_actual.csv")
EST    = os.path.join(BASE, "research", "02_keywords.csv")
OUT    = os.path.join(BASE, "research", "02_keywords_scored.csv")

CV_W   = {"A": 3.0, "B": 1.5, "C": 0.7}
DIFF_W = {"low": 3.0, "mid": 1.5, "high": 0.5}
# AI Overviewに食われる度合い。測量メディアの実測に合わせ4倍の開きを持たせる
# （実例: 全表示回数の38%を占める8位のKWでクリック0件）
AI_W   = {"低": 1.0, "中": 0.6, "高": 0.25}   # ai_risk列: 低リスク=食われない

# 独自性（園長＝採用決裁者の視点が乗るか）
UNIQUE_CLUSTER = "C11"                      # 中核クラスタは定義上すべて乗る
UNIQUE_MARKERS = ["見分け方", "特徴", "選び方", "調べ方", "見方", "チェック",
                  "園長", "採用", "手数料", "紹介会社", "直接応募", "本音", "理由"]


def vol(r):
    try:
        return int(str(r["est_volume"]).replace(",", "").split("〜")[0])
    except (ValueError, KeyError):
        return 0


def uniqueness(r):
    if r["cluster"].startswith(UNIQUE_CLUSTER):
        return 2.0
    if any(m in r["keyword"] for m in UNIQUE_MARKERS):
        return 1.5
    return 1.0


def score(r):
    v = math.log10(vol(r) + 10)
    cv = CV_W.get(r["cv_distance"].strip().upper(), 1.0)
    df = DIFF_W.get(r["difficulty"].strip().lower(), 1.0)
    ai = AI_W.get(r["ai_risk"].strip(), 1.0)
    return v * cv * df * ai * uniqueness(r)


def main():
    top = 50
    if "--top" in sys.argv:
        top = int(sys.argv[sys.argv.index("--top") + 1])
    only = None
    if "--cluster" in sys.argv:
        only = sys.argv[sys.argv.index("--cluster") + 1]

    src = ACTUAL if os.path.exists(ACTUAL) else EST
    measured = src == ACTUAL
    rows = list(csv.DictReader(open(src)))

    print(f"入力: {os.path.relpath(src, BASE)}"
          f"  {'（実測ボリューム）' if measured else '（⚠️ 推定ボリューム。実測前の暫定順位）'}")

    for r in rows:
        r["score"] = f"{score(r):.2f}"
        r["uniqueness"] = f"{uniqueness(r):.1f}"
    # 同点は「ボリューム大 → 語順」で決定的に並べる（推定値が粗いと同点が多発するため）
    rows.sort(key=lambda r: (-float(r["score"]), -vol(r), r["keyword"]))
    for i, r in enumerate(rows, 1):
        r["new_rank"] = i

    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"出力: {os.path.relpath(OUT, BASE)}\n")

    view = [r for r in rows if not only or r["cluster"].startswith(only)]
    print(f"{'新':>3} {'旧':>4}  {'score':>6} {'vol':>7} {'CV':>2} {'難易':>4} {'AI':>2} {'独自':>4}  キーワード")
    print("-" * 92)
    for r in view[:top]:
        old = r["priority_rank"].strip() or "—"
        print(f"{r['new_rank']:>3} {old:>4}  {r['score']:>6} {vol(r):>7,} "
              f"{r['cv_distance']:>2} {r['difficulty']:>4} {r['ai_risk']:>2} "
              f"{r['uniqueness']:>4}  {r['keyword']}")

    # 旧優先50位との入れ替わり
    old50 = {r["keyword"] for r in rows if r["priority_rank"].strip().isdigit()}
    new50 = {r["keyword"] for r in rows[:50]}
    added, dropped = new50 - old50, old50 - new50
    print(f"\n旧優先50位からの変化: 新規浮上 {len(added)}語 / 圏外 {len(dropped)}語")
    if added:
        print("  ▲ 新たに50位以内:", "、".join(sorted(added)[:12]) + ("…" if len(added) > 12 else ""))
    if dropped:
        print("  ▼ 50位圏外へ  :", "、".join(sorted(dropped)[:12]) + ("…" if len(dropped) > 12 else ""))
    ties = {}
    for r in rows[:top]:
        ties.setdefault(r["score"], 0)
        ties[r["score"]] += 1
    worst = max(ties.values()) if ties else 0
    if worst >= 5:
        print(f"\n⚠️ 上位{top}件中、同点が最大{worst}語。ボリュームの粒度が粗く、スコアが順位を"
              f"決められていません。\n   → 実ボリュームを取得して再実行してください"
              f"（tools/merge_volume.py）。")
    if not measured:
        print("\n⚠️ 推定ボリュームでの計算です。実測後に再実行してください。")


if __name__ == "__main__":
    main()
