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

fully operational environment with both spyder and sunpy is named `sp1` @ work-pc

## Getting Data 

Used JSOC web interface to download HMI.IC images as required.`hmi.Ic_720s[2010.05.01/4380d@10d]` was used as the search string and a tar file was downloaded and extracted to `./data/`

## Final Outputs

[sunspots](./out/sunspots.png)
[ssn_plot](./out/ssn_plot.png)

A report was prepared and submitted at the end of the project.Attached [here.](https://www.overleaf.com/project/631767f90b86791026410d82)

