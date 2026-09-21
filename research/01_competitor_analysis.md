# 保育士転職メディア 競合構造分析（SEO）

- 作成日: 2026-09-21
- 対象: 新規立ち上げ「保育士向け転職メディア（アフィリエイト収益モデル）」
- 調査手法: WebSearch による実検索（本編22クエリ＋園長視点検証8クエリ＝計30クエリ）＋ WebFetch による実ページ閲覧

## 0. 調査上の制約（必読）

本セッションの実行環境では、**組織のネットワーク egress ポリシーにより、ほぼ全ての対象ドメインへの直接アクセス（WebFetch / curl とも）がブロックされました**。実際にブロックされたことを確認したドメイン:

`www.hoikushibank.com` / `www.hoikushibank-column.com` / `hoiku.jinzaibank.com` / `hoiku-is.jp` / `job-medley.com` / `simples.co.jp` / `axxis.co.jp` / `resemom.jp` / `hoiku.mynavi.jp` / `tenshoku.mynavi.jp` / `jp.indeed.com` / `hoikushi-worker.com` / `hoikubatake.jp` / `solasto-career.com` / `levwell.jp` / `minhyo.jp` / `note.com` / `ja.dev` / `developers.google.com` / `www.mhlw.go.jp` ほか多数（エラー: `CONNECT tunnel failed, response 403` = `connect_rejected (organization policy)`）。

その結果、本レポートの信頼度は以下のように分かれます。

| セクション | 一次情報の質 |
|---|---|
| 1. SERP占有状況（22クエリ） | **実検索済み・一次情報**（WebSearch で実際に返ってきたURL） |
| 3-A. マイベスト（my-best.com）のページ構造 | **実閲覧済み・一次情報**（唯一アクセスできたドメイン） |
| 3-B〜E. その他4サイトのページ構造 | **未確認（間接情報）**。SERPのタイトル・スニペット・運営者情報の検索結果からの推定。文字数・CTA位置・パンくず等の細部は **未確認** と明記 |
| 5. Googleアップデート | 二次情報（SEO解説記事）。Google公式ドキュメント（developers.google.com）は直接閲覧できず **未検証** |

→ **推奨アクション**: セクション3-B〜E と セクション5 のGoogle公式ソースは、egress 許可のある環境で再調査すること（後述 §8）。

---

## 1. 主要検索クエリ別 上位ドメイン一覧（実検索結果）

WebSearch が返した上位（概ね上位9〜10件相当）をそのまま記載。検索日 2026-09-21。

### 1-1. クエリ一覧と上位ドメイン

| # | クエリ | 上位ドメイン（出現順） |
|---|---|---|
| 1 | 保育士 転職 | hoiku.mynavi.jp / tenshoku.mynavi.jp / co-medical.com ×2 / hoikushibank.com ×2 / hoikushibank-column.com / hoikubatake.jp / simples.co.jp |
| 2 | 保育士 転職サイト おすすめ | coeteco.jp / axxis.co.jp / my-best.com / neo-career.co.jp / simples.co.jp / jipcc.or.jp / willof-hoikushi.jp / emiris.net / busiconet.co.jp |
| 3 | 保育士 求人サイト 比較 | brush-up.jp / axxis.co.jp / my-best.com / hoikushi-japan.sakura.ne.jp / 2b-connect.jp / simples.co.jp / emiris.net / busiconet.co.jp / method-innovation.co.jp |
| 4 | 保育士 辞めたい | studying.jp / co-medical.com / kidsline.me / kidsna-connect.com / hoikushibank-column.com / neo-career.co.jp / kirara-support.jp / 1049.cc / hoiku.jinzaibank.com |
| 5 | 保育士 転職 失敗 | co-medical.com / hoikucollection.jp / hoiku-labo.com / hoiku.jinzaibank.com / simples.co.jp ×2 / hoikunosekai.com / initias-recruit.jp / recruit.yukinohana-sukusuku.com |
| 6 | 保育士 給料 安い | agaroot.jp / chiebukuro.yahoo.co.jp / braves.co.jp ×2 / hoikucollection.jp / hoikushi-worker.com / hoikushibank-column.com / note.com / simples.co.jp |
| 7 | 保育士 派遣 | braves.co.jp / jp.indeed.com ×2 / hoikushi-worker.com / asuka-hu.co.jp / watashi-hoiku.jp / hoiku.jinzaibank.com / 求人ボックス / hoiku-box.net |
| 8 | 保育士 面接 質問 | co-medical.com / hoikucollection.jp / hoikushi-syusyoku.com / solasto-career.com / job-medley.com / hoiku.jinzaibank.com / s-agent.jp / hoikukyuujin.com / hoikushi-jobs.com |
| 9 | 保育士 志望動機 転職 | tenshoku.mynavi.jp / studying.jp / co-medical.com / hoikucollection.jp / solasto-career.com / hoikushibank-column.com / job-medley.com / hoiku.jinzaibank.com / hoiku-shigoto.com |
| 10 | 保育士バンク 評判 口コミ | axxis.co.jp ×2 / hoiku-is.jp / tenshoku.asiro.co.jp / resemom.jp / ponpococco.com / medical-link.co.jp / kokoronomannnaka.com / busiconet.co.jp |
| 11 | 保育士ワーカー 評判 | resemom.jp / minhyo.jp / hoikushi-worker.com / 2b-connect.jp / hoipura.jp / medical-link.co.jp / appart.co.jp / busiconet.co.jp / hakenreco.com |
| 12 | 保育士 異業種 転職 おすすめ | jp.indeed.com / hoiku.mynavi.jp / braves.co.jp / co-medical.com / hoikushibank-column.com / neo-career.co.jp / ichitasu.co.jp / kaigo-pro.web-box.co.jp / cheerup-hoiku.com |
| 13 | 保育士 年収 平均 | tcw.ac.jp / mhlw.go.jp / resemom.jp / manpowergroup.jp / hoikushibank.com / co-medical.com / 求人ボックス / simples.co.jp / hoikukyuujin.com |
| 14 | 保育士 求人 東京 | levwell.jp / baitoru.com / jp.indeed.com / hoiku.benesse-style-care.co.jp / hoikushibank.com / watashi-hoiku.jp / hoiku-shigoto.com / hoikukyuujin.com / hoiku-job.net |
| 15 | 保育士 転職 30代 未経験 | g-asuka.co.jp / axxis.co.jp / hoikucollection.jp / asiro.co.jp / hoiku.mynavi.jp / hoikushibank-column.com / hoikukyuujin.com / hoiku.jinzaibank.com / hoikunosekai.com |
| 16 | 保育士 退職 理由 伝え方 | hoiku.levwell.jp / hoikucollection.jp / karu-keru.com / solasto-career.com / hoikushi-syusyoku.com / hoikushibank-column.com / hoiku.jinzaibank.com / willof-hoikushi.jp / hoiku-box.net |
| 17 | 保育士 パート 働き方 | column.poppins.co.jp / g-asuka.co.jp / hoikushibank.com / hoikucollection.jp / solasto-career.com / hoikushibank-column.com / hoikubatake.jp / hoiku.jinzaibank.com / hoiku-box.net |
| 18 | 保育士 人間関係 悩み | g-asuka.co.jp / hoikushibank.com / hoiku.levwell.jp / jje.ac.jp / co-medical.com / hoiku.jinzaibank.com / hoipura.jp / 1049.cc / aruru.alpha-co.com |
| 19 | 保育士 転職 タイミング 年度途中 | hoiku.levwell.jp / hoiku.mynavi.jp / hoikushi-worker.com / hoikushibank-column.com / hoiku.jinzaibank.com ×2 / hoiku-shigoto.com / sinaikai-hoiku.com / ayuminomori.info |
| 20 | 保育士 辞めてよかった ブログ 体験談 | asiro.co.jp / coeteco.jp / hoiku-is.jp / reskill.gakken.jp / note.com / job-medley.com / hoiku-pocket.jp / hoiku-partners.com / hoicari.com |
| 21 | 保育士 転職サイト 電話なし | tenshoku.asiro.co.jp / axxis.co.jp / coeteco.jp / asiro.co.jp / hoipura.jp / medical-link.co.jp / simples.co.jp / hataraku-hoiku.jp / hoiku-kango-eiyou-tensyoku.com |
| 22 | 保育士 ブランク 復帰 不安 | braves.co.jp / co-medical.com / hoikushibank-column.com / hoikubatake.jp / hoipura.jp / hoikukyuujin.com / hoikunosekai.com / willof-hoikushi.jp / hoikushione.com |

---

## 2. ドメイン分類と占有率

### 2-1. 分類定義とドメイン割当

| 区分 | 定義 | 該当ドメイン（本調査で観測） |
|---|---|---|
| **①事業者一次メディア** | 人材紹介・派遣会社の自社オウンドメディア | hoikushibank.com / hoikushibank-column.com / hoikushi-syusyoku.com（ネクストビート）、hoiku.jinzaibank.com（エス・エム・エス）、hoikushi-worker.com（トライト）、hoiku.mynavi.jp・tenshoku.mynavi.jp（マイナビ）、job-medley.com（メドレー）、hoikubatake.jp（ニッソーネット）、levwell.jp・hoiku.levwell.jp（レバレジーズメディカルケア）、solasto-career.com（ソラスト）、hoiku-shigoto.com（ウェルクス）、willof-hoikushi.jp（ウィルオブ・ワーク）、braves.co.jp、hoikucollection.jp、co-medical.com、g-asuka.co.jp・asuka-hu.co.jp、hoiku-box.net、hoikukyuujin.com、hoikunosekai.com、neo-career.co.jp/careertrus、**simples.co.jp/magazine**、watashi-hoiku.jp、karu-keru.com、hoiku-labo.com、hoikushi-jobs.com、kirara-support.jp、1049.cc、column.poppins.co.jp、cheerup-hoiku.com、hoiku-job.net、hoikushione.com、s-agent.jp |
| **②専門メディア／情報サイト** | 保育業界の情報メディア（求人送客は副次） | hoiku-is.jp（ほいくis）、kidsna-connect.com、kidsline.me |
| **③第三者アフィリエイト比較メディア** | 人材紹介を本業としない事業者／個人による比較・口コミ媒体 | my-best.com、axxis.co.jp/magazine（すべらない転職）、asiro.co.jp/media-career・tenshoku.asiro.co.jp（キャリアアップステージ／アシロ）、coeteco.jp（GMOメディア）、resemom.jp/manabi（ミツカル学び／イード）、busiconet.co.jp/evowork、medical-link.co.jp/nextcareers、2b-connect.jp/tensyoku-connect、appart.co.jp/upcareer、hakenreco.com、emiris.net、method-innovation.co.jp/michibi-q、**jipcc.or.jp/jipcc-tensyoku**、brush-up.jp、reskill.gakken.jp、studying.jp、agaroot.jp、kaigo-pro.web-box.co.jp、hoipura.jp、hoicari.com、minhyo.jp、hataraku-hoiku.jp |
| **④大手ポータル** | jp.indeed.com、求人ボックス（xn--pckua2a7gp15o89zb.com）、baitoru.com、doda.jp |
| **⑤個人ブログ・体験談・UGC** | note.com（個人アカウント）、ponpococco.com（ほいくのおまもり）、kokoronomannnaka.com、hoiku-kango-eiyou-tensyoku.com、hoikushi-japan.sakura.ne.jp、detail.chiebukuro.yahoo.co.jp、aruru.alpha-co.com |
| **⑥その他**（参考） | 養成校（tcw.ac.jp、jje.ac.jp）、公的（mhlw.go.jp）、**保育園・法人の採用サイト**（initias-recruit.jp、recruit.yukinohana-sukusuku.com、sinaikai-hoiku.com、ayuminomori.info、hoiku.benesse-style-care.co.jp）、ichitasu.co.jp、manpowergroup.jp |

> **重要な分類注記**
> - `simples.co.jp/magazine`（しんぷるマガジン）は「保育の転職総合メディア」を名乗るが、**運営はSimple株式会社（有料職業紹介 13-ユ-311091、「しんぷる保育」運営）→ ①事業者一次メディア**。出典: https://www.jesra.or.jp/search/1431/ , https://simples.co.jp/service/
> - `asiro.co.jp`（株式会社アシロ、東証グロース 7378）は **メディア事業者だが自社で有料職業紹介 13-ユ-313782 を保有**する③と①のハイブリッド。出典: https://asiro.co.jp/media-career/operator-information/
> - `resemom.jp/manabi`（ミツカル学び）は教育ニュースメディア ReseMom（株式会社イード）の**サブディレクトリ**。出典: https://resemom.jp/manabi/company/

### 2-2. クエリ種別ごとの占有率（各クエリ上位9件ベースの実測）

| クエリ種別 | 代表クエリ | ① 事業者一次 | ② 専門メディア | ③ 第三者アフィリ | ④ ポータル | ⑤ 個人 | ⑥ その他 |
|---|---|---|---|---|---|---|---|
| **A. サービス比較・ランキング** | 転職サイト おすすめ／求人サイト 比較 | **22%** | 0% | **72%** | 0% | 6% | 0% |
| **B. 個社の評判・口コミ** | 保育士バンク 評判／保育士ワーカー 評判 | 6% | 6% | **78%** | 0% | 11% | 0% |
| **C. 条件付きロングテール比較** | 転職サイト 電話なし | 11% | 0% | **78%** | 0% | 11% | 0% |
| **D. 体験談・感情系** | 辞めてよかった 体験談 | 33% | 11% | **44%** | 0% | 11% | 0% |
| **E. 悩み・意思決定系** | 辞めたい／転職失敗／人間関係／給料安い／ブランク／転職タイミング | **72%** | 4% | 6% | 0% | 6% | 13% |
| **F. 業務ノウハウ系** | 面接 質問／志望動機／退職理由／パート働き方 | **94%** | 0% | 3% | 0% | 0% | 3% |
| **G. 求人ナビ・地域系** | 求人 東京／派遣 | **67%** | 0% | **0%** | **28%** | 0% | 6% |
| **H. データ・統計系** | 年収 平均 | 56% | 0% | 11% | 11% | 0% | 22% |

**一目でわかる線引き:**

```
③第三者アフィリエイトの占有率
  ■■■■■■■■  78%   B. 個社評判・口コミ
  ■■■■■■■■  78%   C. 条件付きロングテール比較
  ■■■■■■■   72%   A. 比較・ランキング
  ■■■■       44%   D. 体験談
  ■           11%   H. データ系
  ■            6%   E. 悩み・意思決定系
  ·            3%   F. 業務ノウハウ系
  ·            0%   G. 求人ナビ・地域系
```

### 2-3. 個別ドメインの露出頻度（22クエリ中の出現回数）

| 順位 | ドメイン | 区分 | 出現回数 |
|---|---|---|---|
| 1 | hoiku.jinzaibank.com（保育士人材バンク） | ① | 10 |
| 2 | hoikushibank.com + hoikushibank-column.com + hoikushi-syusyoku.com（保育士バンク！） | ① | 12（3ドメイン合算） |
| 3 | co-medical.com（コメディカルドットコム） | ① | 8 |
| 4 | hoikucollection.jp（ほいコレ） | ① | 6 |
| 5 | simples.co.jp（しんぷるマガジン） | ① | 6 |
| 6 | axxis.co.jp（すべらない転職） | ③ | 5 |
| 7 | asiro.co.jp + tenshoku.asiro.co.jp（キャリアアップステージ） | ③ | 4 |
| 8 | hoikukyuujin.com（保育求人ガイド／保育士くらぶ） | ① | 4 |
| 8 | hoipura.jp | ③ | 4 |
| 10 | my-best.com / coeteco.jp / resemom.jp / busiconet.co.jp / medical-link.co.jp | ③ | 各 2〜3 |

---

## 3. 上位サイトのページ構造分析

### 3-A. マイベスト（my-best.com/12662）— **実閲覧・一次情報**

出典: https://my-best.com/12662 （閲覧日 2026-09-21）

| 項目 | 内容 |
|---|---|
| タイトル | 【徹底比較】保育士向け転職サイトのおすすめ人気ランキング【2026年7月】 |
| 文字数感 | 約 15,000〜18,000字 |
| H2構成 | ①保育士の転職サイトは掛け持ちしたほうがよい？ → ②保育士向け転職サイトの選び方 → ③**全14選おすすめ人気ランキング** → ④全14サービスを徹底比較！ → ⑤保育士以外にも転職できる？ → ⑥転職サイトとハローワークはどちらがよいの？ → ⑦よくある保育士転職Q&A |
| 監修者 | **野上美希（一般社団法人キッズコンサルタント協会 代表理事）**／ガイド: 真田桃花（マイベスト サービス担当）。顔写真・プロフィール・リンク先あり |
| 掲載社数 | **14社** |
| 評価軸 | ①公開求人数（総数／保育士／正社員／パート／認可保育園／オープニング）をスコア化 ②検索のしやすさ（16項目の検索条件の有無をチェック）をスコア化 |
| 検証方法の記載 | **あり**。「検証のポイント」セクションで調査手順を開示。**調査時点 2026年7月2日を明記** |
| ランキング上位 | 1位 ジョブメドレー（メドレー）4.56／2位 保育士バンク！（ネクストビート）4.70／3位 保育士人材バンク（エス・エム・エス）4.64／4位 保育士ワーカー（トライト）4.15／5位 EUSTYLE CAREER（ユースタイルラボラトリー）4.64 ※5点満点<br>**注: 表示順とスコア順が一致しない（1位4.56 < 2位4.70）。取得時のペアリング誤りか別軸の総合順位かは要再確認** |
| ユーザーの声 | あり（利用者コメントを各社に付与。例: 保育士ワーカー「面談でのヒアリングをしっかりしてくれる」） |
| CTA文言 | 「公式サイトで詳細を見る」／「公式サイト（登録無料）で詳細を見る」／ランキング解説後に「ランキングを見る」 |
| CTA位置 | 各ランキング項目ごと（＝記事中に最低14回） |
| パンくず | `TOP > 就職・転職 > 転職サイト・エージェント > 保育士向け転職サイト・エージェント` （**4階層**） |
| 内部リンク | 助産師転職サイト／看護師転職サイト等の姉妹ランキング、転職サイト全般記事へ複数 |
| 更新日表示 | 「2026.07.31 更新」 |
| PR表記 | **あり**（「ECサイトやメーカー等から送客手数料を受領しており、プロモーションを含みます」） |

**要点**: 第三者アフィリエイトで最上位を取っているマイベストは、①4階層のカテゴリ構造 ②業界団体代表理事による監修 ③日付入りの自社検証プロセス開示 ④PR表記の明示 ——を全部やっている。「スコアを付ける根拠（求人数16項目・検索軸16項目）」という**再現可能な定量検証**が差別化の核。

### 3-B〜E. その他上位サイト — **ページ本体は未確認**

egress ブロックにより本文閲覧不可。以下は SERP タイトル・スニペット・運営者検索からの**推定**であり、細部（文字数・CTA位置・パンくず）は **未確認**。

| サイト | 区分 | URL構造 | 観測できた事実 | 未確認事項 |
|---|---|---|---|---|
| **保育士バンク！**<br>（ネクストビート） | ① | `hoikushibank.com`（求人DB＋一部コラム）／`hoikushibank-column.com/column/`（お役立ちコラム）／`hoikushi-syusyoku.com`（新卒）／`lp.palette.hoikushibank.com`（園向けSaaS） | **コラムを別ドメインに分離する多ドメイン運用**。記事タイトルに「【2026年版】」「【2026年9月最新】」等の年月表記を多用。都道府県ページ（/tokyo, /kumamoto）をタイトルに「【2026年9月最新】」付きで大量保有 | 文字数／監修者表記／CTA位置／パンくず／ドメイン分離の時期と理由 |
| **保育士人材バンク**<br>（エス・エム・エス） | ① | `hoiku.jinzaibank.com/column/<連番>` | 22クエリ中 **10回出現＝本調査最多の単一ドメイン**。`/column/01`〜`/column/202` の**連番URL**。タイトルが「【保育士の人間関係】悩みやエピソードのご紹介！改善方法・解決策、疲れた場合の対策は？」型＝**共起語を全部タイトルに詰める**パターン | 文字数／監修者／CTA／パンくず |
| **しんぷるマガジン**<br>（Simple株式会社） | ① | `simples.co.jp/magazine/<英語スラッグ>` | **人材紹介事業者でありながら「保育士転職サイト・エージェントおすすめ比較ランキング21選」という競合含む比較記事を出し、比較クエリで上位**（Q2, Q3, Q21）。コーポレートドメイン配下のサブディレクトリ運用 | 自社サービス「しんぷる保育」の掲載順位／監修者／文字数 |
| **ほいくis** | ② | `hoiku-is.jp/article/detail/<ID>` | **独自アンケート調査記事を保有**（例:「保育士辞めたい…766人の回答から見えた退職理由とその後の行動を調査【アンケート結果】」）。「【ほいくisお仕事探しシリーズ】」という**転職サービス評判の連載シリーズ**を持ち、「保育士バンク 評判」で③媒体群に混じって上位 | 運営会社・収益モデル／アフィリエイトかタイアップか／監修者 |
| **キャリアアップステージ**<br>（アシロ／東証グロース7378） | ③ | `asiro.co.jp/media-career/<ID>` と `tenshoku.asiro.co.jp/hoiku/<ID>` の**2系統が併存** | **コーポレートドメインのサブディレクトリ**と**サブドメイン**の両方でメディアを運用し、両方が同一クエリ（「電話なし」）で上位。自社で有料職業紹介免許 13-ユ-313782 を保有＝アフィリエイトと直接送客の両建てが可能 | どちらが主か／記事構造／監修者 |

### 3-F. SERPから観測できた「型」の共通項

- **タイトル型**: `【YYYY年M月最新】` または `【2026年版】` ＋ 数字（「おすすめ19選」「失敗する7つの原因」「悩み8選」）＋ `｜運営元名` のサフィックス。ほぼ全社が採用。
- **①事業者一次メディアは「監修者」より「運営者の許認可」で権威性を出す**傾向（「厚生労働大臣認可」「【公式】」をタイトル／サイト名に入れる。例: `【保育士人材バンク】【公式】`、`【保育のせかい(公式)】`、`保育box《公式》`）。
- **③第三者アフィリエイトは外部監修者で権威性を補う**（マイベスト=キッズコンサルタント協会代表理事、`kaigo-pro.web-box.co.jp` は「【転職エージェント監修】」をタイトルに明記）。
- **ブランド接尾辞でSERPの見た目を稼ぐ**: `｜しんぷるマガジン｜保育の転職総合メディア`、`｜保育士・幼稚園教諭のための情報メディア【ほいくis／ほいくいず】` のように、タイトル末尾に長い媒体説明を付ける。

---

## 4. 第三者アフィリエイトが取れているクエリ／取れていないクエリ

### 4-1. 勝敗ライン

| 取れている（③が50%以上） | 取れていない（③が10%以下） |
|---|---|
| 「保育士 転職サイト おすすめ」（③ 67%） | 「保育士 面接 質問」（③ **0%**、① 100%） |
| 「保育士 求人サイト 比較」（③ 78%） | 「保育士 退職 理由 伝え方」（③ **0%**、① 100%） |
| 「保育士バンク 評判 口コミ」（③ 67%） | 「保育士 パート 働き方」（③ **0%**、① 100%） |
| 「保育士ワーカー 評判」（③ 89%） | 「保育士 求人 東京」（③ **0%**、①67%＋④22%） |
| 「保育士 転職サイト 電話なし」（③ 78%） | 「保育士 派遣」（③ **0%**、①67%＋④33%） |
| 「保育士 辞めてよかった 体験談」（③ 44%） | 「保育士 転職」（③ **0%**、① 100%） |
| | 「保育士 転職 失敗」（③ 0%、① 78%） |
| | 「保育士 退職／ブランク／転職タイミング」（③ 0〜11%） |

### 4-2. 線引きの本質

> **③第三者が勝てるのは「どの事業者を選ぶか」を意思決定するクエリだけ。**
> **①事業者一次が勝つのは「業務ノウハウ」「悩み」「求人検索」のクエリ。**

理由は構造的:
1. **「事業者比較」は①にとって利益相反**。保育士バンクが「保育士ワーカーの評判」を中立に書くことはできない。だからここだけ③に空白が残る。唯一の例外が **しんぷるマガジン（Simple社）が比較ランキングを自社で出している**ケース — ①が③の土俵に降りてきている先行事例として要監視。
2. **「求人 東京」「派遣」は求人DBそのものが必要**。③には在庫がないので構造的に勝てない（Indeed・求人ボックスが④として入る）。**ここは初期に狙ってはいけない**。
3. **「面接 質問」「志望動機」「退職理由」は①が9〜10枠を完全に埋めている**。キャリアアドバイザーの現場知見という一次情報の優位が効いている。

### 4-3. 「隙間」の所在（優先度順）

| 優先度 | 隙間 | 根拠（実測） | 難易度 |
|---|---|---|---|
| **S** | **条件付きロングテール比較**（「電話なし」型）| 「電話なし」で③が78%を占有し、うち `hataraku-hoiku.jp` `hoiku-kango-eiyou-tensyoku.com` のような**小規模／個人規模ドメインが2枠入っている**。①の参入は simples.co.jp の1枠のみ | 低 |
| **S** | **個社評判・口コミ**（「〇〇 評判」「しつこい」「退会方法」） | 「保育士ワーカー 評判」で③が89%、`ponpococco.com` `kokoronomannnaka.com` など**個人ブログが2枠**入る（「保育士バンク 評判」） | 低〜中 |
| **A** | **一次アンケート型の体験談** | 「辞めてよかった 体験談」で ほいくis（766人調査）、hoicari.com（152人調査）、hoipura.jp（121名調査）といった**"N人調査"を持つ媒体だけが上位**。テンプレ比較記事は入っていない | 中（調査コストが必要） |
| **A** | **保育士バンクの空白ドメイン間隙** | 保育士バンクは3ドメイン運用（hoikushibank.com / -column.com / hoikushi-syusyoku.com）でカニバリを起こしており、同一クエリで自社2枠を消費している（Q1で2枠、Q13で1枠）。枠の奪取余地あり | 中 |
| **B** | **意思決定クエリ（「辞めたい」「転職失敗」）** | ①が67〜78%だが、**保育園法人の採用サイトブログが2枠混じる**（initias-recruit.jp、recruit.yukinohana-sukusuku.com、sinaikai-hoiku.com、ayuminomori.info）＝**権威性が低いページでも入れている＝防御が薄い** | 中〜高 |
| **×（回避）** | 業務ノウハウ（面接・志望動機・退職理由・パート） | ①が94% | 非常に高 |
| **×（回避）** | 求人ナビ・地域（求人 東京／派遣） | ③が0%、求人DB必須 | 構造的に不可 |

---

## 5. 2024〜2026年のGoogleアップデートの影響

> **注意**: このセクションは二次情報（国内SEO解説記事）に基づく。Google公式ドキュメント（developers.google.com）は egress ブロックにより **直接検証できていない**。

### 5-1. サイトの評判の不正使用（Site Reputation Abuse）

| 時期 | 内容 | 出典 |
|---|---|---|
| 2024-05-05 | スパムポリシーとして適用開始。Search Console のスパムレポート選択肢に「サイトの評判の不正使用」「期限切れドメインの不正使用」が追加 | https://growthseed.jp/experts/seo/google-updated-reputation-abuse-policy/ |
| 2024-11-20 | **ポリシー拡大**。「ファーストパーティの関与やコンテンツ監視の有無にかかわらず違反」と明確化＝**自社で運営していてもサイト本来の目的と無関係なら違反** | https://developers.google.com/search/blog/2024/11/site-reputation-abuse?hl=ja （**未検証**） |
| 2025-01-21 | ドキュメント更新・違反内容をさらに明確化 | https://www.suzukikenichi.com/blog/google-clarifying-the-site-reputation-abuse-policy/ |
| 2025-11-13 | 欧州委員会がDMA違反の疑いで本ポリシーの調査を開始、GoogleはEEA内の運用を調整。**日本には直接適用されない** | 上記検索結果より（**要再検証**） |

**この領域への含意 — 本調査で観測された高リスク構造:**

| ドメイン | 構造 | リスク評価 |
|---|---|---|
| `jipcc.or.jp/jipcc-tensyoku/tensyoku-hoikushi/` | **一般社団法人ドメイン配下**の転職アフィリエイト。「保育士 転職サイト おすすめ」で上位 | **最高**。社団法人の本来目的と無関係 |
| `resemom.jp/manabi/`（ミツカル学び） | 教育ニュースメディア ReseMom（イード）の**サブディレクトリ**で転職比較を展開 | 高。ただし「ReseMom編集部」が運営＝ファーストパーティ。2024/11の拡大解釈では依然リスク |
| `busiconet.co.jp/evowork/` / `medical-link.co.jp/nextcareers/` / `2b-connect.jp/tensyoku-connect/` / `appart.co.jp/upcareer/` / `kaigo-pro.web-box.co.jp` / `method-innovation.co.jp/michibi-q/` | **コーポレートドメイン＋サブディレクトリ**型の比較メディア。「評判」系クエリに集中 | 中〜高 |
| `asiro.co.jp/media-career/` | 同上だが、アシロは**自社で有料職業紹介免許を保有**＝事業として整合 | 中（説明可能性あり） |

→ **戦略含意**: 現在「評判」系クエリの上位の多くは**この構造的脆弱性を抱えている**。独立ドメインで正攻法に作れば、ポリシー執行が強まったときに枠が空く。

### 5-2. コアアップデートの履歴と影響（2025〜2026）

| 実施 | 期間 | 観測された影響 |
|---|---|---|
| 2025年 | 3月／6月／9月／12月（年4回） | 12月アップデートの上位3位変動率 **66.8%** |
| 2026年2月 | Discover 専用コアアップデート | — |
| **2026年3月27日〜4月8日**<br>March 2026 core update | 約2週間 | **米国上位3位圏内の約80%で順位変動**（過去数年で最大級）。「AI生成コンテンツや独自性の乏しい二次情報の記事順位が下落、一次情報や専門性を備えた高品質サイトが上昇」「**個人発信コンテンツの評価向上**（ブログサービス、YouTube/Instagram/TikTok、FAQサイトが上昇傾向）」 |
| 2026年5月22日〜6月2日<br>May 2026 core update | 約2週間 | — |
| 2026年9月時点 | **最新は5月。6月以降の新規コアアップデートの公式発表なし** | — |

**相反する2つの観測（重要）:**

| 観測A（アフィリエイト不利） | 観測B（個人有利） |
|---|---|
| 「2026年3月コアアップデートでアフィリエイトサイトの **71%** がネガティブな順位影響。**テンプレート化された比較ページやレビューコンテンツ、一次検証を欠いた評価ページ**が標的」<br>出典: https://ai-heartland.com/news/google-2026-3-71/ （**媒体の信頼度は低い。数値は要検証**） | 「個人発信コンテンツの評価向上で、ブログサービス、SNS、FAQサイトが上昇傾向」<br>出典: https://manamina.valuesccg.com/articles/4945 / https://infinity-agent.co.jp/lab/latest-news/news0430-google-coreupdate-2026/ |

**この矛盾の読み解き（本調査の解釈）**: 落ちたのは「アフィリエイトサイト」そのものではなく **「一次検証のないテンプレ比較ページ」**。上がったのは **「一次体験・一次データのある個人発信」**。両観測は同じ軸の裏表であり、**"個人だから不利" ではなく "一次情報がないから不利"** と解すべき。実際 SERP でも、一次アンケートを持つ hoiku-is.jp（766人）・hoicari.com（152人）・hoipura.jp（121名）が体験談クエリで生き残り、無検証のテンプレ比較は「辞めてよかった」クエリに一つも入っていない。

### 5-3. AI Overviews / AI Mode の影響

| 指標 | 数値 | 出典 |
|---|---|---|
| 日本の情報系KW: AIO表示時の1位CTR | **9.0%**（AIO非表示時の推定 24.1%）＝ **62.7% 減** | https://webtan.impress.co.jp/n/2026/07/29/53036 （Ahrefs調べ） |
| 日本の1位CTR低下（別集計） | 約 **38%** 低下（グローバルは約58%減） | https://www.commercepick.com/archives/86565 |
| AIOトリガー率（2026年4月時点） | 追跡クエリの約 **48%**（前年比 +58%） | 同上 |
| **転職業界のAIO表示率（2026年2月時点）** | **減少傾向**。クレジットカード・保険・化粧品・不動産が増加傾向なのと対照的 | https://oneder.hakuhodody-one.co.jp/blog/ai-search-engine-202602 （博報堂DYONE） |

**この領域への含意**: 転職領域は AIO 表示率が下がっており、AIOによるトラフィック毀損は他業種（保険・不動産等）より **相対的に軽い**。ただし「保育士 年収 平均」「保育士 給料 安い」のような**事実回答型クエリはAIOに食われやすい**。逆に「どのサービスを選ぶか」「電話なしで使えるのはどれか」といった**比較・選択型クエリはクリックが残りやすい**——これは §4 の隙間分析と同じ方向を指している。

### 5-4. 2026年時点で「個人アフィリエイトが転職領域で上位を取れる余地」はあるか — 結論

**ある。ただし条件付きで、かつ領域は狭い。** 本調査の実測での根拠:

- ✅ **実在する**: 「保育士バンク 評判」で `ponpococco.com`（ほいくのおまもり）と `kokoronomannnaka.com` が上位9件中2枠。「保育士 転職サイト 電話なし」で `hataraku-hoiku.jp` と `hoiku-kango-eiyou-tensyoku.com` が2枠。「保育士 求人サイト 比較」で `hoikushi-japan.sakura.ne.jp`（さくらレンタルサーバのサブドメイン）が1枠。
- ✅ **上位の資本力は絶対ではない**: 「保育士 転職 失敗」では**保育園法人の採用サイトのブログ記事**（`recruit.yukinohana-sukusuku.com`、`initias-recruit.jp`）が上位に入っている＝この領域の一部クエリは防御が非常に薄い。
- ❌ **ただし勝てない領域が明確**: 「保育士 転職」「保育士 面接 質問」「保育士 退職 理由 伝え方」「保育士 パート 働き方」「保育士 求人 東京」「保育士 派遣」は ① が9〜10枠を占有し、個人の入る隙は **0枠**。
- ⚠️ **リスク**: 2026年3月コアアップデートで「一次検証を欠いたテンプレ比較ページ」が集中的に落ちたという観測。単なるASP情報の焼き直しは短命。

---

## 6. 園長視点の空白マップ【追加検証】

### 6-0. 検証した仮説

> 「現役の保育園 園長（＝採用決裁者）の視点」で書かれた保育士転職コンテンツは市場にほぼ存在しない。人材紹介会社のオウンドメディアは**顧客が保育園である**ため、園に不都合な情報を構造上書けないから。

**検証結果: 仮説はほぼ全面的に支持された。** 追加8クエリを実検索した結果、「採用する側の視点で、求職者の利益のために」書かれたコンテンツは **上位に1件も発見できなかった**。さらに仮説より強い事実として、**人材紹介会社が書いたBtoB（園の採用担当者向け）記事が、求職者向けクエリの上位に混入している**ことを複数確認した。

### 6-1. 追加8クエリの上位ドメインと「視点」の判定

| # | クエリ | 上位ドメイン（出現順） | 採用側視点で求職者に書かれた記事 |
|---|---|---|---|
| A1 | 保育士 面接 園長 見ているポイント | hoiku.mynavi.jp / co-medical.com / karu-keru.com / braves.co.jp / **hoikushibank-column.com（BtoB記事）** / job-medley.com / s-agent.jp / hoiku.jinzaibank.com / hoikukyuujin.com | **0件**。全て求職者向けの一般面接対策。園長視点を名乗るものなし |
| A2 | 保育園 採用 されない 理由 不採用 | hoiku.mynavi.jp / hoikushibank-column.com / hoiku-labo.com / hoikunokatachi.jp / simple-hoiku.com / cheerup-hoiku.com / hoiku-job.net / willtec.work / hoiku.jobtoru.com | **0件**。全て①事業者。「落ちた理由」を採用決裁者が語る記事なし |
| A3 | 保育士 園見学 チェックポイント | hoiku.mynavi.jp / kidsline.me / npartner.jp / mirashiru.dai-ichi-life.co.jp / hoikuoyanokai.com / hoipura.jp / lykke-woman.jp / simple-hoiku.com / mirai-kids-monte.com | **0件**。しかも**上位の半数が「保活（保護者が子を預ける）」の園見学記事**でインテント混線。保育士向けは2〜3枠のみ |
| A4 | 保育士 人材紹介 手数料 保育園 負担 相場 | **hoikushibank-column.com ×3（うち2本が【採用担当者向けコラム】明示）** / ameblo.jp / hoikunokatachi.jp / neo-career.co.jp（みんなの採用部＝BtoB） / hoiken.co.jp（BtoB） / column.chipotle.co.jp（BtoB） / recruit.connect-mktg.com（BtoB） | **0件**。上位9件中 **7件がBtoB（園向け）** 。求職者向けは実質ゼロ |
| A5 | 保育園 紹介会社 経由 採用 園長 敬遠 | hrnote.jp（BtoB） / imitsu.jp（BtoB） / hoikushibank-column.com ×3 / hoikushi-worker.com / neo-career.co.jp（BtoB） / hoiku.jinzaibank.com / hoikunokatachi.jp | **0件**。「紹介会社経由だと不利か」を求職者目線で扱った記事は**検索上位に存在せず** |
| A6 | 保育園 採用担当 本音 保育士 採用したい人 | braves.co.jp / karu-keru.com / **saiyo-kakaricho.com（BtoB）** / solasto-career.com ×2 / job-it.jp / hoikunokatachi.jp / job-medley.com / hoikukyuujin.com | **0件**。「本音」を名乗る記事すら不在。BtoBの採用手法記事が混入 |
| A7 | 保育園 ずっと求人 出し続けている 園 理由 | jaic-college.jp / kaigojob.com / kidsline.me / kidsna-connect.com / **hoikushibank-column.com（「経営者がすべき改善策」＝BtoB）** / **note.com/kind_panda380（現役保育士）** / hoikubatake.jp / magazine.meetcareer.net / dym.asia | **0件**（園長視点）。唯一の"内部者視点"は**個人noteの現役保育士**1枠 |
| A8 | 保育士 志望動機 園長 響く 採用側 | tenshoku.mynavi.jp / co-medical.com / hoikucollection.jp ×2 / hoikushi-syusyoku.com / hoikushibank-column.com / job-medley.com / hoiku-shigoto.com / kosodatehoikujoho.com | **0件**。①事業者が9枠中8枠。全て「例文集」型 |

### 6-2. 決定的証拠: BtoB記事の求職者クエリへの混入

仮説の裏づけとして最も強い観測。**人材紹介会社は、園向け記事を求職者クエリにぶつけて枠を埋めている**。

| 記事 | URL | 本来の読者 | 上位表示された求職者クエリ |
|---|---|---|---|
| 【採用担当者向けコラム】**園長先生必見！**保育士さんとの面談では何を話す？ | https://www.hoikushibank-column.com/column/post_2749 | 園長 | 「保育士 面接 園長 見ているポイント」**5位相当** |
| 職場の雰囲気が悪い保育園にありがちな4つの特徴と**経営者がすべき改善策** | https://www.hoikushibank-column.com/column/post_2602 | 園の経営者 | 「保育園 ずっと求人 出し続けている 園 理由」**5位相当** |
| 【採用担当者向けコラム】保育士の人材紹介手数料は高い？相場や会社による違いを解説！ | https://www.hoikushibank-column.com/column/post_3081 | 園の採用担当 | 「保育士 人材紹介 手数料」**2位相当** |
| 【採用担当者向けコラム】保育士の人材紹介とは？使い方や手数料、採用につなげるポイント | https://www.hoikushibank-column.com/column/post_2785 | 園の採用担当 | 「保育士 人材紹介 手数料」**3位相当** |
| 保育士の人材紹介に支払う手数料は？相場や人材紹介を使うメリット・デメリット | https://www.hoikushibank-column.com/column/post_2720 | 園（支払側） | 「保育士 人材紹介 手数料」**1位相当** |

**読み解き**: 保育士バンク！（ネクストビート）は、求職者向けコラムと園向けコラムを**同一ドメイン `hoikushibank-column.com` に同居させている**。結果、求職者が「園長は何を見ているのか」「紹介手数料はいくらなのか」を調べると、**園に向けて書かれた文章に着地する**。
これはまさに仮説の指摘どおりの構造的利益相反であり、同時に **検索ユーザーの意図に正面から答えていない = 隙間**である。

### 6-3. 最大の空白: 人材紹介手数料の「求職者にとっての意味」

観測された事実（すべて①事業者またはBtoB媒体が公開しているもの）:

| 事実 | 数値 | 出典 |
|---|---|---|
| 紹介手数料の相場 | **理論年収の20〜40%**。2026年現在は **30〜35%** が一般的 | https://www.hoikushibank-column.com/column/post_2720 , https://hoikunokatachi.jp/chiebukuro2/recruitment-commission/ |
| 1人採用あたりの実額 | **約65万〜130万円**（保育士平均年収326.8万円ベース）。常勤ベースで80〜100万円という調査も | 同上 / https://www.neo-career.co.jp/humanresource/knowhow/a-contents-middlecareer-hoikusi-syoukairyoukin-hikaku191031/ |
| 園が人材紹介を使う理由 | 「他の採用手法では人材が確保できなかった」**72.1%**（厚労省資料） | https://www.hoikushibank-column.com/column/post_2720 |

**これらの数字はすべて「園に向けて」語られており、求職者に向けて語られていない。**
求職者にとっての意味 —— 「あなたを採用すると園は約100万円払う」「だから紹介会社経由は書類が通りにくい園がある」「だから手数料を払ってでも採りたい園＝人が定着していない園である可能性」「直接応募／ハローワーク併用で交渉余地が変わる」—— を扱った記事は、A4・A5 クエリの上位 **18枠中ゼロ**。

> **これが本調査で見つかった最大かつ最も防御しにくい空白。** ①事業者は自らの収益源を否定する記事を絶対に書けず、③第三者アフィリエイト媒体も紹介会社がクライアント（＝ASP広告主）なので書きにくい。**アフィリエイト媒体にとってもセンシティブだが、"どの紹介会社を選ぶか"の比較記事に接続すれば収益とは両立しうる。**

### 6-4. 「園長監修」「現役園長」を名乗るメディアの有無

| 調査項目 | 結果 |
|---|---|
| **「園長監修」を掲げた保育士"転職"メディア** | **発見できず（＝ほぼ空白）**。検索で見つかった「元園長監修」の用例は**月案・週案の文例記事**（保育業務書類）のみで、転職領域ではない |
| 事業者メディアの園長関連ページ | `hoiku.mynavi.jp/feature/manager/`（管理職特集）、`hoikushibank.com/jobtype/director`（園長求人）、`hoiku.jinzaibank.com/column/17`（園長とは）——いずれも **「園長になりたい人向け」であって「園長が求職者に語る」ものではない** |
| 最も近い既存プレイヤー | **保育のカタチ `hoikunokatachi.jp`**（幼保業界の「人」の問題解決に特化した専門家集団）。`/chiebukuro/`（求職者向け）と `/chiebukuro2/`（経営者向け）の **2ディレクトリを併走**させ、両方がSERPに出現（A2, A4, A5, A6 の4クエリで観測）。ただし同社は採用コンサル・人材紹介も行うため**利益相反は①と同型** |
| 個人発信の"内部者視点" | `note.com/kind_panda380`「もう騙されない！保育士が教えるやばい保育園の見抜き方｜くる｜**現役保育士**」（A7で上位）／`note.com/light_sage3143`「Entyo先生の駆け込み寺『園見学がはじめての皆様へ』」／`hoiku-shi.work`「保育士の手帖」。**いずれも"現役保育士"であって"現役園長"ではない**。規模は個人ブログ／note 記事単位で、専門メディア規模のドメインは **未確認** |
| 園長のnote発信の一般的状況 | 「園長は情報発信が苦手／何を発信すべきか分からず、採用期だけ動く」と業界BtoB媒体が指摘。**園長は発信していない**ことが業界側でも認識されている | 出典: https://hoikunokatachi.jp/chiebukuro2/note_owner_point/ |

→ **結論: 「現役園長監修」を明示した保育士転職メディアは、本調査の範囲では存在しない。**（※ドメイン網羅調査ではないため「絶対に存在しない」とは断定できず、**未確認**の余地は残す）

### 6-5. 空白の優先順位マップ

| 優先度 | クエリ群 | 空白の深さ | 収益接続 | 競合の防御力 | 根拠 |
|---|---|---|---|---|---|
| **S+** | **人材紹介手数料・紹介会社経由の採用**（「保育士 人材紹介 手数料」「紹介会社 経由 不利」「直接応募 どっち」） | **最大**。上位18枠中、求職者視点ゼロ。BtoB記事が7枠占拠 | 高（「だからこの紹介会社を選ぶべき」へ接続可能） | **極低**。①は構造上書けない | §6-3 |
| **S** | **園長・採用決裁者の判断基準**（「園長 見ているポイント」「採用担当 本音」「採用されない理由」「志望動機 園長に響く」） | 大。27枠中、採用側視点ゼロ。例文集とマナー論しかない | 中（面接対策→転職サービス訴求） | **低**。①は「キャリアアドバイザー」の権威しか持たず、決裁者の権威は持たない | §6-1 A1/A2/A6/A8 |
| **A** | **園見学・職場の見抜き方**（「園見学 チェックポイント」「やばい保育園 見抜き方」「ずっと求人出している園」） | 中〜大。A3は**保活記事とインテント混線**し、保育士向けが2〜3枠しかない。A7の内部者視点は個人note1枠のみ | 高（見学→応募→サービス送客） | **低**。①は「悪い園の見抜き方」を書くと顧客である園を敵に回す | §6-1 A3/A7 |
| **B** | **不採用の理由・落ちた後の動き方** | 中。①が9枠占拠だが全て一般論 | 中 | 中 | §6-1 A2 |

### 6-6. この角度がSEO上も有利な理由（§5との接続）

- 2026年3月コアアップデートで落ちたのは「**一次検証を欠いたテンプレ比較ページ**」、上がったのは「**一次情報・実体験のある個人発信**」（§5-2）。**現役園長の一次証言は定義上テンプレ化できず、この評価軸に真正面から合致する。**
- §5-3 のとおり転職領域はAI Overviews表示率が**減少傾向**であり、かつ「園長は実際に何を見て落とすのか」は一般的事実の要約では答えられない＝**AIOに要約されにくい**。
- E-E-A-T の観点でも、③第三者媒体が外部監修者（マイベスト＝キッズコンサルタント協会代表理事）で補っている権威性を、**「現役園長＝Experience（経験）」で直接満たせる**。これは資本力ではなく取材力で作れる差分。

**最大のリスク**: 園長は情報発信していない（§6-4）ため、**監修者・取材協力者の確保そのものがボトルネック**。ここが実行上の真のコストであり、同時に参入障壁＝防御力になる。

---

## 7. 出典一覧

### SERP調査（WebSearch、検索日 2026-09-21）
22クエリ分は §1-1 の表に上位ドメインを掲載。

### 実閲覧ページ
- https://my-best.com/12662 — マイベスト「【徹底比較】保育士向け転職サイトのおすすめ人気ランキング【2026年7月】」（2026.07.31更新）

### 運営者確認
- https://www.jesra.or.jp/search/1431/ — Simple株式会社（日本人材紹介事業協会）
- https://simples.co.jp/service/ — しんぷる保育／しんぷる栄養士
- https://asiro.co.jp/media-career/operator-information/ — キャリアアップステージ 運営者情報（アシロ、有料職業紹介 13-ユ-313782）
- https://resemom.jp/manabi/company/ — ミツカル学び 編集部体制と運営社情報（イード）
- https://www.gmo.media/service/coeteco/ — コエテコ（GMOメディア）
- https://ja.wikipedia.org/wiki/コエテコ_byGMO

### Googleアップデート
- https://developers.google.com/search/blog/2024/11/site-reputation-abuse?hl=ja （**未閲覧・未検証**）
- https://www.suzukikenichi.com/blog/google-clarifying-the-site-reputation-abuse-policy/
- https://growthseed.jp/experts/seo/google-updated-reputation-abuse-policy/
- https://oneder.hakuhodody-one.co.jp/blog/google-site-reputation-update
- https://three-dots.co.jp/sub-dile-lending/ — サブディレクトリ貸しと手動ペナルティ
- https://ja.dev/knowledge/search/algorithm_updates/cu/2026-03 — JADE 2026年3月コアアップデート（**未閲覧**）
- https://manamina.valuesccg.com/articles/4945 — March 2026 core update（ヴァリューズ）
- https://infinity-agent.co.jp/lab/latest-news/news0430-google-coreupdate-2026/ — 上位3位圏内80%変動
- https://ai-heartland.com/news/google-2026-3-71/ — アフィリエイト71%下落（**信頼度低・要検証**）
- https://aidaim.co.jp/may-2026-core-update/ — 2026年9月時点の最新コアアップデート状況
- https://webtan.impress.co.jp/n/2026/07/29/53036 — AI Overviews CTR 62.7%減（Ahrefs）
- https://www.commercepick.com/archives/86565 — 日本38%低下／グローバル58%減
- https://oneder.hakuhodody-one.co.jp/blog/ai-search-engine-202602 — 転職業界のAIO表示率減少

### 収益モデル
- https://kookenn.co.jp/aff/job.html — 転職系アフィリエイトのASPと単価
- http://www.zero-affiliate.net/entry/hoikushi-tensyoku-affiliate-asp — 保育士転職案件のASP取扱
- https://xn--cckcdp5nyc8g2109dde1a.com/category/保育士/ — 保育士系転職案件一覧

**報酬相場（二次情報）**: 保育士転職案件は **2,200〜5,000円がボリュームゾーン**、最大 30,000円の案件も存在。個別例: 「ライクキッズ」12,307円、「保育の求人」3,663円。主要ASP: A8.net（転職案件約250件）、afb（介護・福祉系に強い）、アクセストレード（約120件）。※ASP管理画面での実額確認が必要。

### 園長視点の空白検証（追加調査、検索日 2026-09-21）
- https://www.hoikushibank-column.com/column/post_2749 — 【採用担当者向けコラム】園長先生必見！保育士さんとの面談では何を話す？
- https://www.hoikushibank-column.com/column/post_2602 — 職場の雰囲気が悪い保育園にありがちな4つの特徴と経営者がすべき改善策
- https://www.hoikushibank-column.com/column/post_2720 — 保育士の人材紹介に支払う手数料は？（紹介手数料相場・厚労省72.1%の出所）
- https://www.hoikushibank-column.com/column/post_3081 — 【採用担当者向けコラム】保育士の人材紹介手数料は高い？
- https://www.hoikushibank-column.com/column/post_2785 — 【採用担当者向けコラム】保育士の人材紹介とは？
- https://hoikunokatachi.jp/chiebukuro2/recruitment-commission/ — 保育のカタチ 人材紹介手数料
- https://hoikunokatachi.jp/chiebukuro2/note_owner_point/ — 保育園経営者・園長におすすめの発信方法（園長が発信していない実態）
- https://hoikunokatachi.jp/about/ — 保育のカタチ サービス紹介（求職者向け／経営者向けの二面運営）
- https://www.neo-career.co.jp/humanresource/knowhow/a-contents-middlecareer-hoikusi-syoukairyoukin-hikaku191031/ — 保育士の紹介料金4サービス比較（みんなの採用部／BtoB）
- https://note.com/kind_panda380/n/ndfcc8a5feaeb — もう騙されない！保育士が教えるやばい保育園の見抜き方（現役保育士・個人note）
- https://note.com/light_sage3143/n/n91ba96faeff4 — 『園見学がはじめての皆様へ』Entyo先生の駆け込み寺
- https://hoiku.mynavi.jp/feature/manager/ — マイナビ保育士 管理職（園長や主任）特集
- https://www.hoikushibank.com/jobtype/director — 保育士バンク！ 園長求人
- https://hoiken.co.jp/41/ — 保育人材紹介の採用相場（株式会社ほい研／BtoB）
- https://column.chipotle.co.jp/column/008/ — 保育士の採用単価（チポーレ／BtoB）

---

## 8. 再調査が必要な項目（egressブロックのため未実施）

1. 保育士バンク！／保育士人材バンク／ほいくis／しんぷるマガジン／すべらない転職 の**実ページ構造**（文字数・H2型・監修者表記・CTA位置と回数・パンくず・更新日表示）
2. Google公式の「サイトの評判の不正使用」ポリシー原文（2024-11-20版・2025-01-21更新版）の直接確認
3. JADE による 2026年3月コアアップデートの日本語クエリ分析
4. Ahrefs / Similarweb 等による各ドメインの推定流入・被リンク数（本調査では**未取得**）
5. 「保育士転職サイト おすすめ」等でのAI Overviews実表示有無（WebSearchではAIOブロックを観測できない）
6. ASP管理画面での保育士転職案件の実報酬額・承認率
7. 「園長監修」を掲げた保育士転職メディアの網羅調査（本調査は8クエリのSERP観測のみで、ドメイン網羅調査は未実施＝「存在しない」とまでは断定できない）
8. 保育のカタチ（hoikunokatachi.jp）の実ページ構造・運営会社・収益モデル（egressブロックで未閲覧）
9. 紹介手数料相場の一次ソース（厚生労働省「保育士の職業紹介事業に関する調査」等）の直接確認 — 72.1%・20〜40%の原典は未検証
