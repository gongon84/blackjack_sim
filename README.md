## ブラックジャックの戦略シミュレーション  
「ベーシックストラテジー」を用いた「マーチンゲール法」のシミュレーション比較を行いました。  
<br>
### ベーシックストラテジーとは？  
ディーラーのオープンされてるカードと自分の手札から最適なアクションを行う戦略。  
ブラックジャックで有名な戦略シート。  
<img src="https://user-images.githubusercontent.com/57177320/92253818-f35ea900-ef0a-11ea-8871-6921f9c3b350.png" width="600px">  
<br>

### マーチンゲール法とは？  
負ける度に賭け金を２倍にする戦略。勝った場合の掛け金は１に戻る。  
連敗してもその後に勝つことで負けた分を取り返せる特徴がある。  

例  
ゲーム数｜賭け金｜勝敗｜合計  
　　１　｜　１　｜負け｜ー１  
　　２　｜　２　｜負け｜ー３  
　　３　｜　４　｜負け｜ー７  
　　４　｜　８　｜勝ち｜＋１  
　　５　｜　１　｜勝ち｜＋２  
<br>

### 検証手法  
以下の４つの戦略を考える。  
  
「引き方」  
・ディーラーと同じ動き（以下 normal）  
・ベーシックストラテジー（以下 BS）  
  
「賭け方」  
・ずっと１（以下 normal'）  
・マーチンゲール法（以下 MG）  
<br>

### 適用ルール

今回適用するルールは以下の通りです。  
・プレイヤーはバースト時(22以上)で強制負け  
・ディーラーは１７以上になるまで引く  
・ダブルは１枚ドローしてスタンド  
・デッキは１ゲーム毎にリセット  

※以下のルールは含めない  
・スプリット  
・サレンダー  
・インシュランス  
<br>

### 結果  
### 1. normal & normal'  
<img src="https://user-images.githubusercontent.com/57177320/92250383-5c8fed80-ef06-11ea-99ee-ab9548c73027.png" width="400px">  
試行回数 ５００回<br>金額 １０００ → ９６０  
  
### 2. normal & MG  
<img src="https://user-images.githubusercontent.com/57177320/92251029-33239180-ef07-11ea-8f8d-fd478c6556f1.png" width="400px">  
試行回数 500回<br>金額 1000 → 1207  
  
### 3. BS & normal'  
<img src="https://user-images.githubusercontent.com/57177320/92251046-36b71880-ef07-11ea-98b0-6ee87b1fcdb4.png" width="400px">  
試行回数 500回<br>金額 1000 → 972  
  
### 4. BS & MG  
<img src="https://user-images.githubusercontent.com/57177320/92251051-39197280-ef07-11ea-938a-d911f4194391.png" width="400px">  
試行回数 500回<br>金額 1000 → 1584  
<br>

### 考察＆今後の展望  
○マーチンゲール法は資金が増えるが、一時的にマイナスになる可能性がある。  
→ 自分の手持ちの資金からどれくらいのリスクを取れるのか？（何連敗まで平気か）を知りたい  
  
○BSを用いたが思ったより増えなかった  
→ スプリットやサレンダーなど設定を実際のルールに近づける必要がある  
