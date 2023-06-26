# less_data_ink_ratio
Python script to quantify the Data Ink Ratio in your plot

# Background
データを可視化する上で伝えたい情報を効率的に伝達するグラフデザインが求められている。効率的なグラフデザインを定量する手法として、エドワード・タフテは、データインク比を定義した。データインク比は、作成されたグラフに対して、データのみを表すために使われるインクの量とグラフ全体に使われるインクの総量の比のことである。データインク比が高ければ高いほど、つまり、データのみを表すために使われるインクの量が多いほど、良いグラフィックであるとされる。
ここでは、作成したグラフについて、データインク比を定量するスクリプトを作成する。

# Ugase

## Install

```
# Install by pip from GitHub
pip install git+https://github.com/G708/less_data_ink_ratio

# Install repository from GitHub
git clone https://github.com/G708/less_data_ink_ratio.git
pip install requirements.txt
pip install opencv-python
```


## Requirements
- numPy
- matplotlib
- opencv-python

必要な環境はDockerfileによってもまとめている。
```
# Dockerから取得する
docker pull g708/less_data_ink_ratio
```

## Run script
```
# simple example
python3 data_ink_ratio.py --plot example_plot.py	

python3 data_ink_ratio.py -h
# usage: data_ink_ratio.py [-h] [--plot PLOT] [--threshold THRESHOLD] [-m {bgr2gray,hsv}] [-o OUTPUT]

# options:
#   -h, --help            show this help message and exit
#   --plot PLOT           plotを作成するpythonファイル名
#   --threshold THRESHOLD
#                         plot全体の色の濃さの閾値
# 						デフォルトは255(白)
#   -m {bgr2gray,hsv}, --method {bgr2gray,hsv}
#                         plot全体の色の濃さを定量する方法
# 						デフォルトはhsv
#   -o OUTPUT, --output OUTPUT
#                         plot全体の色の濃さを定量した画像ファイル名

```


