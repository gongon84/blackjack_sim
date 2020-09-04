## ブラックジャックの戦略シミュレーション  
「ベーシックストラテジー」を用いた「マーチンゲール法」のシミュレーション比較を行いました。  
<br>
### ベーシックストラテジーとは？  
ディーラーのオープンされてるカードと自分の手札から最適なアクションを行う戦略。  
ブラックジャックで有名な戦略シート。  
<画像>  
  
### マーチンゲール法とは？  
負ける度に賭け金を２倍にする戦略。勝った場合の掛け金は１に戻る。  
連敗してもその後に勝つことで負けた分を取り返せる特徴がある。  
<画像>  
  
### 検証手法  
以下の４つの戦略を考える。  
  
「引き方」  
・ディーラーと同じ動き（以下 normal）  
・ベーシックストラテジー（以下 BS）  
  
「賭け方」  
・ずっと１（以下 normal'）  
・マーチンゲール法（以下 MG）  
  
### 結果  
### 1. normal & normal'  
<img src="https://user-images.githubusercontent.com/57177320/92250383-5c8fed80-ef06-11ea-99ee-ab9548c73027.png" width="400px">  
### 2. normal & MG  
＜画像＞
3. BS & normal'  
＜画像＞
4. BS & MG  
  
  
### 考察＆今後の展望  
