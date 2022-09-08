# install instructions for sunpy

```
conda update --prefix /opt/anaconda3 anaconda
conda create --name space_phys python=3.9 ipython


#activate the venc. To isolate from my current python env
conda activate space_sphy

conda install -c anaconda spyder-kernels
conda install -c sunpy sunpy

# if the conda command fails (after spyder kernal there are some conflicts
pip install "sunpy[all]"
```

My fully operational environment with both spyder and sunpy `sp1`

## Getting Data 

Used JSOC web interface to download HMI.IC images as required.



