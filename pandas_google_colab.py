# -*- coding: utf-8 -*-
"""歡迎使用 Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

!pip install pyquery

from pyquery import PyQuery as pq
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

page_url = "https://www.cnyes.com/twstock/ranking9.aspx"
html_doc = pq(page_url)

stock_name_selector="td+ td a"
prices_selector="td:nth-child(5)"
stock_name=[i.text for i in html_doc(stock_name_selector)]
prices=[float(i.text) for i in html_doc(prices_selector)]
print(stock_name)
print(prices)

#取股票為開曼
ky_stock_name=[]
ky_prices=[]

for i in range(len(stock_name)):
    if "KY" in stock_name[i]:
        ky_stock_name.append(stock_name[i])
        ky_prices.append(prices[i])
print(ky_stock_name)
print(ky_prices)

import pandas as pd

df=pd.DataFrame()
df["stock_name"]=stock_name
df["prices"]=prices
df[df["stock_name"].str.contains("KY")]

df.to_csv("stock.csv",index=False)

!ls

from google.colab import files
files.download("stock.csv")







"""<p><img alt="Colaboratory logo" height="45px" src="/img/colab_favicon.ico" align="left" hspace="10px" vspace="0px"></p>

<h1>什麼是 Colaboratory？</h1>

Colaboratory &#40;簡稱為「Colab」&#41; 可讓你在瀏覽器上撰寫及執行 Python，且具備下列優點： 
- 不必進行任何設定
- 免費使用 GPU
- 輕鬆共用

無論你是<strong>學生</strong>、<strong>數據資料學家</strong>或是 <strong>AI 研究人員</strong>，Colab 都能讓你的工作事半功倍。請觀看 <a href="https://www.youtube.com/watch?v=inN8seMm7UI">Colab 的簡介影片</a>瞭解詳情，或是直接瀏覽以下的新手入門說明！

## <strong>開始使用</strong>

你正在閱讀的文件並非靜態網頁，而是名為 <strong>Colab 筆記本</strong>的互動式環境，可讓你撰寫和執行程式碼。

舉例來說，以下是包含簡短 Python 指令碼的<strong>程式碼儲存格</strong>，可進行運算、將值儲存至變數中並列印運算結果：
"""

seconds_in_a_day = 24 * 60 * 60
seconds_in_a_day

"""如要執行上方儲存格中的程式碼，請按一下進行選取，再按一下程式碼左側的播放鍵，或是使用鍵盤快速鍵「Command/Ctrl + Enter 鍵」。按一下儲存格即可開始編輯程式碼。

在一個儲存格中定義的變數之後可用於其他儲存格：
"""

seconds_in_a_week = 7 * seconds_in_a_day
seconds_in_a_week

"""Colab 筆記本可讓你在單一文件中結合<strong>可執行的程式碼</strong>和 <strong>RTF 格式</strong>，並附帶<strong>圖片</strong>、<strong>HTML</strong>、<strong>LaTeX</strong> 等其他格式的內容。你建立的 Colab 筆記本會儲存到你的 Google 雲端硬碟帳戶中。你可以輕鬆將 Colab 筆記本與同事或朋友共用，讓他們在筆記本上加上註解，或甚至進行編輯。詳情請參閱 <a href="/notebooks/basic_features_overview.ipynb">Colab 總覽</a>。如要建立新的 Colab 筆記本，你可以使用上方的「檔案」選單或以下連結：<a href="http://colab.research.google.com#create=true">建立新的 Colab 筆記本</a>。

Colab 筆記本是由 Colab 代管的 Jupyter 筆記本。如要進一步瞭解 Jupyter 專案，請參閱 <a href="https://www.jupyter.org">jupyter.org</a>。

## 數據資料學

Colab 可讓你充分利用熱門 Python 程式庫的強大功能，對資料進行分析並以視覺化方式呈現。下方的程式碼儲存格使用 <strong>numpy</strong> 來產生一些隨機性資料，並透過 <strong>matplotlib</strong> 將這些資料視覺化。按一下儲存格即可開始編輯程式碼。
"""

import numpy as np
from matplotlib import pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()

"""你可從自己的 Google 雲端硬碟帳戶 &#40;包括試算表&#41;、GitHub 和許多其他來源，將資料匯入 Colab 筆記本中。如要進一步瞭解如何匯入資料以及將 Colab 用於數據資料學，請參閱下方「<a href="#working-with-data">處理資料</a>」底下的連結。

## 機器學習

你只需要寫<a href="https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb">幾行程式碼</a>，即可透過 Colab 匯入圖片資料集、根據圖片資料集訓練圖片分類工具並評估模型。Colab 筆記本可在 Google 的雲端伺服器上執行程式碼，也就是說，您可以充分運用 Google 硬體的強大效能 &#40;包括 <a href="#using-accelerated-hardware">GPU 和 TPU</a>&#41;，而不必在意自己的電腦性能如何，因為你只要使用瀏覽器就可以了。

Colab 廣泛運用於機器學習社群，相關應用包括：
- 開始使用 TensorFlow
- 開發及訓練類神經網路
- 使用 TPU 進行實驗
- 推廣 AI 研究
- 建立教學課程

如要查看示範機器學習應用程式的範例 Colab 筆記本，請參閱下方的<a href="#machine-learning-examples">機器學習範例</a>。

## 其他資源

### 在 Colab 中使用筆記本
- [Colaboratory 總覽](/notebooks/basic_features_overview.ipynb)
- [Markdown 指南](/notebooks/markdown_guide.ipynb)
- [匯入程式庫及安裝依附元件](/notebooks/snippets/importing_libraries.ipynb)
- [儲存和載入 GitHub 中的筆記本](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)
- [互動式表單](/notebooks/forms.ipynb)
- [互動式小工具](/notebooks/widgets.ipynb)
- <img src="/img/new.png" height="20px" align="left" hspace="4px" alt="New"></img>
 [Colab 中的 TensorFlow 2](/notebooks/tensorflow_version.ipynb)

<a name="working-with-data"></a>
### 處理資料
- [載入資料：雲端硬碟、試算表及 Google Cloud Storage](/notebooks/io.ipynb) 
- [圖表：將資料視覺化](/notebooks/charts.ipynb)
- [開始使用 BigQuery](/notebooks/bigquery.ipynb)

### 機器學習密集課程
以下是一些 Google 線上機器學習課程的筆記本。詳情請參閱<a href="https://developers.google.com/machine-learning/crash-course/">完整的課程網站</a>。
- [Pandas DataFrame 簡介](https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/pandas_dataframe_ultraquick_tutorial.ipynb)
- [以 tf.keras 使用合成資料進行線性迴歸](https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/linear_regression_with_synthetic_data.ipynb)


<a name="using-accelerated-hardware"></a>
### 使用加速硬體
- [搭配 GPU 使用 TensorFlow](/notebooks/gpu.ipynb)
- [使用 TPU 的 TensorFlow](/notebooks/tpu.ipynb)

<a name="machine-learning-examples"></a>

## 機器學習範例

如想瞭解 Colaboratory 支援的互動式機器學習分析端對端範例，請參閱這些使用 <a href="https://tfhub.dev">TensorFlow Hub</a> 模型的教學課程。

一些精選範例如下：

- <a href="https://tensorflow.org/hub/tutorials/tf2_image_retraining">重新訓練圖片分類工具</a>：以預先訓練的圖片分類工具為基礎，建立一個分辨花朵的 Keras 模型。
- <a href="https://tensorflow.org/hub/tutorials/tf2_text_classification">文字分類</a>：將 IMDB 電影評論分類為<em>正面</em>或<em>負面</em>。
- <a href="https://tensorflow.org/hub/tutorials/tf2_arbitrary_image_stylization">風格轉換</a>：運用深度學習轉換圖片的風格。
- <a href="https://tensorflow.org/hub/tutorials/retrieval_with_tf_hub_universal_encoder_qa">支援多種語言的 Universal Sentence Encoder 問與答</a>：使用機器學習模型來回答 SQuAD 資料集的問題。
- <a href="https://tensorflow.org/hub/tutorials/tweening_conv3d">影片畫面內插</a>：預測影片在第一個與最後一個畫面之間的內容。
"""