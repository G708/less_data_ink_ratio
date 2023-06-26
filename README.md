# less_data_ink_ratio
Python script to quantify the Data Ink Ratio in your plot

# Background
データを可視化する上で伝えたい情報を効率的に伝達するグラフデザインが求められている。効率的なグラフデザインを定量する手法として、エドワード・タフテは、データインク比を定義した。データインク比は、作成されたグラフに対して、データのみを表すために使われるインクの量とグラフ全体に使われるインクの総量の比のことである。データインク比が高ければ高いほど、つまり、データのみを表すために使われるインクの量が多いほど、良いグラフィックであるとされる。

# Aim
ここでは、作成したグラフについて、データインク比を定量するスクリプトを作成する。

# Ugase

## Install

```
# Install from GitHub
pip install git+https://github.com/G708/less_data_ink_ratio
```

## Requirements
- numPy
- matplotlib
- opencv-python

必要な環境はDockerfileによってもまとめている。
```
# Dockerから取得する
docker pull g708/less_data_ink_ratio

docker build -t less_data_ink_ratio .
docker run -it --rm -v $(pwd):/work less_data_ink_ratio
```

## Run script
```
python less_data_ink_ratio.py --plot <input_plot_script_file>
```




